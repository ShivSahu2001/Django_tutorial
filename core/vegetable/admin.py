from django.contrib import admin

# Register your models here.

from .models import *
from django.db.models import Sum

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


admin.site.register(SubjectMarks, SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'studentRank', 'totalMarks', 'dateOfReportCardGeneration']
    ordering = ['studentRank']

    def totalMarks(self, obj):
        subjectMarks = SubjectMarks.objects.filter(student = obj.student)

        marks = subjectMarks.aggregate(marks = Sum('marks'))
        # print()
        return marks['marks']

admin.site.register(ReportCard, ReportCardAdmin)
