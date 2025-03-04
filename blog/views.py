from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from blog.models import post, Bikes
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForms

# appName = [
#         {'id':1, 'names': 'post1', 'content': 'viewing post one'},
#         {'id':2, 'names': 'post2', 'content': 'viewing post two'},
#         {'id':3,'names': 'post3', 'content': 'viewing post three'},
#         {'id':4, 'names': 'post4', 'content': 'viewing post four'},
        
#     ]

# Create your views here.
def index(request):
    allpost = post.objects.all()
    page = Paginator(allpost, 3)
    # request object gives the page num
    page_number= request.GET.get("page")
    page_obj = page.get_page(page_number)

    return render(request, 'index.html', {"page_obj": page_obj})


def detail(request, slug):
    try:
        items = post.objects.get(slug=slug)
        relatedpost=  post.objects.filter(catagory= items.catagory).exclude(pk=items.id)
        
    except post.DoesNotExist:
        raise Http404("POST ENOUGH FOUND ERROR")
    # items = next((item for item in appName if item['id'] == int(post_id)), "None")
    return render(request, 'detail.html', {'posts': items, 'relatedpost': relatedpost})

def contact(request):
    if request.method == "POST":
        form = ContactForms(request.POST) 
        logger = logging.getLogger("TESTING")
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message') 
        if form.is_valid():
            form.save()
            success_msg= "Your Form Validation is Sent"
            logger.debug("your form valid is {} {}".format(form.cleaned_data['name'], form.cleaned_data['email']))
            return render(request, 'contact.html' ,{'forms': form, 'success_msg': success_msg})
        else:
            logger.debug("your validations failed")
            return render(request, 'contact.html', {'forms': form, 'name': name, 'email': email, 'message': message})
    return render(request, 'contact.html')

def about(request):
    content = Bikes.objects.first().content
    return render(request, 'about.html', {'content': content})