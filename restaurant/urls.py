from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [path("", views.index)] + debug_toolbar_urls()
