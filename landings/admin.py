from django.contrib import admin
from .models import *
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name","fam","status"]
    class Meta:
        model = MyClient

admin.site.register(MyClient, SubscriberAdmin)
# admin.site.register(MyClient, SubscriberAdmin)
