import json

from django.http import HttpResponse
from django.core import serializers
from datetime import datetime
from .models import Category


def category(request):

    # リクエストされたカテゴリの登録を行う
    if request.method == 'PUT':
        body_json = json.loads(request.body)
        category_name = body_json.get('category_name')

        Category.objects.create(created_at=datetime.now(), updated_at=datetime.now(), name=category_name)

        return HttpResponse("category successfully saved.")
    elif request.method == 'GET':
    
        qs = Category.objects.values('id', 'name')

        return HttpResponse(json.dumps({'categories': list(qs)}), content_type="application/json")
