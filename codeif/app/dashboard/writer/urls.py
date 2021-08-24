from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
  path('post/',include('app.dashboard.writer.post.urls')),
]