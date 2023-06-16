from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=25)
    task = models.TextField('Option, comments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'