from django.conf.urls.static import static
from django.urls import path, include
from .import views
from app.dashboard.reader import views as vr

urlpatterns = [
  path('create/',views.createVIEW, name='Cpost'),
  path('historypost/', views.WhistoryVIEW, name='history'),
  path('<int:id>/details/',views.detailsVIEW, name='details'),
  path('<int:pk>/update/', views.updateVIEW.as_view(), name='update'),  
  path('<int:pk>/delete/', views.DeleteVIEW.as_view(), name='delete'), 
  path('like/<int:id>', views.likeVIEW, name='like'), 
  path('follow/<int:id>',vr.followWriter,name = 'follow'),
  path('followerList/', views.FollowerList, name='followerList'),
]