# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_reglogin.models import User
from django.db import models
import bcrypt

class bookManager(models.Manager):
    def addbook(request,postData,sessiondata):
        print " In addbook %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        if not postData['book_title'] or len(postData['book_title'])<1:
            print "In validation1 "
            results['status'] = False
            results['errors'].append("Please enter a Book Name")
            

        if not postData['new_author'] or len(postData['new_author'])<1:
            print "In validation2 "
            results['status'] = False
            results['errors'].append("Please enter a Author Name")
            

        if not postData['review'] or  len(postData['review'])<1:
            print "In validation3 "
            results['status'] = False
            results['errors'].append("Please enter a Review")
        print "rating"
        print postData['rating']
        print int(postData['rating'])
        if int(postData['rating'])<1:
            print "In validation4 "
            results['status'] = False
            results['errors'].append("Please Provide a Rating")

        if results['status']:
            user1 = User.objects.get(id = sessiondata['id'])
            print "Successfully done@@@@@@@@@@@@@@"
            
            book1 = Book.objects.create(booktitle=postData['book_title'],userbook = user1)
            author1=Author.objects.create(authorname=postData['new_author'],bookauthor = book1)
            review1=Review.objects.create(reviewcontent=postData['review'],bookrating= postData['rating'],bookreview = book1,userreview=user1)
            print book1
            print author1
            print review1
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results

    def addreview(request,postData,sessiondata):
        print " In addbook %%%%%%%%%%%"
        results = {'status': True, 'errors': []}
        
        if not postData['review'] or  len(postData['review'])<1:
            print "In validation3 "
            results['status'] = False
            results['errors'].append("Please enter a Review")
           
        print int(postData['rating'])
        if int(postData['rating'])<1:
            print "In validation4 "
            results['status'] = False
            results['errors'].append("Please Provide a Rating")

        if results['status']:
            user1 = User.objects.get(id = sessiondata['id'])
            print "Next is Book Id"
            print sessiondata['bookid']
            book1 = Book.objects.get(id=sessiondata['bookid'])
            #author1=Author.objects.create(authorname=postData['new_author'],bookauthor = book1)
            review1=Review.objects.create(reviewcontent=postData['review'],bookrating= postData['rating'],bookreview = book1,userreview=user1)
 
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results





class Book(models.Model):
    booktitle = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userbook = models.ForeignKey('app_reglogin.User', related_name="userbooks")
    objects=bookManager()
    #bookauthors
    #bookreviews

class Author(models.Model):
    authorname = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    bookauthor = models.ForeignKey(Book, related_name="bookauthors")
    objects=bookManager()

class Review(models.Model):
    reviewcontent = models.TextField(max_length=1000)
    bookrating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    bookreview = models.ForeignKey(Book, related_name="bookreviews")
    userreview = models.ForeignKey('app_reglogin.User', related_name="userreviews")
    objects=bookManager()


 
    

