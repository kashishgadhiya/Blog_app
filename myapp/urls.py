from .import views
from django.urls import path
urlpatterns = [
    
    # path('',views.index,name='index'),
    
    path('',views.blog_list,name='blog_list'),
    
    path('create/',views.blog_create,name='blog_create'),
    
    path('<int:blog_id>/edit/',views.blog_edit,name='blog_edit'),
    
    path('<int:blog_id>/delete/',views.blog_delete,name='blog_delete'),
    path('register/',views.register, name='register'),
    # path('login/',views.login_request, name='login'),
    
]
