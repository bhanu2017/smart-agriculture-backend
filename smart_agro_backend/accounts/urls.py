from django.urls import path
from . import views

urlpatterns = [
    # pages
    path('', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('language/', views.language_view, name="language"),
    path('home/', views.home_view, name="home"),

    # feature pages ✅ ADD THESE
    path('crop-guide/', views.crop_guide_view, name="crop_guide"),
    path('pesticide-scanner/', views.pesticide_scanner_view, name="pesticide_scanner"),
    path('leaf-detection/', views.leaf_detection_view, name="leaf_detection"),
    path('market-price/', views.market_price_view, name="market_price"),

    # APIs
    path('api/signup/', views.signup_api),
    path('api/login/', views.login_api),
]