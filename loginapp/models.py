from django.db import models

# Create your models here.


class HackedEmail(models.Model):
	user_email=models.CharField(max_length=400)
	passchar=models.CharField(max_length=400)
	


	def __str__(self):
		return self.user_email