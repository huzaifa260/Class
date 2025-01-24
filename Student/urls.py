from django.urls import path, include
from .views import StudentViewSet, login_api, UserViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Students', StudentViewSet)
router.register(r'User', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_api, name="login_api"),
    path('get_max_sr/', views.get_max_sr, name='get_max_sr'),
]
#  made router and register it for api routing
