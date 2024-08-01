from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import FormView

from students.models import User
from students.views.token import account_activation_token
from students.forms import LoginForm, RegisterModelForm
from django.views import View


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'students/auth/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
'''class RegisterFormView(FormView):
    template_name = 'students/auth/register.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.password = form.cleaned_data['password']
        user.save()
        login(self.request, user)
        return redirect('login')'''
def register_page(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.is_active = False

            user.set_password(password)
            user.save()


            send_mail('EduBoost','you successfully registered' , settings.DEFAULT_FROM_EMAIL, [user.email] ,fail_silently=False)

            return redirect('students')

        # send

    else:
        form = RegisterModelForm()

    return render(request, 'students/auth/register.html', {'form': form})

def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')

    return render(request, 'students/email/verify_email_confirm.html')



def verify_email_done(request):
    return render(request, 'students/email/verify_email_done.html')

def verify_email_complete(request):
    return render(request, 'students/email/verify_email_complete.html')