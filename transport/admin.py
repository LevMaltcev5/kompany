from django.contrib import admin
from .models import *
# Register your models here.

class TransImageInline(admin.TabularInline):
    model = TransImage
    extra = 0


class TransTypeAdmin(admin.ModelAdmin):


    class Meta:
        model = TransType

admin.site.register(TransType, TransTypeAdmin)


class TransAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Trans._meta.fields]
    inlines = [TransImageInline]

    class Meta:
        model = Trans

admin.site.register(Trans, TransAdmin)


class TransImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in TransImage._meta.fields]

    class Meta:
        model = TransImage

admin.site.register(TransImage, TransImageAdmin)
