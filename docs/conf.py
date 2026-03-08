"""Sphinx configuration for OC Lettings."""

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

import django  # noqa: E402

django.setup()

project = 'OC Lettings'
copyright = '2026, OC Lettings'
author = 'OC Lettings Team'
release = '2.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
