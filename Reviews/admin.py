from django.contrib import admin
from .models import Review, Property

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'property__name', 'comment')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')

