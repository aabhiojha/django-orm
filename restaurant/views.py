from django.shortcuts import render

from restaurant.models import Rating, Restaurant
from .forms import RatingForm
from django.db.models.functions import Lower
from django.db.models import Sum


def index(request):
    restaurants = (
        Restaurant.objects.prefetch_related("ratings", "sales")
        .filter(ratings__rating=5)
        .annotate(total=Sum("sales__income"))
    )

    # ratings = Rating.objects.filter(rating="5")
    # ratings = Rating.objects.all()

    print(restaurants)
    return render(request, "index.html")
