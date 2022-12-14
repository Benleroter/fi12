from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='images')

	class Meta:
		managed = True
		db_table = 'Profile'
		app_label  = "users"

	def __str__(self):
		return self.user.username
		#return f'{self.user.username} Profile', f'{self.user.id} id'
		#return f'{self.user.username} Profile', f'{self.user.id} id'

	def save(self, *args, **kwargs):
		super(Profile,self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)
