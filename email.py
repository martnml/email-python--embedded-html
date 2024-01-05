# @Author : Zergaoui Mohamed el Amine
# @version : v1.03
# @date : 01/07/2023
# @since : python 3.9.7


import os
import smtplib
import imghdr
# import request
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

if request.method == 'POST':
   subject = request.POST['subject']
   message = request.POST['message']
   email = request.POST['email']
   

contacts = ['exemple@gmail.com', 'exemple@gmail.com']

# Create the 'msg' message and fill in the from, to, and subject headers
msg = EmailMessage()
msg['Subject'] = 'Portfolio Message!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'exemple@gmail.com'

msg.set_content('This is a plain text email')

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h3 style="color:SlateGray;">email :"""+msg['To']+"""<br>subject"""+msg['Subject']+"""</h3>
    </body>
</html>
""", subtype='html')

# Send the email (this example assumes SMTP authentication is required)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("exemple@gmail.com", "Password")
    smtp.send_message(msg)

