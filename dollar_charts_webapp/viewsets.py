from dollar_charts_webapp.serializers import EntrySerializer
from dollar_charts_webapp.models import Entry
from rest_framework import viewsets

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all().order_by('-date')
    serializer_class = EntrySerializer