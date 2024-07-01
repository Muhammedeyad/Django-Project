from django.urls import path
from . import views

app_name = 'bloging'

urlpatterns = [
    path("", views.index, name= "index"),
    path("detail/<str:slug>", views.detail, name='detail'),
    path("contact", views.contact, name='contact')
    
]


