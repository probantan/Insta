from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    form=LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=LoginForm()
    return render(request,'home.html',{"form":form})    
