import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "your@gmail.com"
receiver_email = "sent-email@gmail.com"
password = "app key"

subject = "Interested in AI Automation & Data Analytics Position"
body = """Dear Sir,

I hope this message finds you well.
My name is "your-name", and I am writing to express my interest in the AI Automation and Data Analytics position at your organization.

Please find my CV attached for your review. I would be grateful for the opportunity to discuss how my skills and enthusiasm can add value to your organization.
Thank you for your time and consideration.

Kind regards,
your-name
Email:your-email@gmail.com
Phone: your-num
LinkedIn: your-linkedin-profile-link
Github: your-github-link

"""


msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# CV section
filename = "CV.pdf"   

attachment = open(filename, "rb")
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(part)

attachment.close()

# email send section

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, msg.as_string())
server.quit()

print("✅ Email Sent Successfully!")
