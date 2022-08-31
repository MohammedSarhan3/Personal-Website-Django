from django.urls import path
from .views import all_posts , post_detail
app_name= 'blog'
urlpatterns ={

    path ('',all_posts),
    path('<int:id>',post_detail)

}