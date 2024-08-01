from django.shortcuts import render, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login
from django.views import View

from students.forms import *



# Create your views here.

def share_mail(request):
    sent = False
    if request.method == 'Post':
        form = ShareMail(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            form_email = settings.DEFAULT_FROM_EMAIL
            recipients = form.cleaned_data['recipients']
            send_mail(subject, body, form_email, recipients, fail_silently=False)
            sent = True

    else:
        form = ShareMail()

    return render(request, 'students/email/share_email.html', {'form': form, 'sent': sent})

class StudentSignUpView(View):
    def get(self, request):
        form = StudentSignUpForm()
        return render(request, 'blog/index.html', {'form': form})

    def post(self, request):
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            user = request.user
            student.user = user
            student.save()
            return redirect('index')
        return render(request, 'blog/index.html', {'form': form})


