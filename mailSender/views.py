from django.shortcuts import render
from django.core.mail import EmailMessage
import os
from django.core.files.storage import FileSystemStorage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = 'testpay6397@gmail.com'
sender_password = 'kudiytqcbssgcugz'

def send_email(receiver_email, subject,message,attachPath=None):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    email = EmailMessage(subject, message, sender_email, [receiver_email])
    if attachPath:
        # Attach the file to the email
        with open(attachPath, 'rb') as file:
            email.attach_file(attachPath)
    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email.message().as_string())

def home(request):
    if request.method == 'POST':
        mailTo = request.POST['mailTo']
        subject = request.POST['subject']
        message = request.POST['message']
        attachFile = request.FILES['attachFile']
        # Call the function to delete all files in the media folder
        delete_all_files_in_media()
        # Save the uploaded PDF file to the media directory
        fss = FileSystemStorage()
        file = fss.save(attachFile.name, attachFile)
        attachPath =r'C:\Users\kushwah\OneDrive\Desktop\New folder (3)\mailSender\media\{}'.format(file)
        mails = mailTo.split(',')
        for i in mails:
            print(i)
            send_email(i, subject,message,attachPath)
        return render(request, 'index.html',{'mail_sent': True})
    return render(request, 'index.html')

def marketEmail(request):
    if request.method == 'POST':
        mailTo = request.POST['mailTo']
        subject = request.POST['subject']
        message = request.POST['message']
        mails = mailTo.split(',')
        for i in mails:
            print(i)
            emailForMarketting(i,subject,message)
        return render(request, 'marketMail.html',{'mail_sent': True})
    return render(request, 'marketMail.html')

def emailForMarketting(mailTo,subject,message):
        receiver_email = mailTo
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        subject = subject
        message = message
        body = message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))
        try:
            with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp_server:
                smtp_server.login(sender_email, sender_password)
                smtp_server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")        
        print("mail send")

def delete_all_files_in_media():
    media_path = r'C:\Users\kushwah\OneDrive\Desktop\New folder (3)\mailSender\media'
    for filename in os.listdir(media_path):
        file_path = os.path.join(media_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
