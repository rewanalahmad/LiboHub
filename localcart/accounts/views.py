from django.shortcuts import render,redirect
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
            return redirect('home:homepage')
    context={'form':form}
<<<<<<< HEAD
    return render(request,'registration/register.html', {'form': form})
=======
    return render(request,'registration/register.html',context)

def edit_user_profile(request):
    if request.method=='POST':
        form=UserProfileForm(request.POST, request.FILES ,
                             instance=request.user.profile)#files bec we allowed users add files.
        if form.is_valid():
            form.save()
            return redirect('home:homepage')
    else:
        form=UserProfileForm(instance=request.user.profile)
    return render(request,'edit_profile.html',{'form':form})
>>>>>>> f4e912e73ed49082647d3d58388c96a9434f55a9
