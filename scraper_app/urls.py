from django.urls import path
from scraper_app import views

urlpatterns = [
	path('', views.index, name="index"),
]
