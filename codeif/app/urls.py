from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
  path('user/',include('app.user.urls')),
  path('',include('app.home.urls')),
  path('dashboard/',include('app.dashboard.writer.urls')),
]