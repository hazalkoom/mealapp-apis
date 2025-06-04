from rest_framework import generics, status, permissions
from rest_framework.response import Response
from users.serializers.change_password_serializer import ChangePasswordSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

@method_decorator(name='patch', decorator=swagger_auto_schema(
    tags=['Password-Change'],
    operation_summary="Change password"
))
@method_decorator(name='put', decorator=swagger_auto_schema(
    tags=['Password-Change'],
    operation_summary="Change password"
))
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"message": "Password updated successfully."}, status=status.HTTP_200_OK)
    
