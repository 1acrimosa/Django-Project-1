from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Task(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Task, related_name='items', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
