from django.urls import path
from . import views

app_name = 'photoalbum'

urlpatterns = [
    path('', views.photo_album,name='photoAlbum'),
]
