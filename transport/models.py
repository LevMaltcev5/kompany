from django.db import models

class TransType(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" %  self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Trans(models.Model):
    name = models.CharField(max_length=126, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(TransType, blank=True, null=True, default=None)

    def __str__(self):
        return "%s, %s" % (self.category, self.name)

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

class TransImage(models.Model):
    transport = models.ForeignKey(Trans, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='trans_images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
