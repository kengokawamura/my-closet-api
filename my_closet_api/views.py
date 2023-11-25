from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from .models import category

# Create your views here.

def create_category(request):
    category.objects.create(created_at=datetime.now(), updated_at=datetime.now(), name='test_1')
    return HttpResponse("category successfully saved.")