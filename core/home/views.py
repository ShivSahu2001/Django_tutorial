from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse

from vegetable.seed import *
from .utils import sendMailToUser

def sendEmail(request):
    print("sent...")
    sendMailToUser()
    context = {'page': 'Send Mail'}
    return render(request, "sendMail.html", context )

def home(request):
    # seedDb(100)
    # return HttpResponse("<h1>Django Server is running....</h1>")
    peoples = [
        {'name': 'Raj', 'age': 20},
        {'name': 'Piyush', 'age': 23},
        {'name': 'Shyam', 'age': 24},
        {'name': 'Neha', 'age': 17},
        {'name': 'Bala', 'age': 22},
    ]

    text = '''Lorem, ipsum dolor sit amet consectetur adipisicing elit. Recusandae excepturi cum fugit maxime iusto dignissimos accusamus assumenda doloremque. Totam ipsum obcaecati voluptas quasi quod libero odio, culpa in officiis nam dolore. Magnam officia harum qui ullam minima enim, nesciunt, repellendus nisi maxime quidem quia consequatur quae blanditiis nostrum sed libero?'''

    colors = ["red", "green", "blue"]

    # Through context only we send backend data to frontend

    return render(request, "home/index.html", context= {'page': 'Home', 'peoples': peoples, 'text': text, 'colors': colors})

def contactPage(request):
    context = {'page': 'Contact'}
    return render(request, "contact.html", context )

def aboutPage(request):
    context = {'page': 'About'}
    return render(request, "about.html", context)

def successPage(request):
    return HttpResponse("<h1>Success 200 ok..</h1>")