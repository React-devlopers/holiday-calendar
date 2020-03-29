from rest_framework import serializers

from rest.models import Holiday


class HolidaySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ('id', 'user', 'date')
