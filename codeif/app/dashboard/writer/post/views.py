from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import post
from .forms import CpostFORMS, UpostFORMS
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

# =======================================Create your post logic (here)==================-==============================    Images =request.FILES['Images']       Category=request.POST['CategoryF']
def createVIEW(request):
  if request.method == 'POST':
    form = CpostFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = post(User_Name = request.user,Title=request.POST['TitleF'],Details = request.POST['DetailsF'],)
      new_req.save()
      return HttpResponseRedirect(reverse('test'))

  else:
    form = CpostFORMS()
  
  context = {'form': form}
  return render(request,'createPost.html', context)



# =======================================Details post logic (here)======================================================

def detailsVIEW(request, id):           
  content = post.objects.filter(id=id)
  #views logic...
  blog_post = post.objects.get(id=id) 
  blog_post.views = blog_post.views + 1
  blog_post.Users_views.add(request.user)
  blog_post.save()   
  return render(request,'details.html', {'content': content})



# =======================================Delete post logic (here)=======================================================

class DeleteVIEW(DeleteView):
  model = post
  template_name = 'delete.html'
  context_object_name = 'object'
  success_url = reverse_lazy('index')


# =======================================History post logic (here)=======================================================
'''
def updateVIEW(request, pk):
  postinfo = post.objects.get(id=pk)
  form = UpostFORMS(instance = postinfo)

  if request.method == 'POST':
    form = UpostFORMS(request.POST, instance = postinfo)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('test'))

  else:
    form = UpostFORMS()
  return render(request, 'update.html', {'form' : form})'''


class updateVIEW(UpdateView):
  model = post
  template_name = 'update.html'
  #form_class = UpostFORMS
  fields = ['Title','Details']
  success_url = reverse_lazy('index')


# =======================================History post logic (here)=======================================================

def WhistoryVIEW(request):
  Hposts = post.objects.all().filter(User_Name=request.user)
  return render(request, 'whistory.html', {'Hposts' : Hposts})