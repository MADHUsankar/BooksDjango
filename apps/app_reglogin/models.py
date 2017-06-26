# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
    def register(self, postData):
        print "in def1"
        results = {'status': True, 'errors': [],'user':None}
        if not postData['first_name'] or len(postData['first_name']) <3:
            print "fname error"
            results['status'] = False
            results['errors'].append("Please enter valid first name")
        if not postData['last_name'] or len(postData['last_name']) <3:
            results['status'] = False
            results['errors'].append("Please enter valid last name")
        if not postData['emailid']:
            results['status'] = False
            results['errors'].append("Please enter valid emailid")
        if not postData['password'] or len(postData['password']) <4:
            results['status'] = False
            results['errors'].append("Password must be atleat 4 characters long")
        if postData['reenterpassword'] != postData['password']:
            results['status'] = False
            results['errors'].append("Passwords do not match")
        x = User.objects.filter(emailid = postData['emailid'])
        try:
            if x[0]:
                results['errors'].append("It already exists")
                results['status'] = False
        except:
            if results['status']:
                password = postData['password'].encode() # to get from unicode to string
                hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                print hashed
                y = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], emailid=postData['emailid'], password=hashed)
                y.save()
                results['user'] = y
        return results

    def loginval(self, postData):
        results = {'status': True, 'errors': [],'user':None}


        if not postData['emailid']:
            results['status'] = False
            results['errors'].append("Please enter valid emailid")
        print "asdfghjkl"
        if not postData['password'] or len(postData['password']) <4:
            results['status'] = False
            results['errors'].append("Password must be atleat 4 characters long")
        
        
        if results['status'] == True:
            x = User.objects.filter(emailid = postData['emailid'])
        #print x
        
            try:
                if x[0]:
                    print "in################# "
                    print x[0].password
                    password = postData['password'].encode()
                    y = x[0].password.encode()
                    if bcrypt.hashpw(password,y) == y:
                        results['status'] = True
                        print ("*****It matches**********")
                        results['user'] = x[0]
                    else:
                        results['status'] =False
                        results['errors'].append("Invalid credentials")
 
            except:
                results['status'] =False
                print "please regitser"
                results['errors'].append("Please Register")
        return results

        


class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    emailid = models.CharField(max_length=78)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    #userreviews