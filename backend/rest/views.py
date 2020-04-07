from rest_framework import viewsets

from rest.models import Holiday
from rest.serialisers import HolidaySerialiser


class HolidayView(viewsets.ModelViewSet):
    serializer_class = HolidaySerialiser
    queryset = Holiday.objects.all()

