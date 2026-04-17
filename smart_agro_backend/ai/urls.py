from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_image, name='upload'),

    path('crop-guide/', views.crop_guide, name='crop_guide'),
    path('crop-result/', views.crop_result, name='crop_result'),

    path('pesticide-scanner/', views.pesticide_scanner, name='pesticide_scanner'),
    path('pesticide-result/', views.pesticide_result, name='pesticide_result'),

    path('market-price/', views.market_price, name='market_price'),
    path('market-price-result/', views.market_price_result, name='market_price_result'),    
]