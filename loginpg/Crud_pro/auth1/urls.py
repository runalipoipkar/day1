from django.urls import path
from . import views


urlpatterns=[
    path('spv/',views.sign_view,name='signup_url'),
    path('log/',views.login_view,name='loginPage_url'),
    path('lot/',views.logout_view,name='logout_url')
]