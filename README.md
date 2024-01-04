# Python Email with Embedded HTML and Plain Text


This Python script exemplifies the elegant creation and dispatching of HTML emails featuring embedded images and a fallback plain text version. Leveraging the `email` library, this script constructs a multipart MIME message, allowing for optimal rendering in diverse email clients.

## Instructions

1. Update `strFrom` and `strTo` with your email addresses.
2. Set the SMTP server details in `smtp.connect()` for your specific email provider.
3. Input your login credentials in `smtp.login()` to authenticate with your email server.
4. Execute the script to send the meticulously crafted email.

## Prerequisites

- Python
- Access to an SMTP server (e.g., Gmail, Outlook)

## Usage

```bash
python send_html_email.py
