import json

from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Category


@csrf_exempt
def category(request):
    # リクエストされたカテゴリの登録を行う
    if request.method == 'POST':
        try:
            body_json = json.loads(request.body)
            category_name = body_json.get('category_name')
            
            if not category_name:
                return JsonResponse({'error': 'category_name is required'}, status=400)
                
            category = Category.objects.create(name=category_name)
            
            return JsonResponse({
                'success': True,
                'message': 'Category successfully saved.',
                'category': {
                    'id': category.id,
                    'name': category.name
                }
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    elif request.method == 'GET':
        qs = Category.objects.values('id', 'name')
        return JsonResponse({'categories': list(qs)})
        
    return JsonResponse({'error': 'Method not allowed'}, status=405)
