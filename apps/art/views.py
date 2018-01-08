from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
from django.db.models import Count
from collections import Counter
from django.http import HttpResponseRedirect



def index(request):
    context = {
        'messages':get_messages(request)
    }
    return render(request, 'index.html', context)

def process_login(request):
    if request.method == "POST":

        post_data = {
            'email':request.POST['email'],
            'password':request.POST['password']
        }
        
    login_result = User.objects.login(post_data)
    print login_result

    if login_result['result'] == "failed_authentication":
        print "login result returned failed authentication"
        if 'messages' in login_result.keys():
            for message in login_result['messages']:
                messages.info(request, message)
        return redirect('/')
    else:
        if 'user' in login_result.keys():
            request.session['current_user'] = login_result['user'].id
            if 'messages' in login_result.keys():
                for message in login_result['messages']:
                    messages.success(request, message)
        else:
            messages.info(request, "Something went wrong")
            return redirect('/')

        return redirect('/home')


def process_registration(request):
    request.session['email'] = request.POST['email']
    if request.method == "POST":

        post_data = {
            'name':request.POST['name'],
            'alias':request.POST['alias'],
            'email':request.POST['email'],
            'password':request.POST['password'],
            'confirm_password':request.POST['confirm_password'] 
        }
        
        register_result = User.objects.register(post_data)
        print register_result

        if register_result['result'] == "failed_validation":
            if 'messages' in register_result.keys():
                for message in register_result['messages']:
                    messages.warning(request, message)
            return redirect('/')
        else:
            if 'user' in register_result.keys():
                request.session['current_user'] = register_result['user'].id
                if 'messages' in register_result.keys():
                    for message in register_result['messages']:
                        messages.success(request, message)
            else:
                messages.warning(request, "Something went wrong")
                return redirect('/')
            return redirect('/home')

    return redirect('/')

def home(request):    
    user_id = User.objects.get(pk=request.session['current_user']).id  
    this_user = User.objects.get(id=request.session['current_user'])
    users = User.objects.filter(id = user_id)

    count = Comment.objects.count()

    comments = Comment.objects.all().order_by('-created_at')[:3]

    your_comments = Comment.objects.filter(id = user_id)|Comment.objects.filter(likes=this_user)
    
    context = {
        "users" : users,
        "comments" : comments,
        "count" : count,
        "your_comments" : your_comments
    
    }

    return render(request, "home.html", context)

def process_add(request):
    if request.method == "POST":
        error = False

        if len(request.POST['topic']) < 1 or len(request.POST['message']) < 1 :
            messages.error(request, "All fields required.")
            error = True

        if error:
                messages.error(request, "")
                return redirect('/home')

        else:
            user_id = User.objects.get(pk=request.session['current_user']).id 
            creator = User.objects.get(pk=request.session['current_user'])
            
            new_comment = Comment.objects.create(topic= request.POST['topic'], message= request.POST['message'], created_by = creator )

            creator_name = new_comment.created_by.name 

        
            return redirect('/home')

def logout(request):
    user_id = User.objects.get(pk=request.session['current_user']).id 

    del user_id
  
    return redirect('/')

def delete_comment(request, comment_id):


    the_comment= Comment.objects.get(id=comment_id)

    the_comment.delete()

    return redirect('/home')

def show(request, created_by):

    print created_by

    creator_name = created_by

    return redirect('/show_creator/' + creator_name)



def show_creator(request, created_by):
    
    print created_by

    creator_name = created_by
    print creator_name

    try: 
        user = User.objects.get(alias = creator_name)
        comments = Comment.objects.filter(created_by = user)

        count = comments.count()

        context = {
            "comments" : comments,
            "count" : count,
            "user" : user
        }


    except:
        pass 
        print("no match")


    return render(request, "ok.html", context)


def like_comment(request, comment_id):
    
    this_user = User.objects.get(id=request.session['current_user'])

    print this_user

    the_comment= Comment.objects.get(id=comment_id)

    the_comment.likes.add(this_user)

    return redirect('/home')

def remove_comment(request, comment_id):

    this_user = User.objects.get(id=request.session['current_user'])

    print comment_id

    the_comment= Comment.objects.get(id=comment_id)

    the_comment.likes.clear()

    return redirect('/home')

def user_profile(request, user_id):


    user = User.objects.get(id=user_id)

    comments = Comment.objects.all().filter(created_by= user)

    count = comments.count()

    context = {
        "user" : user,
        "comments" : comments,
        "count" : count
    }

    return render(request, "profile.html", context)


def back(request):

    return redirect('/home')


def aboutme(request):

    return render(request, "aboutme.html")

def portfolio(request):

    return render(request, "portfolio.html")

def home1(request):

    return redirect('/')






