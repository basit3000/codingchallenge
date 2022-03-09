from django.shortcuts import render
from django.db.models import Q
from .models import Restaurant, Offer, Event 

def home(request):
    return render(request, 'core/home.html')

def search(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    offers=Offer.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(start_date__icontains=q) |
        Q(end_date__icontains=q) |
        Q(location__icontains=q)
    )
    events=Event.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(start_date__icontains=q) |
        Q(end_date__icontains=q) |
        Q(location__icontains=q)
    )
    context={'offers':offers, 'events':events}
    return render(request, 'core/search.html', context)

def resultOffer(request, pk):
    offer=Offer.objects.get(id=pk)
    context = {"offer" : offer}
    return render(request, 'core/result.html', context)

def resultEvent(request, pk):
    event=Event.objects.get(id=pk)
    context = {"event" : event}
    return render(request, 'core/result.html', context)