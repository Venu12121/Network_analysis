import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(to_email, subject, message):
    # Email configuration
    sender_email = "argarg1254@gmail.com"
    sender_password = "arg733761"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())

# Example usage
if __name__ == "__main__":
    to_email = "venumuthyala12345@gmail.com"
    subject = "New Device Detected"
    message = "A new device has been detected on your network."
    send_email_alert(to_email, subject, message)
