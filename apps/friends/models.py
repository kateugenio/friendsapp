from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
TIME_REGEX = re.compile(r'^\d{1,2}\:\d{1,2}$')

# Create your models here.
class UserManager(models.Manager):
	def validateRegis(self, **kwargs):
		errors = []
		if len(kwargs['name']) < 1:
			errors.append('Name cannot be empty')
		if len(kwargs['alias']) < 1:
			errors.append('Alias cannot be empty')
		if len(kwargs['email']) < 1:
			errors.append('Email cannot be empty')
		if not EMAIL_REGEX.match(kwargs['email']):
			errors.append("Email address is invalid, please try again")
		if len(kwargs['password']) < 1:
			errors.append("Must fill in password")
		if len(kwargs['password']) < 8:
			errors.append("Password must be more than 8 characters")
		if kwargs['password'] != kwargs['confirmPW']:
			errors.append("Password and Password Confirmation do not match")
		if len(kwargs['dob']) < 1:
			errors.append("Must enter Date of Birth")
		if len(errors) > 0:
			return (False, errors)
		else:
			password = kwargs['password']
			password = password.encode()
			pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
			dob = datetime.datetime.strptime(kwargs['dob'], '%m/%d/%Y').strftime('%Y-%m-%d')
			user = User.userMgr.create(name=kwargs['name'], alias=kwargs['alias'], email=kwargs['email'], pw_hash=pw_hash, dob=dob)
			return (True, user)

	def validateLogin(self, **kwargs):
		try:
			user = self.get(email=kwargs['login_email'])
			password = kwargs['login_pw'].encode()
			if bcrypt.hashpw(password, user.pw_hash.encode()) == user.pw_hash.encode():
				return (True, user)
		except ObjectDoesNotExist:
			pass
		return (False, ["Email/password don't match"])


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=45)
	email = models.EmailField(max_length=255)
	pw_hash = models.CharField(max_length=255)
	dob = models.DateField(auto_now=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userMgr = UserManager()

class Friend(models.Model):
	user = models.ForeignKey(User, related_name="myself")
	user2 = models.ForeignKey(User, related_name="myfriend")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)