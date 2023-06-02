from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def receipes(request):
    # To get data from frontend to backend
    if request.method == "POST":

        data = request.POST

        receipeName = data.get('receipeName')
        receipeDescription = data.get('receipeDesc')
        receipeImage = request.FILES.get('receipeImage')

        # print(receipeName)
        # print(receipeDescription)
        # print(receipeImage)

        Receipe.objects.create(
            receipeName = receipeName,
            receipeDescription = receipeDescription, 
            receipeImage = receipeImage,
        )

        return redirect("/receipes")


    context = {'page': 'Receipe'}
    return render(request, 'receipe.html', context)