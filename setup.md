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