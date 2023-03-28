from django.urls import path
from .views import *

# app_name = "ytproject"

urlpatterns = [
    path("", index, name="home"),
    path('download/', download, name='download'),
    path('download/<itag>/', yt_download_done, name='download_done'),
]
