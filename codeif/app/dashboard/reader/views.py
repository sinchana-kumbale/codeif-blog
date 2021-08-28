from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import readerDetails
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponseRedirect
from app.dashboard.writer import models as mo

def followWriter(request, id):
  print("hello")
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
  return HttpResponseRedirect(reverse('test'))
  