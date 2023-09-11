from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns=[
    path('news_post',views.news_post,name='news_post'),
    path('create_post',views.create_post,name='create_post'),
    path('update_post/<int:postid>/',views.update_post,name='update_post'),
    path('delete_post/<int:postid>/',views.post_delete_form,name='delete_post'),
    path('my_post',views.my_post,name='my_post'),
]