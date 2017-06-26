# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..app_reglogin.models import User
from .models import  Book, Author,Review
from django.core.urlresolvers import reverse

# Create your views here.
def homepage(request):
    #User.objects.all().delete()
    context = {
                    'books' :  Book.objects.all(),
                    'reviews' :  Review.objects.all(),
                    'author' :  Author.objects.all(),
                    "name": request.session['first_name']                
                }
    print context
    return render(request,'app_book/homepage.html', context)

def addbook(request):
    #Book.objects.all().delete()
    ##Author.objects.all().delete()
    #Review.objects.all().delete()
    if request.method == "POST":
        print request.POST
        context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id']
                }
        print context
        result = Book.objects.addbook(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
                return redirect(reverse('books:add_book'))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('books:home_page'))
            
    else:
            print "ENTERED GET"
             
    return render(request,'app_book/addbook.html' )

def  showbook(request,id):
    print request.method
    if request.method == "POST":
        context = {
                "name": request.session['first_name'],
                "id" :request.session['user_id'],
                "bookid" : id
                }
        
        result = Review.objects.addreview(request.POST,context)
        print  result['status']
        if not result['status']:
             
            for error in result['errors']:
                messages.error(request,error)
                print "here"
                return redirect(reverse('books:show_book',kwargs={'id': id}))
        else: 
            messages.success(request,"Successful")
            return redirect(reverse('books:show_book',kwargs={'id': id}))
    else:
        context = {
        'bookdata' :Book.objects.get(id=id),
        'authordata' :Author.objects.get((bookauthor__id)=id),
        'reviewdata' :Review.objects.filter((bookreview__id)=id),
        'userid':request.session['user_id']

        }
        #return redirect(reverse('show',kwargs={'id':id}))
        return render(request,'app_book/showbook.html', context)
def showuser(request,id):
    context = {
        'userdata' :User.objects.get(id=id),
        #'bookdata' :Book.objects.get((userbook__id)=id),
        'reviewdata' :Review.objects.filter((userreview__id)=id)
        }
        #return redirect(reverse('show',kwargs={'id':id}))
    return render(request,'app_book/showuser.html', context)

def  deletereview(request,id):
    reviewdel = Review.objects.get(id=id)
    temp = reviewdel.bookreview.id
    Review.objects.filter(id=id).delete()
    return redirect(reverse('books:show_book',kwargs={'id': temp}))

def logout(request):
    request.session.clear()
    return redirect('users:my_index')

