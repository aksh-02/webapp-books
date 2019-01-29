from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image

# Create your models here.
class Genre(models.Model):
	GENRE_CHOICES = (('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Mystery', 'Mystery'), 
	('Romance', 'Romance'), ('Biography', 'Biography'), ('Autobiography', 'Autobiography'), 
	('Sci-Fi', 'Sci-Fi'), ('History', 'History'), ('Children', 'Children'), ('Fiction', 'Fiction'), 
	('Drama', 'Drama'), ('Poetry', 'Poetry'), ('Mythology', 'Mythology'))

	name = models.CharField(max_length=100, choices=GENRE_CHOICES, unique=True)

	def __str__(self):
		return self.name
	
	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=60)
	author = models.CharField(max_length=30)
	description = models.TextField(null=True, blank=True)
	genre = models.ManyToManyField(Genre)
	price = models.FloatField()
	seller = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	slug = models.SlugField(unique=True)
	image = models.ImageField(default='default_book.jpeg', upload_to='book_pics')

	def __str__(self):
		return f'{self.name} by {self.author}'

	def __unicode__(self):
		return f'{self.name} by {self.author}'

	def save(self, *args, **kwargs):
		if not self.slug:
			original = slugify(self.name)
			new_slug = original
			numb = 2
			while Product.objects.filter(slug=new_slug).exists():
				new_slug = '%s-%d'%(original, numb)
				numb += 1
			self.slug = new_slug

		super(Product, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		output_size = (250, 400)
		img.thumbnail(output_size)
		img.save(self.image.path)
