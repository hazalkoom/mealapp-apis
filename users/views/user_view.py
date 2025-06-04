from rest_framework.permissions import IsAuthenticated
from users.serializers.user_serializer import UserSerializer
from users.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

# @method_decorator(name='get', decorator=swagger_auto_schema(
#     tags=['Users'],
#     operation_summary="Get user profile"
# ))
# @method_decorator(name='put', decorator=swagger_auto_schema(
#     tags=['Users'], 
#     operation_summary="Update user profile"
# ))
# @method_decorator(name='delete', decorator=swagger_auto_schema(
#     tags=['Users'],
#     operation_summary="Delete user account"
# ))
class UserProfileView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user