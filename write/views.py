from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import hw
from django.core import serializers

import json as simplejson
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import addImg

@login_required(login_url='/home/LogIn/')
def Home(r):
    f=addImg()
    return render(r,'home1.html',{'f':f})
    #return HttpResponse("wakeup wakeup wakeup its a brand new day")
    
@login_required(login_url='/home/LogIn/')
def AddHandWriting(r):
    return render(r,'addHandWriting.html')
    
def SignUp(r):
    return render(r,'signup.html')
    #return HttpResponse("gcgudgcudgvh")
    
def SignUpSave(r):
    fn=r.POST.get("fn")
    sn=r.POST.get("sn")
    e=r.POST.get("e")
    pwd=r.POST.get("pwd")
    u=r.POST.get("e")
    #create_user(username, email=None, password=None, **extra_fields)
    t=User.objects.create_user(u,e,pwd)
    t.first_name=fn
    t.last_name=sn
    t.save()
    al=hw.objects.create(uid=t)
    return HttpResponseRedirect("/home/LogIn/")

def LogIn(r):
    if r.method=="POST":
        e=r.POST.get("e")
        pwd=r.POST.get("pwd")
        u=authenticate(username=e,password=pwd)
        if u is not None:
            auth_login(r,u)
            r.session['e']=e
            print("logged in")
            return JsonResponse({"l":"valid"})
        else:
            print("failed login")
            return JsonResponse({"l":"invalid"})
            
    return render(r,'login.html')

def AddLetter(r):
    em=r.session['e']
    print(em)
    u=User.objects.get(username=em)
    img=r.POST.get("img")
    alpha=['sa','sb','sc','sd','se','sf','sg','sh','si','sj','sk','sl','sm','sn','so','sp','sq','sr','ss','st','su','sv','sw','sx','sy','sz','ba','bb','bc','bd','be','bf','bg','bh','bi','bj','bk','bl','bm','bn','bo','bp','bq','br','bs','bt','bu','bv','bw','bx','by','bz']
    c=int(r.POST.get("count"))
    p=alpha[c-1]
    hwo=hw.objects.get(uid=u)
    setattr(hwo,p,img)
    hwo.save()
    return JsonResponse({'d':'success'})

def addImgr(r):
    f=addImg(r.POST,r.FILES)
    em=r.session['e']
    u=User.objects.get(username=em)
    hwo=hw.objects.get(uid=u)
    if f.is_valid():
        
        ns=hw(simg=f.cleaned_data['simg'])
        print(ns)
        hwo.simg=hw(simg=f.cleaned_data['simg'])
        hwo.save()
        #f.save()
    return HttpResponseRedirect('/home/')

def Convert(r):
    em=r.session['e']
    txt=r.POST.get('txt')
    u=User.objects.get(username=em)
    hwo=hw.objects.filter(uid=u)
    hwojson=simplejson.dumps(list(hw.objects.filter(uid=u).values()))
    #n = json.dumps(m)
    o = simplejson.loads(hwojson)
    #hwojson = serializers.serialize("json", hwo)
    #data = {"SomeModel_json": SomeModel_json}
    return JsonResponse(o,safe=False)
    #return JsonResponse(o,safe=False)
    #return render(r,'output.html')
    #return render(r,'output.html',d)
    
def ConvertToText(r):
    txt="hello"
    #l=r.POST.get("len")
    #f=r.post.get("files")
    #for i in range(0,l):
     #   print(f[i])
    return render({'txt':txt})

def Output(r):
    #print(d)
    global d
    t=d
    em=r.session['e']
    u=User.objects.get(username=em)
    hwo=hw.objects.get(uid=u)
    return render(r,'output.html',{'hwo':hwo})

def LogOut(r):
    del r.session['e']
    auth_logout(r)
    return render(r,'login.html')