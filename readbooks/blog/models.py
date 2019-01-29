from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	slug = models.SlugField(unique=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
    
	def __str__(self):
		return self.title
    
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('posts-home')

	def save(self, *args, **kwargs):
		if not self.slug:
			original = slugify(self.title)
			new_slug = original
			numb = 2
			while Post.objects.filter(slug=new_slug).exists():
				new_slug = '%s-%d'%(original, numb)
				numb += 1
			self.slug = new_slug
		super(Post, self).save(*args, **kwargs)
    	
class Comment(models.Model):
	name = models.CharField(max_length=60)
	text = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.text
		
	def __unicode__(self):
		return self.text
