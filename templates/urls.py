#..............Fuad Garibli................
#..............Yazılım Testi Ödevi 2.......
#..............G201210558..................
#..............path kodları...........

from django.contrib import admin
from django.urls import path
from .views import index, blog_single_post, blog, add_blog_article, industries_single_industry,submit_blog_article, submitindustry, industries, addindustry, register, user_login, user_logout

urlpatterns = [
    path('', index, name='index'),
    path('submit_blog_article/', submit_blog_article, name='submit_blog_article'),
    path('add_blog_article/', add_blog_article, name='add_blog_article'),
    path('addindustry/', addindustry, name='addindustry'),
    path('submit_blog_article/', submit_blog_article, name='submit_blog_article'),
    path('addindustry/submit/',submitindustry, name='submitindustry'),
    path('index/', index, name='index'),
    path('blog-single-post/', blog_single_post, name='blog_single_post'),
    path('blog/', blog, name='blog'),
    path('industries-single-industry/', industries_single_industry, name='industries_single_industry'),
    path('industries/', industries, name='industries'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
