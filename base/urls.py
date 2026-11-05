from django.urls import path
from .views import home_view, about_view,contact_veiw

app_name='base'

urlpatterns = [
    path('',home_view,name='home'),
    path('about',about_view,name='about'),
    path('contact',contact_veiw,name='contact')
]
