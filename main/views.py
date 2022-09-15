from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from .models import projects
from django.contrib import messages
# Create your views here.


def home(request):
    # form = feedbackForm(request.POST)
    # if form.is_valid():
    #     emailId = form.cleaned_data.get('emailId')
    #     message = form.cleaned_data.get('message')
    #     message = "From : " + emailId + "\n" + message
    #     subject = form.cleaned_data.get('subject')
    #     send_mail(
    #         subject, 
    #         message, 
    #         'senders117@gmail.com', 
    #         ['portfolioreciever@gmail.com'],
    #         fail_silently=False
    #         )
    #     form.save()
    #     messages.success(request, 'Thank You for your Feedback :) !!')
    #     return redirect('home')
    return render(request, 'main/index.html', {'projects': projects.objects.all()})
