from django.shortcuts import render
from app.dashboard.writer.post.models import post

# Create your views here.
def testVIEW(request):
  return render(request, 'test.html')

def indexVIEW(request):
  posts = post.objects.all().order_by('-id')
  return render(request, 'index.html', {'posts' : posts})