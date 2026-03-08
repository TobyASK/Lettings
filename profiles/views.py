"""Views for profiles domain."""

import logging

from django.shortcuts import get_object_or_404, render

from .models import Profile

logger = logging.getLogger(__name__)


def profiles_index(request):
    """Render all profiles."""
    profiles_list = Profile.objects.all()
    logger.info('Profiles index requested (%s records)', profiles_list.count())
    return render(
        request,
        'profiles_index.html',
        {'profiles_list': profiles_list},
    )


def profile(request, username):
    """Render one profile details page."""
    profile_obj = get_object_or_404(Profile, user__username=username)
    logger.info('Profile detail requested (username=%s)', username)
    return render(request, 'profile.html', {'profile': profile_obj})
