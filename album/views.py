from django.shortcuts import render
from .models import Album
# Create your views here.


# photo album views

def photo_album(request):
    photo_album = Album.objects.all()
    context = {
        'photo_album':photo_album
    }

    return render(request,'album/index.html',context)