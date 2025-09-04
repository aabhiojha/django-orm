from django.shortcuts import render

from restaurant.models import Restaurant
from .forms import RatingForm


# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return render(request, "index.html", context)
