from django.conf.urls.static import static
from django.urls import path, include
from .import views

urlpatterns = [
  path('create/',views.createVIEW, name='Cpost'),
  path('<int:id>/details/',views.detailsVIEW, name='details'),
  path('historypost/', views.WhistoryVIEW, name='history'),
  path('<int:pk>/delete/', views.DeleteVIEW.as_view(), name='delete'), 
]