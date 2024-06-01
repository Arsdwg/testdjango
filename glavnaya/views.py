from django.shortcuts import render

from django.shortcuts import render
from .models import Motto, YouTubeVideo, Gadget

def home(request):
    motto = Motto.objects.first()
    video = YouTubeVideo.objects.first()
    popular_gadgets = Gadget.objects.order_by('-popularity')[:5]
    context = {
        'motto': motto,
        'video': video,
        'popular_gadgets': popular_gadgets
    }
    return render(request, 'home.html', context)
