from apps.user.models import Talent, Employer

def site_data(request):
    profile = None

    if request.user.is_authenticated:
        profile = {'image': None}

        try:
            talent_profile = Talent.objects.get(user=request.user)
            profile['image'] = talent_profile.image
        except Talent.DoesNotExist:
            try:
                employer_profile = Employer.objects.get(user=request.user)
                profile['image'] = employer_profile.image
            except Employer.DoesNotExist:
                profile['image'] = None

    data = {
        'site_name': 'Remote Forge',
        'profile': profile
    }
    
    return data
