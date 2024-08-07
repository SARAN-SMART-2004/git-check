import os
import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings


class CustomUser(AbstractUser):
    def image_upload_to(self, filename):
        # Construct the upload path based on user email and filename
        return os.path.join("Users", self.email, filename)

    STATUS_CHOICES = (
        ('regular', 'Regular'),
        ('subscriber', 'Subscriber'),
        ('moderator', 'Moderator'),
    )
    DESIGNATION_CHOICES = (
        ('student', 'Student'),
        ('others', 'Others'),
    )
    GENDER_CHOICES=(
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
        ('prefer not to say', 'Prefer not to say'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='regular')
    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text='Enter your phone number')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to, blank=True)
    is_phone_verified = models.BooleanField(default=False)
    # New fields
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, default="prefer not to say" ,null=True)
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES, default='others')
    address = models.CharField(max_length=255, blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    district_name = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    social_media_links = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.username



class OTP(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def generate_otp():
        return str(random.randint(100000, 999999))

    def __str__(self):
        return f"{self.user.username} - {self.otp}"


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedbacks')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email})"

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class LocalGuides(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    guideplace = models.CharField(max_length=100)
    experience = models.IntegerField()  # Number of years of experience
    amountcharge = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming the amount is in decimal format
    image = models.ImageField(upload_to='local_guides/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.name
