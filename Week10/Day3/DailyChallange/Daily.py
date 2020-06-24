from github import Github
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path = "C:/Users/USER/Desktop/token.txt"
with open(path, "r") as file:
    token = file.read()
    g = Github(token)  # safer alternative, if you have an access token
    u = g.get_user()
    repo = u.create_repo("HW repo")
    path = "D:\Developers Institute\git\Week10\Day3\DailyChallange\daily.py"
    with open (path, "r") as content:
        repo.create_file(path,"commit test",content.read())
path = "C:/Users/USER/Desktop/emailpassword.txt"

with open(path,"r") as file:
    email_password = file.read()

    mail_content = """Hi Eyal,
    THe HW is updated in the the repo - https://github.com/arturisto/HW-repo
    and also in my main github folder: https://github.com/arturisto/Dev-Inst/tree/master/Week10/Day3/DailyChallange
    Thanks,
    Arthur
    """
    #The mail addresses and password
    sender_address = 'arthurr.ie@gmail.com'
    sender_pass = email_password
    receiver_address = 'eyal.work@chocron.eu'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Week 10, day 3 daily challange by Arthur'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
