from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims to the token payload
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        token['is_farmer'] = user.is_farmer
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom user info in login response
        data['username'] = self.user.username
        data['is_admin'] = self.user.is_admin
        data['is_farmer'] = self.user.is_farmer
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
