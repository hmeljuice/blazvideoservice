from django.shortcuts import render
from .models import Video
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required
def index(request):
    """View function for home page"""
    videos = Video.objects.filter(lender=request.user)

    context = {
        'videos': videos,
    }

    return render(request, 'index.html', context)

