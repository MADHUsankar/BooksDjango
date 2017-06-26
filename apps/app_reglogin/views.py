# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User 
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    #User.objects.all().delete()
    context = {
        'users' :  User.objects.all()
    }
    print context
    return render(request,'app_reglogin/index.html', context)

def registration(request):
    result = User.objects.register(request.POST)
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
    else:
        messages.success(request,"Successful")
    return redirect(reverse('users:my_index'))
 
def loginuser(request):
    result = User.objects.loginval(request.POST)
    
    if not result['status']:
        for error in result['errors']:
            messages.error(request,error)
        return redirect(reverse('users:my_index'))
    else:
        messages.success(request,"Successful")
        request.session['emailid'] = result['user'].emailid
        request.session['first_name'] = result['user'].first_name
        request.session['user_id'] = result['user'].id
        print result['user'].emailid
        return redirect(reverse('books:home_page'))

