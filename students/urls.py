from django.urls import path

from students.views.auth import LoginView, LogoutView, register_page, verify_email_done, verify_email_confirm, verify_email_complete
from students.views.views import StudentSignUpView, share_mail
urlpatterns = [
    path('Login/', LoginView.as_view(), name='login'),
    path('Logout/', LogoutView.as_view(), name='logout'),
    path('Register/', register_page, name='register'),
    path('Students/', StudentSignUpView.as_view(), name='students'),
    path('sending-mail/', share_mail, name='share_email'),
    path('verify-email-done/', verify_email_done, name='verify_email_done'),
    path('verify-email-confirm/<uidb64>/<token>/', verify_email_confirm, name='verify-email-confirm'),
    path('verify-email-complete/', verify_email_complete, name='verify_email_complete'),
]