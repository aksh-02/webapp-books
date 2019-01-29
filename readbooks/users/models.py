from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.validators import RegexValidator


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
	about = models.TextField(blank=True, null=True, default="Not Mentioned")
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits only")
	employment = models.CharField(max_length=100, blank=True, default="Not Mentioned")
	hobbies = models.TextField(blank=True, null=True, default="Not Mentioned")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, default="Not Mentioned")
	lives_in = models.CharField(max_length=100, blank=True, default="Not Mentioned")
	from_place = models.CharField(max_length=100, blank=True, default="Not Mentioned")
	shipping_address = models.TextField(blank=True, null=True, default="Not Mentioned")

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
