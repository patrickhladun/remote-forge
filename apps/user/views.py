from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Talent
from .forms import TalentProfileForm

def talent_view(request, id):
    """View function for talent single page."""
    talent = get_object_or_404(Talent, id=id)
    return render(request, "user/talent.html", {"talent": talent})


def talents_view(request):
    """View function for talents list."""
    talents = Talent.objects.all()
    return render(request, 'user/talents.html', {'talents': talents})


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("login")  # Ensure the user is authenticated

    if request.method == "POST":
        if request.user.user_type == "talent":
            talent = get_object_or_404(Talent, user=request.user)
            form = TalentProfileForm(request.POST, request.FILES, instance=talent)
            template_name = "user/admin/talent_profile.html"
        else:
            return redirect("error")

        if form.is_valid():
            form.save()
            return redirect("profile")  # Redirect to a success page
    else:
        if request.user.user_type == "talent":
            talent = get_object_or_404(Talent, user=request.user)
            form = TalentProfileForm(instance=talent)
            template_name = "user/admin/talent_profile.html"
        else:
            return redirect("error")  # Redirect or handle the error

    return render(request, template_name, {"form": form})


def account_view(request):
    return render(request, 'user/admin/account.html')