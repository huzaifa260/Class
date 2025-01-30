from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student, user, Receipt
from .serializers import StudentSerializer, UserSerializer, ReceiptSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if user:
        return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


def get_max_sr(request):
    # Get the current max sr value
    max_sr = Student.objects.aggregate(Max('sr'))['sr__max'] or 0
    return JsonResponse({'max_sr': max_sr + 1})  # Return the next sr value
