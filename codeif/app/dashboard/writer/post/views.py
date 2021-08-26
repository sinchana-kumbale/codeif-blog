from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import post
from .forms import CpostFORMS, UpostFORMS
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

#sys.path.append('../writer') # Adding writer to the system path to import its models.
from .. import models as mo #importing the writer models.


# =======================================Create your post logic (here)==================-==============================    Images =request.FILES['Images']       Category=request.POST['CategoryF']
def createVIEW(request):
  if request.method == 'POST':
    form = CpostFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = post(User_Name = request.user,Title=request.POST['TitleF'],Details = request.POST['DetailsF'],Category=request.POST['CategoryF'])
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
  details = authorDetails(request.user)
  return render(request, 'whistory.html', {'Hposts' : Hposts,'followers':details[0],'isValidated':details[1]})

#To return the number of followers and their verified status 
def authorDetails(user):
  print(user)
  print(mo.writerDetails.objects.all())
  follower  = None
  is_validated = None
  try:
    writer_Details = mo.writerDetails.objects.filter(User_Name = user)
    if (writer_Details):
      follower = writer_Details[0].follower
      is_validated = writer_Details[0].isValidated
      print(writer_Details)
  except mo.writerDetails.DoesNotExist:
    follower  = None
    is_validated = None
  return (follower,is_validated)

def likeVIEW(request, pk):
  each_post = get_object_or_404(post, id=request.POST.get('post_id'))
  liked = False
  if each_post.likes.filter(id=request.user.id).exists():
    each_post.likes.remove(request.user)
    liked = False 
  else:
    each_post.likes.add(request.user)  
    liked = True 
  return HttpResponseRedirect(reverse('details', args=[str(pk)]))
  

'''def likeVIEW(request, id):
  user = request.user
  if request.method == 'POST':
    post_id = request.POST.get('post_id')
    post_obj = Instruction.objects.get(id=post_id)

    if user in post_obj.Likes_M.all():
      post_obj.Likes_M.remove(user)
      post_obj.Liked_int_M = post_obj.Liked_int_M - 1
      post_obj.save()

    else:
      post_obj.Likes_M.add(user)
      local_VAR_like_status=True
      post_obj.Liked_int_M = post_obj.Liked_int_M + 1
      post_obj.save()
  #not using now
  return HttpResponseRedirect(reverse('details', args=[str(id)]))'''
  

