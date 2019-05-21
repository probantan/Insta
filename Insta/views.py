from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Image, Profile
from .forms import ProfileForm, PostForm,CommentForm
from django.db import transaction

# Create your views here.

@login_required(login_url='/accounts/login/')
def search (request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET.get("query")
        user = Profile.search_profiles(query)
        images = Image.objects.all()
        message = f"query"

        collection = {
            "message": message,
            "got": user,
            "images": images,
        }

        return render(request, 'search.html', collection)
    else:
        message = "No Username Searched"
        return render(request,'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def rest (request, pk):
    profile = Profile.objects.get(pk=pk)
    images = Image.objects.all().filter(creator_id=pk)
    collection = {
        "profile": profile,
        'images': images,
    }
    return render(request, 'rest.html', collection)
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    image = Image.objects.all()
    collection = {

        "current_user": current_user,
        "image": image,
    }
    return render(request, 'home.html', collection)
 

@login_required(login_url='/accounts/login/')
def all(request):
    all_pics = Image.objects.all()
    collection={         
          "all_pics":all_pics
    }
    
    return render(request, 'all.html', collection)
@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    profile =get_object_or_404(Profile)
    post_form= PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES )
        if form.is_valid():
            post = form.save()
            post.creator = current_user
            post.profile = profile
            post.save()
            return redirect('home')
    return render(request, 'post.html', locals())
# @login_required(login_url='/accounts/login/')
# def post(request):
#     current_user = request.user
#     profiles = Profile.objects.all()
#     form = PostForm()

#     for profile in profiles:
#         if profile.user.id == current_user.id:
#             if request.method == 'POST':
#                 form = PostForm(request.POST, request.FILES)
#                 if form.is_valid():
#                     post = form.save(commit=False)
#                     post.creator = current_user
#                     post.profile = profile
#                     post.save()
#                     return redirect('home')
#             else:
#                 form = PostForm()
#                 content = {
#                     "post_form": form,
#                 }
#     return render(request, 'post.html', content)        
def comment(request, pk):
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
    test = 'Profile route Working'
    current_user = request.user
    images = Image.objects.filter(creator=request.user)
    profiles = Profile.objects.filter(user=request.user)
    content = {
        "test": test,
        "current_user": current_user,
        "images": images,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)



@login_required(login_url='/accounts/login')
def updateprofile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('profile')

	else:
			form = ProfileForm()
	return render(request, 'updateprofile.html',{"form":form })
# @login_required(login_url='/accounts/login/')
# def updateprofile(request):
#     if request.method == 'POST':
#         current_user= request.user
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             edit = form.save(commit=False)
#             # edit.user = current_user
#             edit.save()
#             return redirect('edit_profile')
#     else:
#         form = ProfileForm()
#     return render(request, 'updateprofile.html', {'form':form})
 

@login_required(login_url='/accounts/login/')
def like(request, operation, pk):
    post  = get_object_or_404(Image, pk=pk)
    if operation == 'like':
        post.likes = post.likes +1
        post.save()
    return redirect('home')

