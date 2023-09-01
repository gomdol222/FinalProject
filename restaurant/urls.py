from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('rest/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('rest/review/', views.restaurant_review, name='restaurant_review'),
    path('restaurant_account/', views.restaurant_account, name='restaurant_account'),
]
