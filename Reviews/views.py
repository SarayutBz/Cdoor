from django.http import JsonResponse, HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Review
import json

@method_decorator(csrf_exempt, name='dispatch')
class ReviewListView(View):
    def get(self, request):
        reviews = Review.objects.all()
        reviews_data = [
            {
                "id": review.id,
                "property": review.property_id,
                "user": review.user_id,
                "rating": review.rating,
                "comment": review.comment,
                "created_at": review.created_at
            } for review in reviews
        ]
        return JsonResponse(reviews_data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class ReviewDetailView(View):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
            review_data = {
                "id": review.id,
                "property": review.property_id,
                "user": review.user_id,
                "rating": review.rating,
                "comment": review.comment,
                "created_at": review.created_at
            }
            return JsonResponse(review_data, status=200)
        except Review.DoesNotExist:
            return JsonResponse({'error': 'Review not found'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')
class CreateReviewView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            review = Review(
                property_id=data.get('property'),
                user=request.user,  # ใช้ผู้ใช้ที่ล็อกอินในปัจจุบัน
                rating=data.get('rating'),
                comment=data.get('comment')
            )
            review.save()
            return JsonResponse({'id': review.id, 'message': 'Review created successfully!'}, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
