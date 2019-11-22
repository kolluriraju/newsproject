from django.shortcuts import render
from django.http import HttpResponse
from newsapp.models import Student
# Create your views here.
def index(request):
    return render(request,'newsapp/index.html')

def moviesinfo(request):
    head_msg='Latest Movie information'
    msg1='sharukhan new movie released'
    msg2='kajal in movie'
    msg3='modi wonder'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest sports Movie information'
    msg1='criket new game'
    msg2='first gold achived by sindhu'
    msg3='all are geraetr'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)

    return render(request,'newsapp/news.html')

def politicsinfo(request):
    head_msg='Latest politics information'
    msg1='TSRTS SAMME BUSESS'
    msg2='HEVIEY RAIN'
    msg3='SOFTWARE JOBS MORE IN HYDERABAD'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsapp/news.html',context=my_dict)
def studentview(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'newsapp/student.html',context=my_dict)
