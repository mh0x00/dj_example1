from django import template
from blog.models import Post,Category
register = template.Library()


@register.inclusion_tag('blog_page/inclusion/popular_blog.html')
def lastpost():
    posts=Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog_page/inclusion/blog_categories.html')
def categories():
    posts=Post.objects.filter(status=1)
    category=Category.objects.all()
    cat_dict={}
    for name in category:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categor":cat_dict}