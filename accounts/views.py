from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import JobApplication
from .models import ApplicationStatus
from .lookup_gmail import fetchJobApplications
from django.http import HttpResponseRedirect

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')

def updateJobApplication(request):
  if request.method == 'POST':
    user_job_app = JobApplication.objects.get(pk=request.POST['pk'])
    status = request.POST['ddStatus']
    if status == -1:
        pass
    else:
        user_job_app.applicationStatus = ApplicationStatus.objects.get(pk=status)
        user_job_app.save()
        messages.success(request, '.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  else:
    return dashboard(request)

def deleteJobApplication(request):
  if request.method == 'POST':
    user_job_app = JobApplication.objects.get(pk=request.POST['pk'])
    user_job_app.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
  else:
    return dashboard(request)    

def dashboard(request):
  user_job_apps = JobApplication.objects.filter(user_id=request.user.id).order_by('-applyDate')
  statuses = ApplicationStatus.objects.all()
  if request.user.social_auth.filter(provider='google-oauth2'):
      fetchJobApplications(request.user)

  context = {
    'job_apps': user_job_apps,
    'statuses': statuses
  }
  return render(request, 'accounts/dashboard.html', context)

"""
def addJobApplication(request):
 if request.method == 'POST':
   job_title = request.POST['job_title']
   company = request.POST['company']
   applicationdate = request.POST['applicationdate']
   status = request.POST['status']
   source = request.POST['source']
   japp = JobApplication(jobTitle=job_title, company=company, applyDate=applicationdate, msgId='', source =source, user = request.user)
   japp.applicationStatus = ApplicationStatus.objects.get(pk=status)
   japp.save()
   return dashboard(request)
   """

import json
def addJobApplication(request):
 if request.method == 'POST':
   body = json.loads(request.body)
   print(body)
   job_title = body['job_title']
   company = body['company']
   print(company)
   applicationdate = body['applicationdate']
   print(body['status'])
   status = int(body['status'])
   source = body['source']
  
   japp = JobApplication(jobTitle=job_title, company=company, applyDate=applicationdate, msgId='', source =source, user = request.user, companyLogo = '/static/images/errorcvlogotemporary.png')
   japp.applicationStatus = ApplicationStatus.objects.get(pk=status)
   japp.save()
   return HttpResponseRedirect('/accounts/dashboard')

def filterJobApplications(request):
  if request.method == 'POST':
    start = request.POST['start']
    end = request.POST['end']
    query = JobApplication.objects.filter(user_id=request.user.id)
    if start != '':
      query = query.filter(applyDate__gte=start)
    if end != '':
      query = query.filter(applyDate__lte=end)
    user_job_apps = query.order_by('-applyDate')
    statuses = ApplicationStatus.objects.all()
    context = {
      'job_apps': user_job_apps,
      'statuses': statuses
    }
    return render(request, 'accounts/dashboard.html', context)
  else:
    return dashboard(request)

