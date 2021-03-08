from dollar_charts_webapp.models import Entry
from rest_framework import serializers

# Serializers define the API representation.
class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        fields = ['id', 'date', 'buy_price', 'sell_price']