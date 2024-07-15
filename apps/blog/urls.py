from django.urls import path
from apps.blog.views import BloglistView, BlogCreateView

app_name='blogs'

urlpatterns =[
    path('', BloglistView.as_view(), name='bloglist'),
    path('create/', BlogCreateView.as_view(), name='create_blog')

]