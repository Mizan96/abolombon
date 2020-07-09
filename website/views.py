from django.views import generic
from .models import *

class IndexView(generic.ListView):
	template_name = 'website/index.html'
	context_object_name = 'productCat'

	def get_queryset(self):
		return Product_Cat.objects.all()

class LogInView(generic.ListView):
	template_name = 'website/logIn.html'


	def get_queryset(self):
		return Product_Cat.objects.all()


class SignUpView(generic.ListView):
	template_name = 'website/signUp.html'


	def get_queryset(self):
		return Product_Cat.objects.all()



class ProductDetailView(generic.DetailView):
	template_name = 'website/productDetail.html'
	context_object_name = 'productCat'

	def get_queryset(self):
		return Product_Cat.objects.all()

class AboutUsView(generic.ListView):
	template_name = 'website/aboutUs.html'

	def get_queryset(self):
		return Product_Cat.objects.all()

class ContactView(generic.ListView):
	template_name = 'website/contact.html'

	def get_queryset(self):
		return Product_Cat.objects.all()
