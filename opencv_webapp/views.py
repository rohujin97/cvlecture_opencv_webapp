from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UploadImageForm
from .forms import ImageUploadForm
from django.conf import settings
from .opencv_dobj import opencv_dobj
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import RequestContext

from django.core.files.storage import FileSystemStorage

from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from django.conf import settings
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login


def signup(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('opencv_webapp/signup.html')
        else:
            form = UserForm()
            return render(request, 'opencv_webapp/signup.html',{'form':form})

def signin(request):
    return render(request, 'opencv_webapp/signin.html',{})

def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {})

def uimage(request):
  if request.method == 'POST':
      form = UploadImageForm(request.POST, request.FILES)
      if form.is_valid():
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'opencv_webapp/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
  else:
      form = UploadImageForm()
      return render(request, 'opencv_webapp/uimage.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('first_view')
        return render(request, 'opencv_webapp/dobj.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'opencv_webapp/dobj.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('second_view')
        else:
            return HttpResponse('Login Failed')
    else:
        form = LoginForm()
        return render(request, 'opencv_webapp/signin.html', {'form':form})


def dobj(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            wordlist = opencv_dobj(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'opencv_webapp/dobj.html', {'form':form, 'post':post,'wordlist':wordlist})
            #return render(request, 'opencv_webapp/voca.html', {'form': form, 'post': post, 'wordlist': list(wordlist) })
    else:
        form = ImageUploadForm()
    return render(request, 'opencv_webapp/dobj.html', {'form': form})

def voca(request):
    wordlist=[]
    return render(request, 'opencv_webapp/voca.html', {'list':wordlist})

def second_view(request):
    return render(request, 'opencv_webapp/second_view.html', {})