from django.shortcuts import render,redirect

# Create your views here.
from .models import *

from datetime import *

import random

from django.core.mail import send_mail
from LMS.settings import EMAIL_HOST_USER


def Student_login(req):
    if req.method=='POST':
        user=req.POST.get('username')
        password=req.POST.get('password')
        print(user,password)
        status=Student_details.objects.filter(Student_Email=user,password=password).exists()
        print(status)
        if  status:
            data= Student_details.objects.get(Student_Email=user,password=password)
            req.session['session_id']=data.id
            return redirect('Dashboard')
    return render(req,'Student/Login.html')



def Dashboard(req):
    try:
        if req.session.get('session_id')!=None:
            ss_id=req.session.get('session_id')
            data=Student_details.objects.get(id=ss_id)
            print(data)
            for x in data.Student_Courses.all():
                print(x)
            context={
                'data':data,
                'pk':None
            }
            return render(req,'Student/Dashboard.html',context)
        else:
            return redirect('Student_login')
    except:
        return redirect('Student_login')

def Course_details(req,pk=None):
    try:
        if req.session.get('session_id')!=None:
            ss_id=req.session.get('session_id')
            data=Student_details.objects.get(id=ss_id)
            print(data)
            FRONT_END=[]
            BACKEND=[]
            DATABASE=[]
            for x in data.Student_Courses.all():
                if str(x.course_type)=='FRONTEND':
                    FRONT_END.append(x)
                elif str(x.course_type)=='BACKEND':
                    BACKEND.append(x)
                elif str(x.course_type)=='DATABASE':
                    DATABASE.append(x)
            print(FRONT_END)
            print(BACKEND)
            print(DATABASE)
            Topics=None
            if str(pk)!='None':
                Topics=Topic_videos.objects.filter(Topic_name=pk)
                # print('Not None')
            
            
            context={
                'data':data,
                'FRONT_END':FRONT_END,
                'BACKEND':BACKEND,
                'DATABASE':DATABASE,
                'Topics':Topics
            }
            
            return render(req,'Student/Course_details.html',context)
        else:
            return redirect('Student_login')
    except:
        return redirect('Student_login')
   

def Profile(req):
    try:
        if req.session.get('session_id')!=None:
            ss_id=req.session.get('session_id')
            data=Student_details.objects.get(id=ss_id)
            context={
                'data':data,
              
            }
             
            return render(req,'Student/Profile.html',context)
        else:
            return redirect('Student_login')
    except:
        return redirect('Student_login')
    

def Admin_login(req):
    if req.method=='POST':
        user=req.POST.get('username')
        password=req.POST.get('password')
        print(user,password)
        if user=='ADMIN' and password=='ADMIN':
            req.session['Admin_session']='ADMIN'
            return redirect('Create_student')
    return render(req,'Admin/Admin_login.html')
    

def Create_student(req):
    try:
        if req.session.get('Admin_session')!=None:
            # student_id
            
            #
            
            # student courses
            # password
            # enrollment data and time
            
            if req.method=='POST':
                Name=req.POST.get('Name')
                Mobile=req.POST.get('Mobile')
                email=req.POST.get('Email')
                profile=req.FILES.get('profile')
                validity_date=req.POST.get('Validity_date')
                print(Name,Mobile,email,profile,validity_date)
                student_id='LMS'+str(Name)[0:3]+str(Mobile)[0:5]+str(validity_date)[0:4]+str(random.randint(0000,9999))
                print('Student id :',student_id)
                special_char='!@#$%^&*()_+|/'
                upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                lower_case='abcdefghijklmnopqrstuvwxyz'
                numerical='0123456789'
                student_password=str(Name)[0:4]+random.choice(special_char)+random.choice(upper_case)+random.choice(lower_case)+random.choice(numerical) + str(random.randint(0000,9999))
                print(student_password)
                subject='LMS USER PASSOWRD'
                message=f'Your LMS User Password Is Here :{student_password}'
                from_email=EMAIL_HOST_USER
                to_email=[email]
                
                print(subject,message,from_email,to_email)
                
                
                Student_details.objects.create(
                    Student_id=student_id,
                    Student_Name=Name,
                    Student_Email=email,
                    Student_Mobile=Mobile,
                    Student_profile=profile,
                    Enrollment_date=datetime.now(),
                    Course_validity=validity_date,
                    password=student_password,
                ).save()
                send_mail(
                    subject,
                    message,
                    from_email,
                    to_email,
                    fail_silently=False,
                )
                
                
                
            
           
             
            return render(req,'Admin/Create_student.html')
        else:
            return redirect('Admin_login')
    except Exception as e:
        print('exception ;',e)
        return redirect('Admin_login')

def Course_allocation(req):
    try:
        if req.session.get('Admin_session')!=None:
            std_data=Student_details.objects.all()
            all_courses=Courses.objects.all()
            if req.method=='POST':
                student_info=req.POST.get('student')
                course_info=req.POST.getlist('course')
                print(student_info,course_info)
                student=Student_details.objects.get(id=student_info)
                student.Student_Courses.set(course_info)
                student.save()
            content={
                'std_data':std_data,
                'all_courses':all_courses
            }
            return render(req,'Admin/Course_allocation.html',content)
        else:
            return redirect('Admin_login')
    except:
        return redirect('Admin_login')

    

def Videos_allocation(req):
    try:
        if req.session.get('Admin_session')!=None:
            all_course=Courses.objects.all()
            
            if req.method=='POST':
               course= req.POST.get('course')
               title= req.POST.get('title')
               video= req.FILES.get('video')
               print(course,title,video)
               Topic_videos.objects.create(
                   Topic_name_id=course,
                   Title=title,
                   recorded_video=video
               ).save()
            
            content={
                'all_course':all_course
            } 
            return render(req,'Admin/Videos_allocation.html',content)
        else:
            return redirect('Admin_login')
    except:
        return redirect('Admin_login')

   

def Student_data(req):
    try:
        if req.session.get('Admin_session')!=None:
            std_data=Student_details.objects.all()
            
            content={
                'std_data':std_data,
            }
            return render(req,'Admin/Student_details.html',content)
        else:
            return redirect('Admin_login')
    except:
        return redirect('Admin_login')

  