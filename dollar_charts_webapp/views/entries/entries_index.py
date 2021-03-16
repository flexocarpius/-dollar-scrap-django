from django.views.generic.base import TemplateView
from dollar_charts_webapp.models import Entry
from django.views.generic.detail import DetailView
from datetime import datetime, timedelta

class EntriesIndex(TemplateView):
    template_name = 'entries/index.html'
    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today_entry = Entry.objects.order_by('-date').first()
        context['entry'] = today_entry

        yesterday_entry = Entry.objects.order_by('-date')[1]
        context['yesterday_entry'] = yesterday_entry

        context['buy_percent'] = 100 * (today_entry.buy_price - yesterday_entry.buy_price) / (today_entry.buy_price + yesterday_entry.buy_price)
        context['sell_percent'] = 100 * (today_entry.sell_price - yesterday_entry.sell_price) / (today_entry.sell_price + yesterday_entry.sell_price)

        week_entries_db = Entry.objects.order_by('-date')[:8]
        week_entries = []

        for times in range(0, 7):
            entry = week_entries_db[times]
            y_entry = week_entries_db[times + 1]

            week_entries.append({
                'entry': entry,
                'yesterday_entry': y_entry,
                'buy_percent': 100 * (entry.buy_price - y_entry.buy_price) / (entry.buy_price + y_entry.buy_price),
                'sell_percent': 100 * (entry.sell_price - y_entry.sell_price) / (entry.sell_price + y_entry.sell_price)
            })

        context['week_entries'] = week_entries

        return context