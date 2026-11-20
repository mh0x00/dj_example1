from django.urls import path
from blog.views import blog_single_view, blog_veiw,test_view

app_name = 'blog'

urlpatterns = [
    path('', blog_veiw, name='blog'),
    path('<int:pid>', blog_single_view, name='blog_single'),
    path('test', test_view, name='test')
]
