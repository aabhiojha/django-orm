from django.utils import timezone
from restaurant.models import Rating, Restaurant, Sale
from django.contrib.auth.models import User
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower


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

    # restaurant = Restaurant.objects.all()
    # rating = Rating.objects.all()
    # sale = Sale.objects.all()
    # print(restaurant.count())
    # print(rating.count())
    # print(sale.count())

    # chinese = Restaurant.TypeChoices.CHINESE
    # indian = Restaurant.TypeChoices.INDIAN
    # mexican = Restaurant.TypeChoices.MEXICAN
    # check_types = [chinese, indian, mexican]

    # restaurants = Restaurant.objects.filter(restaurant_type__in=check_types)
    # print(restaurants)

    # chinese = Restaurant.TypeChoices.CHINESE
    # restaurant = Restaurant.objects.exclude(restaurant_type=chinese)
    # print(restaurant)
    # print(restaurant.count())

    # restaurant = Restaurant.objects.filter(longitude__lt="0")
    # print(restaurant)

    # sales = Sale.objects.filter(income__range=(50, 60)).order_by("-income")
    # print([sale.income for sale in sales])
    restaurants = Restaurant.objects.order_by("date_opened")[2:5]
    print(restaurants)

    pprint(connection.queries)
