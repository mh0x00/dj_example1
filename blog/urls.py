from django.urls import path
from blog.views import blog_single_view, blog_veiw,test_view,blog_search

app_name = 'blog'

urlpatterns = [
    path('', blog_veiw, name='blog'),
    path('<int:pid>', blog_single_view, name='blog_single'),
    path('category/<str:cat_name>', blog_veiw, name='category'),
    path('author/<str:author_username>', blog_veiw, name='author'),
    path('search/', blog_search, name='search'),
    path('test', test_view, name='test'),
]
