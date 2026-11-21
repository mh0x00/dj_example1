from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.models import Post

# Create your views here.


def blog_veiw(req,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=posts.filter(author__username=kwargs['author_username'])

    posts=Paginator(posts,3)
    try:    
        page_number=req.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context = {'posts': posts}
    return render(req, 'blog_page/blog_home.html', context)


def blog_single_view(req, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(req, 'blog_page/blog_single.html', context)

def blog_search(req):
    posts = Post.objects.filter(status=1)
    if req.method == 'GET':
        if s:=req.GET.get('s'):
            posts=posts.filter(Q(content__icontains=s) | Q(title__icontains=s))
    context = {'posts': posts}
    return render(req, 'blog_page/blog_home.html', context)

    
def test_view(req):
    return render(req,'test.html')