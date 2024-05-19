#..............Fuad Garibli................
#..............Yazılım Testi Ödevi 2.......
#..............G201210558..................
#..............view kodları...........

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse

def add_blog_article(request):
    return render(request, 'add_blog_article.html')

def index(request):
    return render(request, 'index.html')

def addindustry(request):
    return render(request, 'addindustry.html')

def blog_single_post(request):
    return render(request, 'blog-single-post.html')

def blog(request):
    return render(request, 'blog.html')

def industries_single_industry(request):
    return render(request, 'industries-single-industry.html')

def industries(request):
    return render(request, 'industries.html')

def blog(request):
    blog_articles = request.session.get('blog_articles', [])
    return render(request, 'blog.html', {'blog_articles': blog_articles})

def submit_blog_article(request):
    if request.method == 'POST':
        blog_title = request.POST.get('blogTitle')
        blog_content = request.POST.get('blogContent')
        blog_image = request.POST.get('blogImage')
        blog_link = request.POST.get('blogLink')
        new_blog_article = {
            'title': blog_title,
            'content': blog_content,
            'image': blog_image,
            'link': blog_link,
        }
        blog_articles = request.session.get('blog_articles', [])
        blog_articles.append(new_blog_article)
        request.session['blog_articles'] = blog_articles
        return redirect('blog')
    else:
        return redirect('add_blog_article')

def add_blog_article(request):
    return render(request, 'add_blog_article.html')

def submitindustry(request):
    if request.method == 'POST':
        service_title = request.POST.get('serviceTitle')
        service_description = request.POST.get('serviceDescription')
        service_image = request.POST.get('serviceImage')
        service_link = request.POST.get('serviceLink')
        
        new_article = {
            'title': service_title,
            'description': service_description,
            'image': service_image,
            'link': service_link,
        }
        
        articles = request.session.get('articles', [])
        articles.append(new_article)
        
        request.session['articles'] = articles
        
        return redirect('industries')
    else:
        return HttpResponse('Invalid request method')
    
def industries(request):
    articles = request.session.get('articles', [])
    return render(request, 'industries.html', {'articles': articles})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already taken.')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful.')
    return redirect('index')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('index')
    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('index')