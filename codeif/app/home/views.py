from django.shortcuts import render
from app.dashboard.writer.post.models import post
from app.dashboard.writer.models import writerDetails
from app.dashboard.writer.post import views as vw
# Create your views here.
# def testVIEW(request):
#   print(request.user)
#   print(request.user.Category)
#   if (request.user.Category == 'Writer' and not(writerDetails.objects.filter(User_Name = request.user))):
#   	writer = writerDetails(User_Name = request.user,follower = 0,isValidated =False)
#   	writer.save()
#   details = vw.authorDetails(request.user)
#   return render(request, 'test.html',{'followers':details[0],'isValidated':details[1]})
  

# def indexVIEW(request):
#   posts = post.objects.all().order_by('-id')
#   print(posts[0])
#   #print(posts[0][:])
#   details_list = []
#   for i in posts:
#   	#for eachPost in posts:
#   	details = vw.authorDetails(i.User_Name)
#   	details_list.append({'followers':details[0],'isValidated':details[1]})
#   required_list = zip(posts,details_list)
#   return render(request, 'index.html', {'list':required_list})

def indexVIEW(request):
  # print(request.user)
  # print(request.user.Category)
  if (request.user.Category == 'Writer' and not(writerDetails.objects.filter(User_Name = request.user))):
  	writer = writerDetails(User_Name = request.user,follower = 0,isValidated =False)
  	writer.save()
  details = vw.authorDetails(request.user)
  return render(request, 'dashboard.html',{'followers':details[0],'isValidated':details[1]})
# testVIEW
# indexVIEW

def testVIEW(request):
  posts = post.objects.all().order_by('-id')
  print(posts[0])
  #print(posts[0][:])
  details_list = []
  for i in posts:
  	#for eachPost in posts:
  	details = vw.authorDetails(i.User_Name)
  	details_list.append({'followers':details[0],'isValidated':details[1]})
  required_list = zip(posts,details_list)
  return render(request, 'index.html', {'list':required_list})