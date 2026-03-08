"""Views for lettings domain."""

import logging

from django.shortcuts import get_object_or_404, render

from .models import Letting

logger = logging.getLogger(__name__)


def lettings_index(request):
    """Render all available lettings."""
    lettings_list = Letting.objects.all()
    logger.info('Lettings index requested (%s records)', lettings_list.count())
    return render(
        request,
        'lettings_index.html',
        {'lettings_list': lettings_list},
    )


def letting(request, letting_id):
    """Render one letting details page."""
    letting_obj = get_object_or_404(Letting, id=letting_id)
    logger.info('Letting detail requested (id=%s)', letting_id)
    context = {'title': letting_obj.title, 'address': letting_obj.address}
    return render(request, 'letting.html', context)
