from dollar_charts_webapp.views.entries.entries_data import weekly_data
from dollar_charts_webapp.views.entries.entries_index import EntriesIndex
from dollar_charts_webapp.views.entries.entries_chart import EntriesChart
from dollar_charts_webapp.viewsets import EntryViewSet
from django.urls import path, include
from rest_framework import routers
from dollar_charts_webapp.views.entries.entries_list import EntriesList
from .url_views import scrap

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet, basename='entry')

urlpatterns = [
    path('', EntriesIndex.as_view(), name='entries_index'),
    path('historic/', EntriesList.as_view(), name='entries_list'),
    path('chart/', EntriesChart.as_view(), name='entries_chart'),
    path('scrap/', scrap, name='entries_scrap'),
    path('api/', include(router.urls)),
    path('weekly/', weekly_data, name='weekly_data'),
]