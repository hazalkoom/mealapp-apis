from django.urls import path
from .views.register_view import RegisterView
from .views.user_view import UserProfileView
from users.views.change_password_view import ChangePasswordView
from .views.password_reset_view import PasswordResetConfirmView, PasswordResetRequestView
from .views.email_verification_view import EmailVerView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    #path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('verify-email/<uidb64>/<token>/', EmailVerView.as_view(), name='verify-email')

]

# urlpatterns += [
#     path('verify-email/<uid>/<token>/', EmailVerView.as_view(), name='verify-email'),
# ]