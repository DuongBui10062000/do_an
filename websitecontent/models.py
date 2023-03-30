from django.db import models
from profiles.models import User

# Create your models here.
class Blogs(models.Model):
	name = models.CharField(max_length = 1000)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	description = models.TextField(max_length=300)
	postcontent = models.TextField(null=True)
	topictype = models.CharField(max_length=100)
	contact = models.CharField(max_length=1000, null=True)
	date_post = models.DateTimeField(auto_now_add=True, null=True)
	picture = models.ImageField(upload_to='blog_pictures')

	def __str__(self):
		return self.name