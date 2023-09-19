import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, subject, html_content):
    # SMTP server details
    smtp_server = 'google.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    from_address = 'your_email@example.com'

    # Create a MIMEText object to represent the email content
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS encryption
            server.starttls()
            # Log in to the SMTP server
            server.login(smtp_username, smtp_password)
            # Send the email
            server.sendmail(from_address, to_address, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print('Failed to send email:', str(e))

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    to_address = 'klatort@gmail.com'
    subject = 'Sample HTML Email'
    template_filename = 'email_template.html'

    # Read the HTML template
    html_template = read_template(template_filename)

    # Replace placeholders in the HTML template
    #html_content = html_template.replace('{name}', 'John Doe')

    # Send the email
    send_email(to_address, subject, html_template)

if __name__ == "__main__":
    main()
