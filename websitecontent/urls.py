from django.urls import path, include
from .import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('blogPage/', views.blogPage, name='nameBlogsPage'),
    path('aboutPage/', views.aboutPage, name='nameAboutPage'),
    path('<int:id>/', views.detailBlogPage, name='nameDetailBlogPage'),
    path('crawl/', views.crawl, name='nameCrawl'),
    path('article/<str:post_name>/', views.article_detail, name='nameArticleDetail'),
    path('addBlogs/', views.AddBlogs.as_view(), name='nameAddBlogs'),
]
