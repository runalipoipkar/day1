from django.urls import path
from . import views


urlpatterns=[
    path('ao/',views.order_view,name='addorder_url'),
    path('sv/',views.show_view,name='show_url'),
    path('up/<int:pk>',views.update_view,name='update_url'),
    path('dl<int:pk>',views.delete_view,name='delete_url')
]