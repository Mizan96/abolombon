from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     url(r'^$',views.IndexView.as_view(),name='index'),
     url(r'^logIn/$',views.LogInView.as_view(),name='logIn'),
     url(r'^signUp/$',views.SignUpView.as_view(),name='signUp'),
     url(r'^contact/$',views.ContactView.as_view(),name='contact'),
     url(r'^aboutUs/$',views.AboutUsView.as_view(),name='aboutUs'),
     url(r'^(?P<pk>[1-9]+)/$',views.ProductDetailView.as_view(),name='productDetail'),
]
