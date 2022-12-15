initializing project:
======================

# Downloading the virtualenv 

-pip install virtualenv

# Creating virtualEnvironment 

- python3 -m virtualenv <file-Name>

# Connecting to the ve

# for linux
  -source <file-Name>/bin/activate
# for windows
  -source <file-Name>/Scripts/activate
# install django 

- pip install django==2.2

# Creating the first project 

-Django-admin startproject <project-Name> .

# Running the project 

-python manage.py runserver 

# Creating apps in django

-python manage.py startapp mobiles

### Creating views.py and setting the path 
-create views.py file in the project and imort the following headers

"from django.http impor HttpResponse"

-create a function or method 

def ex1(request):
    return HttpResponse("Hello")

--After Completing the above steps set the path to the file as follows--

from . import views 

path('ex1',views.ex1,name="ex1")

here ex1= method name 

!!-taking files external html pages-!!
--------------------------------------

-first have to create a folder externally and in it create a index file 
-open the settings.py file go to the template section in template section there is a line named as DIRS rewrite it as follows 
       *before == 'DIRS': [ ]
       *After =='DIRS': [os.path.join(BASE_DIR,'templates')],
-the go to the views.py file and add following command
   from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

-After that open the urls.py file and set the path as follows 

from django.contrib import admin
from django.urls import path
from mobiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.home),

# Completed 