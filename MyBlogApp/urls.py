from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="BlogHome"),
    path('blogpost/<int:my_id>', views.blogpost, name="blogpost")

]

