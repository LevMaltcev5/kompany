from django.db import models

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class MyClient(models.Model):
    name = models.CharField(max_length=20, blank=False)
    fam = models.CharField(max_length=40, blank=False)
    fath = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=True, null=True, default=None)
    interested = models.CharField(max_length=256, blank=False)
    day = models.CharField(max_length=30, blank=True, null=True, default=None)
    time = models.CharField(max_length=40,blank=True, null=True, default=None)
    phone = models.CharField(max_length=30,blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)

    def __str__(self):
        return "Пользователь %s %s %s " % (self.name, self.fam, self.fath,)
    class Meta:
        verbose_name  = "Клиент"
        verbose_name_plural = "Клиенты"
