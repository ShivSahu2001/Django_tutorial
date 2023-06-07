from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
User = get_user_model()

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(isDeleted = False)

class Receipe(models.Model):
    # on_delete= models.CASCADE means If user is deleted then all the corresponding receipe will be deleted of that user

    # on_delete= models.SET_NULL if user is deleted than the user will be set to null and also receipes will be set to null

    # on_delete= models.SET_DEFAULT if user is deleted than we can set default user


    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    receipeName = models.CharField(max_length=100)
    receipeDescription = models.TextField()
    receipeImage = models.ImageField(upload_to="receipe")
    receipeViewCount = models.IntegerField(default=1)
    

  

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    studentId = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.studentId
    
class Subject(models.Model):
    subjectName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subjectName

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    studentId = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    studentName = models.CharField(max_length=100)
    studentEmail = models.EmailField(unique=True)
    studentAge = models.IntegerField(default=1)
    studentAddress = models.TextField()
    isDeleted = models.BooleanField(default=False)

      # By default Model Manager
    #   This will filter the (isDeleted = True) rows. and show the results 
    objects = StudentManager()

    # It will show all the rows including (is_deleted=True) field also
    adminObjects = models.Manager()

    
    def __str__(self) -> str:
        return self.studentName

    class Meta:
        # ordering means --> it will sort according studentName in ascending order
        # if you want in descending order then do '-studentName'
        ordering = ['studentName']
        # verbose_name --> table will be save with the name "student"
        verbose_name = "student"

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.studentName} has {self.subject.subjectName}"

    class Meta:
        # unique_together --> one unique student have one each unique subjects
        unique_together = ['student', 'subject']

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete=models.CASCADE)
    studentRank = models.IntegerField()
    dateOfReportCardGeneration = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['studentRank', 'dateOfReportCardGeneration']


