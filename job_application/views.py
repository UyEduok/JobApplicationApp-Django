from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            email = form.cleaned_data['email']
            occupation = form.cleaned_data['occupation']
            print(first_name)

            Form.objects.create(first_name=first_name, last_name=last_name,
                                date=date, email=email, occupation=occupation)

            message_body = f"Thanks for your application, {first_name} "
            email_message = EmailMessage('Application Submission', message_body, to=[email])
            email_message.send()

            messages.success(request, f'Hi {first_name} your application was submitted successfully')
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
