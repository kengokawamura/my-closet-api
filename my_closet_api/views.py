import json

from django.shortcuts import render
from django.http import HttpResponse, QueryDict

from datetime import datetime
from .models import category

# リクエストされたカテゴリの登録を行う

def create_category(request):
    if request.method == 'PUT':
        body_json = json.loads(request.body)
        category_name = body_json.get('category_name')

        category.objects.create(created_at=datetime.now(), updated_at=datetime.now(), name=category_name)

        return HttpResponse("category successfully saved.")
    
    return HttpResponse("request is not PUT")