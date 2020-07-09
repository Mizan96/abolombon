from django.db import models

class Product_Cat(models.Model):
	name = models.CharField( max_length = 254 )
	image = models.FileField()

	def __str__(self):
		return self.name

class Product_List(models.Model):
	cat = models.ForeignKey( Product_Cat, on_delete = models.CASCADE)
	name = models.CharField( max_length = 254 )
	price = models.IntegerField()
	stock = models.IntegerField()
	image = models.ImageField(upload_to='catagory', blank=True)

	def __str__(self):
		return self.name+' - '+self.price+' - '+self.stock

class Upcoming_Product(models.Model):
	cat = models.ForeignKey( Product_Cat, on_delete = models.CASCADE)
	name = name = models.CharField( max_length = 254 )
	price = models.IntegerField()
	arrival_date = models.CharField( max_length = 254 )

	def __str__(self):
		return self.name+' - '+self.price+' - '+self.arrival_date

class Product_Comment(models.Model):
	name = models.ForeignKey( Product_List, on_delete = models.CASCADE )
	email = models.EmailField( max_length = 254 )
	text = models.TextField()

	def __str__(self):
		return self.email+' - '+self.text


class Tutorial_Cat(models.Model):
	name = models.CharField( max_length = 254 )

	def __str__(self):
		return self.name

class Tutorial(models.Model):
	cat = models.ForeignKey(Tutorial_Cat, on_delete = models.CASCADE )
	name = models.CharField( max_length = 254 )
	email = models.EmailField( max_length = 254 )
	date = models.DateField( auto_now=False, auto_now_add=False )
	file = models.FileField()

	def __str__(self):
		return self.name+' - '+self.email+' - '+self.date+' - '

class Tutorial_Comment(models.Model):
	name = models.ForeignKey( Tutorial, on_delete = models.CASCADE )
	email = models.EmailField( max_length = 254 )
	text = models.TextField()

	def __str__(self):
		return self.email+' - '+self.text

class User_Info(models.Model):
	first_name = models.CharField( max_length = 254 )
	last_name = models.CharField( max_length = 254 )
	user_name = models.CharField( max_length = 254 )
	email = models.EmailField(max_length = 254 )
	password = models.CharField(max_length = 20 )
	location = models.CharField( max_length = 254 )
	mobile_no = models.CharField(max_length = 11)

	def __str__(self):
		return self.first_name+' - '+self.last_name+' - '+' - '+self.user_name+' - '+self.email+' - '+self.password+' - '+self.location+' - '+self.mobile_no
