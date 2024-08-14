from django.urls import path
from .views import ReviewListView, ReviewDetailView, CreateReviewView

urlpatterns = [
    path('Reviews/', ReviewListView.as_view(), name='review-list'),
    path('Reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
    path('Reviews/create/', CreateReviewView.as_view(), name='create-review'),
]

