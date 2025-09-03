from django.utils import timezone
from restaurant.models import Rating, Restaurant, Sale
from django.contrib.auth.models import User
from django.db import connection
from pprint import pprint


def run():
    # forward query
    # rating = Rating.objects.first()
    # print(rating.restaurant)

    # backward  query
    # restaurant = Restaurant.objects.first()
    # ratings = restaurant.ratings.all()
    # print(ratings)

    pprint(connection.queries)
