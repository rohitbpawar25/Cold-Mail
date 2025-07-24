# ColdMail: Automated Cold Email Sender in Python
---

## 📌 Objective
**ColdMail** Is A Python-Based Automation Tool Designed To Streamline The Process Of Sending Personalized Cold Emails For Job Outreach Or Hiring Purposes. Whether You're Reaching Out To Potential Employers, Recruiters, Or Candidates, This Script Helps Craft And Send Customized Messages At Scale, Increasing Your Chances Of Engagement And Response.

---

## 🔧 Features

- ✅ **Automated Email Sending** – Send multiple personalized emails with a single script execution.
- 📬 **CSV Integration** – Load recipient details (like name, email, role, company) from a CSV file.
- ✉️ **Dynamic Email Templates** – Customize subject and body with placeholders for personalized messages.
- 🔐 **Secure SMTP Authentication** – Connects to your email provider using secure credentials.
- 🧪 **Dry Run Mode** – Test emails without actually sending them (ideal for previewing output).
- 📊 **Logs & Feedback** – Get a summary of sent, failed, or skipped emails after execution.
  
## ⚙️ How to Use

### 🎯 Command-Line Input

- **python ColdMail.py  HRMailDetails.csv  Resume.pdf**

- ## 🔄 Flow of Program

```
graph TD

    A[main()] --> B[validateFilePaths(csv_path, resume_path)]
    B --> C{Are paths valid?}
    C -- No --> D[Exit program]
    C -- Yes --> E[SendMail(gmail_csv, resume_path)]
    E --> F[Read recipient data from CSV]
    F --> G[For each recipient]
    G --> H[Compose Email (with resume attachment)]
    H --> I[Connect to SMTP and Send Email]
    I --> J[Log Success or Failure]
    J --> K[Write Final Summary to Mail_log.txt]

# ========================
# Script starts executing here
# ========================
if __name__ == "__main__":
    main()  # Entry point of the script

# ========================
# Main function starts
# ========================
def main():
    # Accept command-line arguments from user
    # If incorrect arguments → print usage and exit
    # If valid arguments (CSV path, Resume path) provided:
    #     → Validate both paths using validateFilePaths()
    #     → If valid, call SendMail() to begin sending

# ========================
# Validates input files
# ========================
def validateFilePaths(csv_path, resume_path):
    # Check if both files exist on the filesystem
    # If either is missing → print error and return False
    # Return True if both files exist

# ========================
# Called from main() after validation
# ========================
def SendMail(gmail_csv, resume_path):
    # Initialize log file in same directory as CSV
    # Read all rows from CSV using csv.DictReader
    # Initialize counts: total, sent, failed

    # For each row in CSV:
    #     → Extract sender, receiver, subject, body from columns
    #     → Load resume file in binary mode
    #     → Create an EmailMessage with subject, body, and attachment
    #     → Try sending email over SMTP with TLS
    #         - If success: increment sent count and log success
    #         - If failure: increment fail count and log error

    # At the end:
    #     → Call LogHeaderFooter() to write summary into Mail_log.txt

# ========================
# Called at the end of SendMail()
# ========================
def LogHeaderFooter(log_path, total_emails, sent_count, fail_count, start_time, email_logs):
    # Create a well-formatted log file with:
    #     → Header, timestamp, counts
    #     → Details of each email's status
    #     → Summary and footer

# ========================
# Final result:
#     → Reads HR contact data from CSV
#     → Sends personalized cold emails with resume
#     → Logs every success/failure in Mail_log.txt
#     → Outputs a clear summary of total, sent, failed emails
# ========================
```

## 🧾 Conclusion

ColdMail Automates Personalized Job Out Reach By Sending Resumes Via Email To HR Contacts, Logging All Activity With Clear Success/Failure Tracking.



