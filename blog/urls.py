from django.urls import path
from . import views

app_name = 'bloging'

urlpatterns = [
    path("", views.index, name= "index"),
    path("detail/<str:post_id>", views.detail, name='detail')
    
]


