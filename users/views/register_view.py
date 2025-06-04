from rest_framework import generics, status
from rest_framework.response import Response
from users.serializers.register_serializer import RegisterSerializer
from rest_framework.permissions import AllowAny
from users.views.email_verification_view import EmailVerView
from users.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=['Register'],
    operation_summary="Register new user"
))

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save() 
        user.is_active = False
        user.save()

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        verification_link = f"http://127.0.0.1:8000/users/verify-email/{uid}/{token}/"

        send_mail(
            subject="Verify your email",
            message=f"Click the link to verify your account: {verification_link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )

        return Response({
            "message": "User registered successfully. Please check your email to verify your account.",
            "user": self.get_serializer(user).data,
        }, status=status.HTTP_201_CREATED)