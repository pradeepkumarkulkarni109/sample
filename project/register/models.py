# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.core.validators import RegexValidator
from django.db import models
from rest_framework.utils import json

class Signup(models.Model):

    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$',
                                 message="Phone number entered in the format:'+919999999999'. Up to 14 digits number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    password = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return self.email+ "|" +str(self.id)

    def get_data(self):
        return json.loads(self.data)

class Document(models.Model):
        user = models.OneToOneField(Signup, on_delete=models.CASCADE)
        document = models.FileField(upload_to='images')
