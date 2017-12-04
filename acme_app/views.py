# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm, ContactForm
from models import SignUpModel, SessionModel, ContactModel
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import MySQLdb
import sys
import csv

# Create your views here.
dbServer = '127.0.0.1'
dbPass = ''
dbSchema = 'electric_info'
dbUser = 'root'


def home_view(request):
    date = datetime.now()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pin = form.cleaned_data['pin']
            device = form.cleaned_data['device']
            email = form.cleaned_data['email']
            phno = form.cleaned_data['phno']
            # city = form.cleaned_data['city']
            query = form.cleaned_data['query']

            # saving data to DB
            user = ContactModel(name=name, pin=pin, phno=phno, email=email, query=query, device=device)
            user.save()
            dbQuery = 'SELECT *FROM electric_info.acme_app_contactmodel;'

            # db = .connect(host=dbServer, user=dbUser, passwd=dbPass)
            # cur = db.cursor()
            # cur.execute(dbQuery)
            # result = cur.fetchall()

            # c = csv.writer(open("temp.csv", "wb"))
            # c.writerow(result)
            # return render(request, 'contact.html')
            # # using sendgrid
            # subject = "Successfully Signed Up!"
            # body = "Thank you for Signing Up"
            # code = send_mail(email, subject, body)
            # if code == 202:
            #     mail_status = "Account has been created successfully and mail has been sent to your email-id"
            # else:
            #     mail_status = "There is some problem in sending a mail"
            # # returning user ro success page that you have successfully signup to the app
            # return render(request, 'success.html', {'response': mail_status})
        else:
            print "INVALID FORM ENTRIES"
            # ctypes.windll.user32.MessageBoxW(0, u"Invalid form entries.Enter again", u"Error", 0)
            form = ContactForm()
    else:
        form = ContactForm()
    # returning to signup page if method is not post or there is no data in form or payload is empty
    return render(request, 'index.html', {'form': form}, {'Date': date})


# signup view to display at the time of signup
def signup_view(request):
    date = datetime.now()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if len(username) > 4 and len(password) > 5:
                # saving data to DB
                user = SignUpModel(name=name, username=username, email=email, password=make_password(password))
                user.save()

                # using sendgrid
                # subject = "Successfully Signed Up!"
                # body = "Thank you for Signing Up"
                # code = send_mail(email, subject, body)
                # if code == 202:
                #     mail_status = "Account has been created successfully and mail has been sent to your email-id"
                # else:
                #     mail_status = "There is some problem in sending a mail"
                # returning user ro success page that you have successfully signup to the app
                # return render(request, 'success.html', {'response': mail_status})
            else:
                print 'Invalid username/password'
                # ctypes.windll.user32.MessageBoxW(0, u"Invalid username/password. please try again", u"Error", 0)
                form = SignUpForm()
        else:
            print "INVALID FROM ENTRIES"
            # ctypes.windll.user32.MessageBoxW(0, u"Invalid form entries.Enter again", u"Error", 0)
            form = SignUpForm()
    else:
        form = SignUpForm()
    # returning to signup page if method is not post or there is no data in form or payload is empty
    return render(request, 'signup.html', {'form': form}, {'Date': date})


# login view to display at the time of login or sign in
def login_view(request):
    date = datetime.now()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = SignUpModel.objects.filter(username=username).first()
            if user:
                # check for the password
                if check_password(password, user.password):
                    token = SessionModel(user=user)
                    token.create_token()
                    token.save()
                    response = redirect('/L_services/')
                    response.set_cookie(key='session_token', value=token.session_token)
                    return response
                else:
                    print("Incorrect Username or Password")
                    # ctypes.windll.user32.MessageBoxW(0, u"Incorrect Username or Password", u"Error", 0)
                    return render(request, 'login.html', {'invalid': True})
            else:
                print ("User does not exist")
                # ctypes.windll.user32.MessageBoxW(0, u"User does not exist.Please sign up", u"Error", 0)
                return render(request, 'index.html', {'invalid': True})
        else:
            print ("Error: Invalid form")
            # ctypes.windll.user32.MessageBoxW(0, u"Invalid form entries.Enter again", u"Error", 0)
            form = SignUpForm()
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form}, {'Date': date})


def check_validation(request):
    if request.COOKIES.get('session_token'):
        session_auth = SessionModel.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session_auth:
            logged_in_time = session_auth.created_on + timedelta(days=1)
            if logged_in_time > timezone.now():
                return session_auth.user
            else:
                return None
        else:
            return None


def contact_view(request):
    return render(request, 'contact.html')


def services_view(request):
    return render(request, 'services.html')


def amc_view(request):
    return render(request, 'amc.html')


def about_view(request):
    return render(request, 'about.html')
