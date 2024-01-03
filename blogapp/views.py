from django.shortcuts import render,HttpResponse ,redirect

# Create your views here.
from .models import Post , categories
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
def index(request):
    posts=Post.objects.all()
    cats=categories.objects.all()
    data={
        'posts': posts,
        'cats': cats
    }
    # print(posts)
    return render(request,'home.html',data)

def post(request,url):
    posturl=Post.objects.get(url=url)
    cats=categories.objects.all()
    data={
        'posturl': posturl,
        'cats': cats
    }
    print(posturl)
    return render(request,'posts.html',data)



def category(request,url):
    cats=categories.objects.get(url=url)
    posts=Post.objects.filter(cat=cats)
   
    data={
        'posts': posts,
        'cats': cats,
    }
    return render(request,'category.html',data)


def registration_page(request):
    if request.method == 'POST':
        uname=request.POST['username']
        uemail=request.POST['useremail']
        upassword1=request.POST['userpassword1']
        upassword2=request.POST['userpassword2']
        if(upassword1!=upassword2):
            return HttpResponse("password and confirm password not same!!")
        my_user=User.objects.create_user(uname,uemail,upassword1)
        return redirect('/admin')
    return render(request, 'registration_page.html') 

