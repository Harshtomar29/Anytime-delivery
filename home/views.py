from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Courier
from home.models import Reserve
from home.models import Orders
from django.contrib import messages


# Create your views here.
def index (request):

     context= {
         "variable1" : "Harsh is great",
         "variable2" : "Harry is great"

     }

     return render (request , 'index.html', context)   
   # return HttpResponse("this is homepage")

def about (request):

    return render (request,'about.html')
   # return HttpResponse("this is aboutpage")




    return render (request,'services.html')
    #r eturn HttpResponse("this is services page")
#make migration and migrate ka khyal rakhna h

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')

def courier(request):
    if request.method=="POST":
        Sname=request.POST.get("Sname")
        Sphone=request.POST.get("Sphone")
        pick=request.POST.get("pick")
        Rname=request.POST.get("Rname")
        Rphone=request.POST.get("Rphone")
        drop=request.POST.get("drop")
        package=request.POST.get("package")

        courier=Courier(Sname=Sname,Sphone=Sphone,pick=pick,Rname=Rname,Rphone=Rphone,drop=drop,package=package,date=datetime.today())
        courier.save()
    return render (request,"courier.html" )


 
     
def orders (request):
     if request.method == "POST":
        name = request.POST.get('name')
        phone= request.POST.get('phone')
        product = request.POST.get('product')
        Quantity = request.POST.get('Quantity')
        details = request.POST.get('details')

        Address = request.POST.get('Address')
        
        orders =Orders(name=name, phone=phone, product=product ,Quantity=Quantity,details=details, Address=Address,date = datetime.today() )
        orders.save()



     return render (request,'orders.html')
      

def reservation (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        plan= request.POST.get('plan')
        occasion = request.POST.get('occasion')
        Address = request.POST.get('Address')

        reservation=Reserve(name=name,email=email,plan=plan,occasion=occasion,Address=Address,date = datetime.today())
        reservation.save()
         
    return render (request,'reservation.html')



#https://source.unsplash.com/1600x600/?icecream,ice