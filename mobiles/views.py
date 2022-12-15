from django.shortcuts import render
from django.http import HttpResponse

from .models import MobileList
# Create your views here.


def home(request):
    return render(request,'index.html')

def new(request):
    return HttpResponse("Hello")

def index(request):
    return HttpResponse("Status-200")

def mob(request):
    store_name=['Lot','Big-C']
    brand =['vio','oppo']
    price =[20,30]
    storage= ['128','128']
    color=['black','blue']

    context2={
        'name':'store_name',
        'brand':brand,
        'price':price,
        'storage':storage,
        'color': color,
    
    
    }
    data = zip(brand,price,storage,color)
    print(data)

    context ={
        'data':data
    }
    return render(request,'index.html',context)

######################################################################


def index(request):
    a = """
    <button><a href="/about">About</a></button>
    <button><a href="/gallery">Gallery</a></button>
    <button><a href="/contact">Contact Us</a></button>
    <button><a href="/services">Services</a></button>

    """
    return HttpResponse(a)

def about(request):
    a = """
    <h1>ABout </h1>
    <button><a href="/index">Back</a></button>
    """

    return HttpResponse(a)
    # Testing function for urls
    # return render(request,"temp.html")

def gallery(request):
    a = """
        <h1>Gallery</h1>
        <button><a href="/index">Back</a></button>        
        """
    return HttpResponse(a)

def contact(request):
    a = """
        <h1>Contact </h1>
        <button><a href="/index">Back</a></button>              
        """
    return HttpResponse(a)

def services(request):
    a = """
    <h1>Services</h1>

    <button><a href="/index">Back</a></button>
    
    
    """
    return HttpResponse(a)
##############################################################
# test tutorials 

def test(request):
    return render(request,'test.html')



def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')
    analyzed=djtext
    params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")

    

def new(request):
    data = MobileList.objects.all()
    # brand=['vivo','realme']
    # price=['100','200']
    # color=['red','blue']
    # ram=['4gb','8gb']
    # storage=['128','215']

    print(data)

    context = {
        'data':data,
    }
    return render(request,'new.html',context)
