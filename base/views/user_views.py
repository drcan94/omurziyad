from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from django.db.models.query_utils import RegisterLookupMixin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    UserSerializerWithToken,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    default_error_messages = {
        "no_active_account": "Girilen bilgilere ait bir hesap bulunamadı!"
    }

