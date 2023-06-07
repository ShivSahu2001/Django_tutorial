from home.models import Student
import time
from django.core.mail import send_mail 
from django.conf import settings

def runFunction():
    print("Function Started")
    time.sleep(2)
    print("Function executed")


def sendMailToUser():
    subject = "Email from Django Server"
    message="This is a test message from Django server email"
    from_email=settings.EMAIL_HOST_USER
    recipientList = ["shivsahu495@gmail.com"]
    send_mail(subject, message, from_email, recipientList)