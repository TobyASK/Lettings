"""Project-level views."""

import logging

import sentry_sdk
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Render the homepage."""
    logger.info('Homepage requested')
    return render(request, 'index.html')


def custom_404(request, exception):
    """Render custom 404 page."""
    logger.warning('404 error on path %s', request.path)
    if request.path.rstrip('/') == '/sentry-debug':
        sentry_sdk.capture_message('Sentry debug fallback hit from 404 handler')
        raise RuntimeError('Sentry debug fallback triggered from custom 404 handler')
    return render(request, '404.html', status=404)


def custom_500(request):
    """Render custom 500 page."""
    logger.exception('500 error triggered for path %s', request.path)
    return render(request, '500.html', status=500)


def sentry_debug(request):
    """Raise an exception to test Sentry integration."""
    logger.error('Sentry debug route called')
    sentry_sdk.capture_message('Sentry debug route called')
    raise RuntimeError('Sentry test exception from /sentry-debug/')
