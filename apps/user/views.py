from django.shortcuts import render, get_object_or_404
from .models import Talent

def talent(request):
    """View function for talent list."""
    talents = Talent.objects.all()
    return render(request, 'user/talent.html', {'talents': talents})


def talent_profile(request, id):
    """View function for talent."""
    talent_obj = get_object_or_404(Talent, id=id)
    return render(request, 'user/talent-profile.html', {'talent': talent_obj})