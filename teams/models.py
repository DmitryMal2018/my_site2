from django.contrib.auth.models import User
from django.db import models
#python manage.py makemigrationsfrom django.urls import reverse


class Team(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Название команды', 
        help_text='введите название команды')
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Удаленные пользователи',
        help_text='укажите исключенных пользователей',
        related_name="teams")
    
    class Meta:
        verbose_name_plural = 'Команды'
        verbose_name = 'Команда'
        ordering = ['name']

    def __str__(self):
        return self.name
    
#    def get_absolute_url(self):
#        return reverse('team', kwargs={'team_id':self.pk})
from django.contrib.auth.models import User
from django.db import models
#python manage.py makemigrationsfrom django.urls import reverse


class Team(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Название команды', 
        help_text='введите название команды')
    username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Удаленные пользователи',
        help_text='укажите исключенных пользователей',
        related_name="teams")
    
    class Meta:
        verbose_name_plural = 'Команды'
        verbose_name = 'Команда'
        ordering = ['name']

    def __str__(self):
        return self.name
    
#    def get_absolute_url(self):
#        return reverse('team', kwargs={'team_id':self.pk})