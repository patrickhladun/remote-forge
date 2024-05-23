from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Talent, Employer
from .forms import AccountProfile, TalentProfileForm, EmployerProfileForm

def talent_view(request, id):
    """View function for talent single page."""
    talent = get_object_or_404(Talent, id=id)
    return render(request, "user/talent.html", {"talent": talent})


def talents_view(request):
    """View function for talents list."""
    talents = Talent.objects.all()
    return render(request, 'user/talents.html', {'talents': talents})

@login_required
def profile_view(request):
    if request.user.user_type == "talent":
        profile = get_object_or_404(Talent, user=request.user)
        form_class = TalentProfileForm
    elif request.user.user_type == "employer":
        profile = get_object_or_404(Employer, user=request.user)
        form_class = EmployerProfileForm
    else:
        return redirect("error")  # Redirect or handle the error

    if request.method == "POST":
        form = form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = form_class(instance=profile)

    return render(request, 'user/admin/profile.html', {"form": form})

@login_required
def account_view(request):
    if request.method == "POST":
        form = AccountProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account updated successfully.")
            return redirect("account")
    else:
        form = AccountProfile(instance=request.user)
    return render(request, 'user/admin/account.html', {"form": form})