from django.views.generic.base import TemplateView
from dollar_charts_webapp.models import Entry
from django.views.generic.detail import DetailView
from datetime import datetime, timedelta

class EntriesIndex(TemplateView):
    template_name = 'entries/index.html'
    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_today = today + timedelta(hours=23, minutes=59, seconds=59)
        today_entry = Entry.objects.filter(date__gte=today, date__lte=end_today).first()
        context['entry'] = today_entry

        yesterday = today - timedelta(days=1)
        end_yesterday = yesterday + timedelta(hours=23, minutes=59, seconds=59)
        yesterday_entry = Entry.objects.filter(date__gte=yesterday, date__lte=end_yesterday).first()
        context['yesterday_entry'] = yesterday_entry

        context['buy_percent'] = 100 * (today_entry.buy_price - yesterday_entry.buy_price) / (today_entry.buy_price + yesterday_entry.buy_price)
        context['sell_percent'] = 100 * (today_entry.sell_price - yesterday_entry.sell_price) / (today_entry.sell_price + yesterday_entry.sell_price)

        week_entries = []
        base_date = today
        end_base_date = base_date + timedelta(hours=23, minutes=59, seconds=59)
        y_base_date = base_date - timedelta(days=1)
        y_end_base_date = y_base_date + timedelta(hours=23, minutes=59, seconds=59)

        for times in range(0, 7):
            entry = Entry.objects.filter(date__gte=base_date, date__lte=end_base_date).first()
            y_entry = Entry.objects.filter(date__gte=y_base_date, date__lte=y_end_base_date).first()

            week_entries.append({
                'entry': entry,
                'yesterday_entry': y_entry,
                'buy_percent': 100 * (entry.buy_price - y_entry.buy_price) / (entry.buy_price + y_entry.buy_price),
                'sell_percent': 100 * (entry.sell_price - y_entry.sell_price) / (entry.sell_price + y_entry.sell_price)
            })

            base_date = base_date - timedelta(days=1)
            end_base_date = base_date + timedelta(hours=23, minutes=59, seconds=59)
            y_base_date = base_date - timedelta(days=1)
            y_end_base_date = y_base_date + timedelta(hours=23, minutes=59, seconds=59)

        context['week_entries'] = week_entries

        return context