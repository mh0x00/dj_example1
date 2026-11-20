from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.


def blog_veiw(req):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(req, 'blog_page/blog_home.html', context)


def blog_single_view(req, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(req, 'blog_page/blog_single.html', context)



def test_view(req):
    return render(req,'test.html')