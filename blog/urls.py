from django.urls import path
from blog.views import blog_single_veiw, blog_veiw

app_name = 'blog'

urlpatterns = [
    path('', blog_veiw, name='blog'),
    path('blog_single', blog_single_veiw, name='blog_single')
]
