from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Course(models.Model):
	code = models.CharField(max_length = 255)
	section = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)
	semester = models.CharField(max_length = 255)
	seats = models.CharField(max_length = 255)
	instructor = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#	date_created = models.DateTimeField(auto_now_add=True)
#	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}" .format(self.name)

class Interest(models.Model):
	owner = models.ForeignKey('auth.User', related_name = 'interests', on_delete = models.CASCADE)
	course = models.ForeignKey('Course', related_name = 'interests', on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#	date_created = models.DateTimeField(auto_now_add=True)
#	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.id)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

