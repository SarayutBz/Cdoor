# users/views.py

from django.http import JsonResponse
from django.views import View
from .models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user = User.objects.create(
                username=data['username'],
                password_hash=data['password_hash'],
                email=data['email']
            )
            return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)

class UserListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values('id', 'username', 'email')
        return JsonResponse(list(users), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(View):
    def get(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            user_data = {'id': user.id, 'username': user.username, 'email': user.email}
            return JsonResponse(user_data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

    def put(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            data = json.loads(request.body)
            user.username = data.get('username', user.username)
            user.password_hash = data.get('password_hash', user.password_hash)
            user.email = data.get('email', user.email)
            user.save()
            return JsonResponse({'id': user.id, 'username': user.username, 'email': user.email}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    def delete(self, request, user_id, *args, **kwargs):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=204)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
