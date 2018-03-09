from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.http import HttpResponse

from .models import Post, UploadFile
from .forms import PostForm, UploadFileForm, UserForm, LoginForm

# Create your views here.

def file_list(request):
	posts = UploadFile.objects.filter(upload_date__lte=timezone.now()).order_by('-upload_date')
	return render(request, 'blog/file_list.html', {'posts': posts})

def file_new(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.upload_date = timezone.now()
			post.save()
			return redirect('file_list')
	else:
		form = UploadFileForm()
	return render(request, 'blog/post_edit.html', {'form': form})


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new2(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(request, new_user)
			return redirect('post_list')
	else:
		form = UserForm()
		return render(request, 'blog/add_user.html', {'form': form})

def signin(request):
	if request.method == "POST":			
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('post_list')
		else:
			print('로그인 실패, 다시 시도해보세요.')
			return HttpResponse('로그인 실패, 다시 시도해보세요.')
	else:
		form = LoginForm()
		return render(request, 'blog/login.html', {'form': form})






