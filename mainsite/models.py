import datetime
from django.db import models
from django.utils import timezone
import uuid


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class AmazonPriceTracking(models.Model):
    # url, name, current price, preferred price, created_at,contact_method, email, phone, expired_at
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=750)
    name = models.CharField(max_length=500)
    current_price = models.DecimalField(decimal_places=2, max_digits=5)
    tracking_price = models.DecimalField(
        decimal_places=2, max_digits=5, null=True)
    expired_date = models.DateField()
    contact_method = models.CharField(max_length=25)
    email = models.CharField(max_length=150, null=True)
    phone = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

