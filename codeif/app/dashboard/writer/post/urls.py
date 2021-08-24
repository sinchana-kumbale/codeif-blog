from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
  path('create/',views.createVIEW, name='Cpost'),
  path('historypost/', views.WhistoryVIEW, name='history')
]