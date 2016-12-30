from django.shortcuts import render
from .models import Userdata, UserHash
from uuid import uuid1
from django.http import HttpResponse
# from sendsms import api
from sendsms.message import SmsMessage


def index(request):
    if request.method == "POST":
        mobileNo = request.POST['mobileNo']
        name = request.POST['username']
        user = Userdata()
        user.mobile = mobileNo
        user.name = name
        user.save()

        userhash = UserHash()
        userhash.user = user
        userhash.hashValue = uuid1().hex
        userhash.save()

        data = "Hello '"+name+"'\nYour URL is : "+request.build_absolute_uri()+userhash.hashValue
        abc = SmsMessage(body=data, from_phone=user.mobile, to=['+41791234567'])
        abc.send()
        print(data)
        print(abc)
        return HttpResponse('Successfully sent')
    else:
        return render(request, 'sendMessage/index.html')


def message(request, uuid):
    userhash = UserHash.objects.get(hashValue=uuid)
    return HttpResponse("Welcome - "+userhash.user.name)
