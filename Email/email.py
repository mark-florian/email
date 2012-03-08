# Import smtplib for the actual sending function
import smtplib
import email.mime.text

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText('Hello, world!')
#fp.close()

me = 'me@me.com'
you = 'marknflorian@gmail.com'
msg['Subject'] = 'Hello'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()