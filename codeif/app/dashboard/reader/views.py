from app.user.models import CustomUser
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import readerDetails, Followers
from django.conf import settings
#from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponseRedirect, request
from app.dashboard.writer import models as mo
#from django.contrib.auth.models import CustomUser
from app.user.models import CustomUser as User
'''def followWriter(request, pk):
  user = request.user
  if request.method == 'POST':
    Writer_Name = request.POST.get(id = id)
    # writer_object = readerDetails.objects.get(User_Name = user)
    writer_object = readerDetails.objects.filter(User_Name = user)
    print("hello")
    # print(type(writer_object))
    # print(writer_object)
    # print(writer_object)
    if Writer_Name in writer_object.followingList:
      writer_object.followingList.remove(Writer_Name)
      writer_object.followings = writer_object.followings - 1
      writer_object.save()
      mo.writerDetails.followerList.remove(user)
      mo.writerDetails.follower = mo.follower - 1
      mo.writerDetails.save()

    else:
      writer_object.followingList.add(Writer_Name)
      writer_object.followings = writer_object.followings + 1
      writer_object.save()
      mo.writerDetails.followerList.add(user)
      mo.writerDetails.follower = mo.follower + 1
      mo.writerDetails.save()
  return HttpResponseRedirect(reverse('test'))'''


def follow_user(request, user_name):
    other_user = User.objects.get(email=user_name)
    session_user = request.user
    get_user = User.objects.get(email=session_user)
    session_following, create = Followers.objects.get_or_create(
        user=session_user)
    following, create = Followers.objects.get_or_create(user=session_user.id)
    check_user_followers = Followers.objects.filter(another_user=get_user)
    check_follower = Followers.objects.get(user=get_user.id)

    is_followed = False
    if session_following.another_user.filter(name=user_name).exists() or following.another_user.filter(name=user_name).exists():
        is_followed = True
    else:
        is_followed = False
    param = {'user_obj': get_user, 'followers': check_user_followers,
             'following': following, 'is_followed': is_followed}
    is_followed = False
    if other_user.name != session_user:
        if check_follower.another_user.filter(name=other_user).exists():
            add_usr = Followers.objects.get(user=get_user)
            add_usr.another_user.remove(other_user)
            is_followed = False
            return HttpResponseRedirect(reverse('test'))
        else:
            add_usr = Followers.objects.get(user=get_user)
            add_usr.another_user.add(other_user)
            is_followed = True
            return HttpResponseRedirect(reverse('test'))

        return HttpResponseRedirect(reverse('test'))
    else:
        return HttpResponseRedirect(reverse('test'))


def reader_dashboard(request):

    # reader = CustomUser.objects.filter(Category='reader')
    user = CustomUser.objects.all()

    context = {
        'user': user,
    }

    return render(request, 'index.html', context)
