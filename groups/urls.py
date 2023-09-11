from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
    path('create_groups',views.create_group,name='create_groups'),
    path('show_groups',views.show_group,name='show_groups'),
]
