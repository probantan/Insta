from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Image, Profile
from .forms import ProfileForm, PostForm,CommentForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def others(request, pk):
    profile = Profile.objects.get(pk=pk)
    images = Image.objects.all().filter(creator_id=pk)
    content = {
        "profile": profile,
        'images': images,
    }
    return render(request, 'other.html', content)

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    form=LoginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=LoginForm()
    return render(request,'home.html',{"form":form})  



@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.creator = current_user
                    post.profile = profile
                    post.save()
                    return redirect('home')
            else:
                form = PostForm()
                content = {
                    "post_form": form,
                    "user": current_user
                }
    return render(request, 'post.html', content)

@login_required(login_url='/accounts/login/')
def comment(request, pk):
    test = 'Working'
    post = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = current_user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    content = {
        "test": test,
        "comment_form": form,
    }
    return render(request, 'comment.html', content)

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(creator=request.user)
    profiles = Profile.objects.filter(user=request.user)
    content = {
        "current_user": current_user,
        "images": images,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)

@login_required(login_url='accounts/login/')
def add_profile( request):
    current_user=request_user
    user_profile = Profile.objects.filter(user_id=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = current_user
            user_profile.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user)

        content = {
            "form": form,
        }
        return render(request, 'profiles/prof-edit.html', content)
