from django.views.generic.base import TemplateView
from dollar_charts_webapp.models import Entry

class EntriesChart(TemplateView):
    template_name = 'entries/chart.html'
    