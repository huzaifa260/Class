from django.db.models import Max
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student, user, Receipt
from .serializers import StudentSerializer, UserSerializer, ReceiptSerializer
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fees_type']  # or 'fees_type' if that's your field's name


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # to add filter in api url like sr=2 we need to add get_queryset or django filters
        # here we will see get_queryset()
        queryset = user.objects.all()
        username = self.request.query_params.get('username', None)
        password = self.request.query_params.get('password', None)
        # here we fetch value of username & password with 'self.request.query_params.get'
        # this is require to fetch and in parameters ('username', None) 'username' is for
        # that we want username value and none is default value if nothing is there it will take None

        if username is not None and password is not None:
            queryset = queryset.filter(username=username, password=password)
        # here we add filter that username should match username pass in link and also password
        # and for only username & only password also we need to create filter
        elif username is not None:
            queryset = queryset.filter(username=username)
        elif password is not None:
            queryset = queryset.filter(password=password)

        return queryset
        # and than return the queryset but this method is complex direct djangofilter is easy


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    # to add filter in api url like sr=2 we add djangofilter
    # for this first install django_filters with pip install django_filters than import DjangoFilterBackend
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sr']
    # after presiquite it is very easy just define filter_backends variable and than
    # filterset_fields variable in which define which fields we require


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
