from django.contrib import admin

from .models import Question, AmazonPriceTracking

admin.site.register(Question)
admin.site.register(AmazonPriceTracking)