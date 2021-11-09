from django.core import paginator
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
import random, json,requests,ast
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from .models import Popular, Feedback, Menu,News

# Create your views here.

def popular_view(request):
    popular=Popular.objects.all()
    return render(request, 'home/index.html', {'popular':popular})

def feedback_view(request):
    feedback=Feedback.objects.all()
    return render(request, 'home/index.html', {'feedback':feedback})

def menu_view(request):
    menu=Menu.objects.all()
    return render(request, 'home/index.html', {'menu':menu})

def news_view(request):
    news=News.objects.all()
    return render(request, 'home/index.html', {'news':news})
