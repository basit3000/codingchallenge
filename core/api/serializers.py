from rest_framework.serializers import ModelSerializer
from core.models import Event, Offer, Restaurant

class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

    
