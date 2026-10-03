from django.contrib import admin
from .models import CustomUser
from base.models import BaseModel
# Register your models here.
admin.site.register(CustomUser)
