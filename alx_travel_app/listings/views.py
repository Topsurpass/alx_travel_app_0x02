from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing listing instances.

	This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for the Listing model.
	"""
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
	"""
	A viewset for viewing and editing booking instances.

	This viewset provides `list`, `create`, `retrieve`, `update`, and `destroy` actions for the Booking model.
	"""
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer