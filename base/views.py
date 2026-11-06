from django.shortcuts import render


def home_view(reqest):
    return render(reqest, 'site_page/index.html')

def about_view(reqest):
    return render(reqest, 'site_page/about.html')

def contact_veiw(reqest):
    return render(reqest, 'site_page/contact.html')
