# ====================================================================================
# Script: Cold Mail Sender for HR Contacts
#
# Description:
#   - Sends personalized emails to multiple HR contacts listed in a CSV file.
#   - Attaches a specified resume file to each email.
#   - Logs the status of each email (sent or failed) in a log file.
#   - The log file includes a header, timestamp, total email count, sent count, failed count, and footer.
#
# CSV File Format (headers required):
#   SenderEmail,AppPassword,Email,Name,Subject,Body,Company
#
# Usage:
#   python script.py <Path_to_CSV> <Path_to_Resume>
#
# Example:
#   python script.py hr_contacts.csv My_Resume.pdf
# ====================================================================================

import csv
import os
import sys
import smtplib
from datetime import datetime
from email.message import EmailMessage

def validateFilePaths(csv_path, resume_path):
    if not os.path.exists(csv_path):
        print(f"Error: CSV file '{csv_path}' not found.")
        return False

    if not os.path.exists(resume_path):
        print(f"Error: Resume file '{resume_path}' not found.")
        return False

    return True

def LogHeaderFooter(log_path, total_emails, sent_count, fail_count, start_time, email_logs):
    border = "-" * 90
    fobj = open(log_path, 'w', encoding='utf-8')
    fobj.write(border + "\n")
    fobj.write("Cold Mail Send Details".center(90) + "\n")
    fobj.write(("Date: " + start_time.strftime("%Y-%m-%d") + "    Time: " + start_time.strftime("%H:%M:%S")).center(90) + "\n")
    fobj.write(border + "\n\n")

    summary = f"Total Emails Processed: {total_emails} | Sent: {sent_count} | Failed: {fail_count}"
    fobj.write(summary.center(90) + "\n\n")

    for line in email_logs:
        fobj.write(line + "\n")

    fobj.write("\n" + border + "\n")
    fobj.write("End".center(90) + "\n")
    fobj.write(border + "\n")
    fobj.close()

def SendMail(gmail_csv, resume_path):
    base_dir = os.path.dirname(os.path.abspath(gmail_csv))
    log_file = os.path.join(base_dir, 'Mail_log.txt')
    start_time = datetime.now()

    fobj = open(gmail_csv, newline='', encoding='utf-8')
    reader = list(csv.DictReader(fobj))
    fobj.close()

    total_emails = len(reader)
    sent_count = 0  
    fail_count = 0
    email_logs = []

    for row in reader:
        sender_email = row['SenderEmail']
        sender_password = row['AppPassword']
        receiver_email = row['Email']
        receiver_name = row['Name']
        subject = row['Subject']
        company_name = row.get('Company', 'the company')
        body_template = row['Body']
        body = body_template.format(Name=receiver_name, Company=company_name)

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(body)

        fobj = open(resume_path, 'rb')
        resume_data = fobj.read()
        fobj.close()

        msg.add_attachment(
            resume_data,
            maintype='application',
            subtype='octet-stream',
            filename=os.path.basename(resume_path)
        )

        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            smtp.quit()
            log_msg = f"Email sent to {receiver_name} ({receiver_email})"
            sent_count += 1
        except Exception as e:
            log_msg = f"Failed to send email to {receiver_name} ({receiver_email}) - Error: {e}"
            fail_count += 1

        email_logs.append(log_msg)

    LogHeaderFooter(log_file, total_emails, sent_count, fail_count, start_time, email_logs)

    summary = f"Total Emails Processed: {total_emails} | Sent: {sent_count} | Failed: {fail_count}"
    print(summary.center(90))

def main():
    border = "-" * 80
    print(border + "\n")
    print(" Script For Sending Mail to HR ".center(90) + "\n")
    print(border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This Script is Use To Send Mail to HR By Attaching the Resume ")
        elif sys.argv[1] in ("--u", "--U"):
            print("Usage: Python Script.py Mail.CSV Resume ")
        
    elif len(sys.argv) == 3:
        gmail = sys.argv[1]
        resume = sys.argv[2]

        if not validateFilePaths(gmail, resume):
            sys.exit(1)

        print("Program Running Successfully".center(90))
        print("Program is in Running State (Press [Ctrl + C] to Stop)\n".center(90))
        print(border + "\n")

        SendMail(gmail, resume)

    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags:")
        print("--h: Used to Display the Help")
        print("--u: Used to Display the Usage\n")

    print(border + "\n")
    print("Script End".center(90) + "\n")
    print(border + "\n")

if __name__ == "__main__":
    main()
