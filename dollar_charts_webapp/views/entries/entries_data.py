from dollar_charts_webapp.models import Entry
from django.http import JsonResponse

def weekly_data(request):
    context = {}
    today_entry = Entry.objects.order_by('-date').first()
    context['entry'] = today_entry.to_dict()

    yesterday_entry = Entry.objects.order_by('-date')[1]
    context['yesterday_entry'] = yesterday_entry.to_dict()

    context['buy_percent'] = 100 * (today_entry.buy_price - yesterday_entry.buy_price) / (today_entry.buy_price + yesterday_entry.buy_price)
    context['sell_percent'] = 100 * (today_entry.sell_price - yesterday_entry.sell_price) / (today_entry.sell_price + yesterday_entry.sell_price)

    week_entries_db = Entry.objects.order_by('-date')[:8]
    week_entries = []

    for times in range(0, 7):
        entry = week_entries_db[times]
        y_entry = week_entries_db[times + 1]

        week_entries.append({
            'entry': entry.to_dict(),
            'yesterday_entry': y_entry.to_dict(),
            'buy_percent': 100 * (entry.buy_price - y_entry.buy_price) / (entry.buy_price + y_entry.buy_price),
            'sell_percent': 100 * (entry.sell_price - y_entry.sell_price) / (entry.sell_price + y_entry.sell_price)
        })

    context['week_entries'] = list(week_entries)
    return JsonResponse(context)