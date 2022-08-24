from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializers import (
    MyTokenObtainPairSerializer,
)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


