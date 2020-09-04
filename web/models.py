from django.db import models
from multiselectfield import MultiSelectField
from django.template.defaultfilters import slugify
from datetime import date

# Create your models here.

MY_CHOICES = ((1, 'Bed Rooms'),
               (2, 'Bath Rooms'),
               (3, 'Luggage'),
               (4, 'Garage'),
               (5, 'Water'),
               (6, 'Stories'),
               (7, 'Roofing'),)

CAT1 = ((1, 'Jobs'),)
CAT2 = ((3, 'Coffe'),)
CAT3 = ((3, 'Travel'),)

class House(models.Model):
	title = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	description = models.TextField()
	Image = models.ImageField(default='default.jpg', upload_to='images/')
	Price = models.FloatField(default = 1.0)
	Price_per_month = models.FloatField(default = 1.0)
	Bed_Amount = models.IntegerField(default = 1)
	Bathub_Amount = models.IntegerField(default = 1)
	Floor_plan_or_Height = models.IntegerField(default = 1)
	posted_at = models.DateTimeField(auto_now_add = True)
	features = MultiSelectField(choices=MY_CHOICES)
	url = models.SlugField(max_length=500, unique=True, blank="Do not touch this")

	def save(self, *args, **kwargs):
		self.url= slugify(self.title)
		super(House, self).save(*args, **kwargs)


	def __str__(self):
		return self.title

class Blog(models.Model):
	title = models.CharField(max_length = 200)
	description = models.CharField(max_length = 500)
	Image = models.ImageField(default='default.jpg', upload_to='posts/')
	tag1 = MultiSelectField(choices=CAT1)
	tag2 = MultiSelectField(choices=CAT2)
	tag3 = MultiSelectField(choices=CAT3)
	posted = models.DateTimeField(auto_now_add = True)
	content = models.TextField(default="Contents")
	url = models.SlugField(max_length=500, unique=True, blank="Do not touch this")

	def save(self, *args, **kwargs):
		self.url= slugify(self.title)
		super(Blog, self).save(*args, **kwargs)

	def __str__(self):
		return self.title	

class Requests(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	Thoughts = models.TextField(default="")
	house = models.CharField(default="", max_length = 200)

	def __str__(self):
		return self.first_name + " " + self.last_name


