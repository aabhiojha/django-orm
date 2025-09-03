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

    # user = User.objects.first()
    # restaurant = Restaurant.objects.first()

    # rating, created = Rating.objects.get_or_create(
    #     user=user, restaurant=restaurant, rating=9
    # )
    # if created:
    #     print("Rating is created")
    # else:
    #     print(rating)

    # rating = Rating(user=user, restaurant=restaurant, rating=10)
    # rating.full_clean()
    # rating.save()

    # restaurant = Restaurant.objects.last()
    # restaurant.name = "Ram lal ko paan pasal"
    # restaurant.save(update_fields=["name"])

    # Restaurant.objects.create(
    #     name="Aurora Cafe",
    #     website="https://auroracafe.com",
    #     date_opened="2021-5-15",
    #     latitude=40.7128,
    #     longitude=-74.0060,
    #     restaurant_type=Restaurant.TypeChoices.MEXICAN,  # must match one of the defined choices
    # )
    # print(restaurant)

    # restaurants = Restaurant.objects.all()
    # restaurants.update(date_opened=timezone.now())

    # restaurants = Restaurant.objects.filter(name__startswith="shyam")
    # print(restaurants.update(name="Shyam lal ko paan pasal"))
    # print(restaurants)

    # restaurant = Restaurant.objects.first()
    # print(restaurant.pk)
    # print(restaurant.ratings.all())
    # restaurant.delete()

    restaurant = Restaurant.objects.all().delete()
    print(restaurant)

    pprint(connection.queries)
