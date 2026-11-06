from django.shortcuts import render

# Create your views here.
def blog_veiw(req):
    return render(req,'blog_page/blog_home.html')

def blog_single_veiw(req):
    return render(req,'blog_page/blog_single.html')
