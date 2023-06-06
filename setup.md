always go to first virtual env
Then come to your actual folder
and run command
    --> python manage.py runserver

To create an App in Django
 --> python manage.py startapp Appname

To make migrations in Django you use command
    --> python manage.py makemigrations

To run the migrate in Django you use command 
    --> python manage.py migrate 

Want to use Django Shell then type command 
    --> python manage.py shell

To add or Create Data in DB in Django Shell
1) student = Student(name="Raj", address="Kurla")
    student.save()
2) student.objects.create(name="Raj", address="Kurla")

3) carData = {"carName": "Mahindra" , "speed": 140}
Car.objects.create(**carData)

To read Data

cars = Car.objects.all()
cars
    <QuerySet [<Car: Car object (1)>, <Car: Car object (2)>, <Car: Car object (3)>]>

2)  car = Car.objects.get(id = 1)
    car

To update Data

1)  car = Car.objects.get(id = 1)
car.speed = 180
car.save()

2) Car.objects.filter(id=1).update(carName= "BMW Superb")

To Delete Data
Car.objects.get(id=1).delete()

To create admin username and password we hit the command:
    --> python manage.py createsuperuser

Aggregate --> used to query on a  single column
Student.objects.aggregate(Min('studentAge')) 

Annotate --> used to make query on multiple columns
student = Student.objects.values('studentAge').annotate(Count('studentAge'))
O/P:  [{'studentAge': 18, 'studentAge__count': 11}, {'studentAge': 19, 'studentAge__count': 21}, {'studentAge': 20, 'studentAge__count': 17}, {'studentAge': 21, 'studentAge__count': 15}, {'studentAge': 22, 'studentAge__count': 16}, {'studentAge': 23, 'studentAge__count': 9}, {'studentAge': 24, 'studentAge__count': 16}, {'studentAge': 25, 'studentAge__count': 14}]


Adding multiple annotation
------------------------------------------------
student = Student.objects.values('department', 'studentAge').annotate(Count('department'),Count 
('studentAge')).values_list()


 <!--if there is a change in URL everytime we have to change the URL here  -->
 <!-- {% url 'showMarksPage' student.studentId %} by this way we don't have to change url everytime 'showMarksPage' here name field in urls.py -->