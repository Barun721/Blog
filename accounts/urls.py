from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.registration,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout')
]