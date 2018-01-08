 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt, re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALIAS_REGEX = re.compile(r'^\w+$')

class UserManager(models.Manager):
    def login(self, postData):

        failed_authentication = False
        messages = []

        try:
            found_user = User.objects.get(email=postData['email'])
        except:
            found_user = False

        if len (postData['email']) < 1 or len(postData['password']) < 1 :
            messages.append("All fields required.")
            failed_authentication = True

        elif not found_user:
            messages.append("No user found with this username. Please register new user.")
            failed_authentication = True

        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}

        if len(postData['password']) < 8:
            messages.append("Password must be at least 8 characters")
            return {'result':"failed_authentication", 'messages':messages}

        hashed_password = bcrypt.hashpw(str(postData['password']), str(found_user.salt))

        if found_user.password != hashed_password:
            messages.append("Incorrect password! Please try again")
            failed_authentication = True

        if failed_authentication:
            return {'result':"failed_authentication", 'messages':messages}
        else:
            messages.append('Successfully logged in!')
            return {'result':'success', 'messages':messages, 'user':found_user}
            

    def register(self, postData):

        failed_validation = False
        messages = []
     
        if len (postData['name']) < 1 or len (postData['alias']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1:
            messages.append("All fields required.")
            failed_validation = True

        try:
            found_user = User.objects.get(email=postData['email'])
        except:
            found_user = False

        if len(postData['email']) < 1:
            messages.append("Email is required!")
            failed_validation = True

        elif not EMAIL_REGEX.match(postData['email']):
            messages.append("Please enter a valid email!")
            failed_validation = True

        elif found_user:
            messages.append("This email is already registered!")
            failed_validation = True

        elif len(postData['password']) < 8:
            messages.append("Password must be at least 8 characters")
            failed_validation = True

        elif postData['confirm_password'] != postData['password']:
            messages.append("Passwords must match. Try again.")
            failed_validation = True

        if failed_validation:
            return {'result':"failed_validation", 'messages':messages}

        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(str(postData['password']), str(salt))

        User.objects.create(name=postData['name'], alias=postData['alias'], email= postData['email'], password=hashed_password, salt=salt)

        user = User.objects.get(email=postData['email'])
 
        return {'result':"Successfully registered new user", 'messages':messages, 'user':user}


    def show_user(self, user_id):


        user = User.objects.get(id = user_id)

        return {'user' : user}




class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __repr__(self):
        return "<User: name: {}, alias: {}, email: {}".format(self.name, self.alias, self.email)


class Comment(models.Model):
    topic = models.CharField(max_length=45)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name= "added_by")
    likes = models.ManyToManyField(User, related_name = "liked_by")

    def __repr__(self):
        return "<Comment: topic: {}, message: {}, created_by: {}".format(self.topic, self.message, self.created_by)


