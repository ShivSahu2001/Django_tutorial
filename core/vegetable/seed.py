from faker import Faker
fake = Faker()
import random
from .models import *

def createSubjectMarks(n):
     try:
          studentObjs = Student.objects.all()
          for student in studentObjs:
               subjectObj = Subject.objects.all() 
               for subject in subjectObj:
                    SubjectMarks.objects.create(
                         subject = subject,
                         student = student,
                         marks = random.randint(20, 100)
                    )

     except Exception as e:
        print(e)


def seedDb(n=10) -> None:
    try:
        for _ in range(0, n):
            #[1, 2, 3, 4]
                departmentObj = Department.objects.all()
                randomIndex = random.randint(0, len(departmentObj)-1)
                department = departmentObj[randomIndex]
                studentId  = f'STU-00{random.randint(50, 999)}'
                studentName = fake.name()
                studentEmail = fake.email()
                studentAge =  random.randint(18, 25)
                studentAddress = fake.address()

                studentIdObj = StudentID.objects.create(studentId = studentId)

                studentObj  = Student.objects.create(
                    department = department,
                    studentId = studentIdObj,
                    studentName = studentName,
                    studentEmail = studentEmail,
                    studentAge = studentAge,
                    studentAddress = studentAddress,
                )

    except Exception as e:
         print(e)