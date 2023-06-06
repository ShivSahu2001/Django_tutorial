from django.shortcuts import render, redirect


from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def deleteReceipe(request, id):
    print(id)
    querySet = Receipe.objects.get(id = id)
    querySet.delete()
    # return HttpResponse("a")
    return redirect("/receipes")

@login_required(login_url="/login/")
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


def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Credentials")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/receipes/")



    context = {'page': "Login Page"}
    return render(request, 'login.html', context)
    
@login_required(login_url="/login/")
def logoutPage(request):

    logout(request)
    return redirect("/login/")

def registerPage(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.warning(request, "Username already exist")
            return redirect("/register/")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        # To encrypt the password we use set_password method
        user.set_password(password)
        user.save()

        messages.success(request, "User Registered Successfully...")

        return redirect("/login/")

    context = {'page': "Register Page"}
    return render(request, 'register.html', context)

from django.db.models import Q,Sum 

def getStudents(request):
    querySet = Student.objects.all()

    # rank nased on the marks
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-studentAge', 'studentName')

    # for rank in ranks:
    #     print(rank.marks)

    # Filter with student name
    if request.GET.get("search"):
        search = request.GET.get("search")
        # querySet = querySet.filter(studentName__icontains = search)

        # For multiple column filter
        querySet = querySet.filter(
            Q(studentName__icontains = search) |
            Q(department__department__icontains = search) |
            Q(studentEmail__icontains = search) |
            Q(studentId__studentId__icontains = search) 
        )

    paginator = Paginator(querySet, 10)  # Show 10 students per page.

    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj.object_list)
    # 'pageObj': page_obj
    context = {'querySet' : page_obj }
    return render(request, 'report/students.html', context)


from vegetable.seed import generateReportCard
def showMarks(request, studentId):
    # generateReportCard()
    # sourcery skip: move-assign-in-block, use-next
    querySet = SubjectMarks.objects.filter(student__studentId__studentId = studentId)
    totalMarks = querySet.aggregate(totalMarks = Sum('marks'))
    # currentRank = -1
    # ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks', '-studentAge', 'studentName')

    # i = 1
    # for rank in ranks:
    #     print(rank.studentId)
    #     if studentId == rank.studentId.studentId:
    #         currentRank = i
    #         break
    #     i = i + 1
    # print(totalMarks)
    # , 'currentRank': currentRank
    context = {'querySet': querySet, 'totalMarks': totalMarks}
    return render(request, 'report/showMarks.html', context)
