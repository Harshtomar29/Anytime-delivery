from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("courier",views.courier,name="courier"),
    path("orders",views.orders,name="orders"),
    path("reservation",views.reservation,name="reservation")
   
    
]