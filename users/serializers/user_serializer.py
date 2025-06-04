from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'avatar', 'date_joined', 'last_login']
        read_only_fields = ['email', 'date_joined', 'last_login']
