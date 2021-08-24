from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
  path('writer/', include('app.dashboard.writer.urls')),
  path('reader/', include('app.dashboard.reader.urls')),
]