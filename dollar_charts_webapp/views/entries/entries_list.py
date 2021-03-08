from django.views.generic import ListView
from dollar_charts_webapp.models import Entry

class EntriesList(ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'entries/entries_list.html'

    def get_queryset(self):
        return Entry.objects.all().order_by('-date')
    