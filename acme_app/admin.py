# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import ContactModel, SignUpModel, SessionModel

# Register your models here.

admin.site.register(SignUpModel)
admin.site.register(SessionModel)
admin.site.register(ContactModel)
