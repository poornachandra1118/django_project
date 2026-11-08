from django.db import models

# Create your models here.
from datetime import *


class Course_type(models.Model):
    course_type=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.course_type)

class Courses(models.Model):
    course_type=models.ForeignKey(Course_type,on_delete=models.CASCADE,null=True,blank=True)
    Course_name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return str(self.Course_name)


class Student_details(models.Model):
    Student_id=models.CharField(max_length=100,null=False,blank=False)
    Student_Name=models.CharField(max_length=120,null=True,blank=True)
    Student_Mobile=models.CharField(max_length=10,null=True,blank=True)
    Student_Email=models.EmailField(max_length=120,null=True,blank=True)
    Student_Courses=models.ManyToManyField(Courses,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)
    Student_profile=models.ImageField(upload_to='Student_profile',null=False,blank=False)
    Enrollment_date=models.DateTimeField(default=datetime.now())
    Course_validity=models.DateField(default=date.today())
    

class Topic_videos(models.Model):
    Topic_name=models.ForeignKey(Courses,on_delete=models.CASCADE,null=False,blank=False)
    Title=models.CharField(max_length=200,null=True,blank=True)
    recorded_video=models.FileField(upload_to='Topic_videos')
    



# student_details  with out courses

# Course_allocation

# student_details with courses

