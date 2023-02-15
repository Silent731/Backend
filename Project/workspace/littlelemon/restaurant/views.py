from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import Menu
from rest_framework import generics
from .serializer import MenuSerializer, MenuItemSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializer import BookingSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

