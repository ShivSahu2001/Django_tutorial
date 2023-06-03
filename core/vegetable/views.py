from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
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

    querySet = Receipe.objects.all()

    if request.GET.get('mysearch'):
        # print(request.GET.get('mysearch'))
        
        # __icontains --> search for specific character if match return it.
        querySet = querySet.filter(receipeName__icontains = request.GET.get('mysearch'))
    
    context = {'page': 'Receipe', 'receipes': querySet}
    return render(request, 'receipe.html', context)

def deleteReceipe(request, id):
    print(id)
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    # return HttpResponse("a")
    return redirect("/receipes")

def updateReceipe(request, id):
    print(id)
    querySet = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        receipeName = data.get('receipeName')
        receipeDescription = data.get('receipeDesc')
        receipeImage = request.FILES.get('receipeImage')

        querySet.receipeName = receipeName
        querySet.receipeDescription = receipeDescription

        if receipeImage:
             querySet.receipeImage = receipeImage

        querySet.save()
        return redirect("/receipes")

    context = {'page': 'Update Receipe','receipe': querySet}
    return render(request, 'updateReceipe.html', context)
