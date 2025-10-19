from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def register(request):
    template=loader.get_template("register.html")
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
    return render(request, 'register.html', {'form': form})
