from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.models import Offer, Event, Restaurant
from .serializers import OfferSerializer, EventSerializer, RestaurantSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/restaurants', 
        'GET /api/offers',
        'GET /api/events',
        'GET /api/restaurants/:id',
        'GET /api/offers/:id',
        'GET /api/events/:id'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getRestaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRestaurant(request,pk):
    restaurant = Restaurant.objects.get(id=pk)
    serializer = RestaurantSerializer(restaurant, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getOffers(request):
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOffer(request, pk):
    offer = Offer.objects.get(id=pk)
    serializer = OfferSerializer(offer, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvent(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)
