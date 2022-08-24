from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions
from django.contrib.auth.models import User
from base.models import OmurInitials
from django.core.exceptions import ObjectDoesNotExist


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
        ]

    @staticmethod
    def get_name(obj):
        name = obj.first_name
        if name == "":
            return obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
            'token',
        ]

    @staticmethod
    def get_token(obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):

        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user)
        serialized_data = serializer.data

        for key, value in serialized_data.items():
            data[key] = value

        try:
            user = User.objects.get(email=data['email'])
            if not user.is_active:
                self.error_messages['no_active_account'] = (
                    'Bu hesap henüz aktif değil'
                )
                raise exceptions.AuthenticationFailed(
                    self.error_messages['no_active_account'],
                    'no_active_account',
                )
        except User.DoesNotExist:
            self.error_messages['no_active_account'] = (
                'Böyle bir hesap mevcut değil')
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        if self.user is None:
            self.error_messages['no_active_account'] = (
                'Verilen bilgiler eşleşmedi')
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )

        return data


class OmurInitialsSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OmurInitials
        fields = [
            'id',
            'commenter',
            'content',
            'created_at',
            'full_name',
        ]

    @staticmethod
    def get_full_name(obj):
        name = obj.commenter.get_full_name()
        if name == "":
            return obj.commenter.email
        return name