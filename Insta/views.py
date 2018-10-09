from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Image, Profile
from .forms import ProfileForm, PostForm,CommentForm
from django.db import transaction

# Create your views here.


@login_required(login_url='/accounts/login/')
def search_result(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET.get("query")
        user = Profile.search_profiles(query)
        images = Image.objects.all()
        message = f"query"

        content = {
            "message": message,
            "found": user,
            "images": images,
        }

        return render(request, 'search.html', content)
    else:
        message = "You haven't searched for anyone"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def follow(request, operation, pk):
    """
    To implement this adding friends using many to many relationship will try
    friend = Friend.follow(operation, pk)
    where operation maybe to add or remove a friend.
    the follow() does the tie of current user to friend instance. From here it
    it would mean displaying the Friend.objects.all() to the where would
    display friends
    """

    return redirect('home')



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
    image = Image.objects.all()
    profiles = Profile.objects.all()
    user = Profile.objects.get(user=current_user)
    print(user)
    content = {

        "current_user": current_user,
        "user": user,
        "image": image,
        "profiles": profiles
    }
    return render(request, 'home.html', content)
 

@login_required(login_url='/accounts/login/')
def all(request):
    all_pics = Image.objects.all()
    content = {
        'all_pics': all_pics,
    }
    return render(request, 'all.html', content)


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
    comment='comment.objects.all()'
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



@login_required(login_url='/accounts/login/')
@transaction.atomic
def add_profile(request):
    current_user = request.user
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

@login_required(login_url='/accounts/login/')
def like(request, operation, pk):
    current_user = request.user
    post = post = get_object_or_404(Image, pk=pk)

    if operation == 'like':
        post.likes = post.likes + 1
        post.save()
    elif operation == 'unlike':
        post.likes = post.likes - 1
        post.save()
    return redirect('home') 
