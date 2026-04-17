from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer


# =========================
# PAGE VIEWS
# =========================

def login_view(request):
    return render(request, 'login.html')


def signup_view(request):
    return render(request, 'signup.html')


def language_view(request):
    return render(request, 'language.html')


def home_view(request):
    return render(request, 'home.html')


def crop_guide_view(request):
    return render(request, 'crop-guide.html')


def pesticide_scanner_view(request):
    return render(request, 'pesticide-scanner.html')


def leaf_detection_view(request):
    return render(request, 'leaf-detection.html')


def market_price_view(request):
    return render(request, 'market-price.html')


# =========================
# API VIEWS
# =========================

@api_view(['POST'])
def signup_api(request):

    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message": "User created successfully",
            "username": user.username
        })

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login_api(request):

    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():

        user = serializer.validated_data['user']

        return Response({
            "message": "Login successful",
            "username": user.username,
            "language": user.language
        })

    return Response(serializer.errors, status=400)