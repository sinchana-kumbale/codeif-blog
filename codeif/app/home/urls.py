from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
  path('', views.testVIEW, name='test')
]