from django.shortcuts import render

def home_view(reqest):
    return render(reqest,'base_page/index.html')


def about_view(reqest):
    return render(reqest,'base_page/about.html')
