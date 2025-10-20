from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.template import loader
from .forms import UserProfileForm

def register(request):
    if  request.method !='POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            #log the user in
            login(request,new_user)
            return HttpResponse("Done")
    context={'form':form}
    return render(request,'register.html',context)

def edit_user_profile(requeast):
    if requeast.method=='POST':
        form=UserProfileForm(requeast.POST, requeast.FILES ,
                             instance=requeast.user.profile)#files bec we allowed users add files.
        if form.is_valid():
            form.save()
            return HttpResponse('profile was updated !!')
    else:
        form=UserProfileForm(instance=requeast.user.profile)
    return render(requeast,'edit_profile.html',{'form':form})