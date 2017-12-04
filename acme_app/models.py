# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid4


# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=240)
    device = models.CharField(max_length=240)
    pin = models.CharField(max_length=240, null=False, blank=False)
    phno = models.BigIntegerField(null=False, blank=False)
    query = models.TextField(max_length=255, null=False, blank=False)


class SignUpModel(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=120, unique=True, null=False, blank=False)
    password = models.TextField(max_length=40, null=False, blank=False)


class SessionModel(models.Model):
    user = models.ForeignKey(SignUpModel)
    session_token = models.CharField(max_length=255)
    is_valid = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid4()

