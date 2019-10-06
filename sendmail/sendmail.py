import smtplib
from email.mime.text import MIMEText

def send_warning(gmail_ID, PW, to_email, times):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_ID, PW)
    msg = MIMEText('Abuese Suspicious!')
    msg['Subject'] = makeText(times)
    s.sendmail(gmail_ID, to_email, msg.as_string())

    s.quit()
    return True

def makeText(times):
    text = "Suspicious of abuse at times below\n\n"

    for key in times:
        text += str(int(float(times[key][0])/1000)) + " ~ " + str(int(float(times[key][1])/1000)) + "\n"

    text += "\n"

    return text
