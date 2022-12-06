from django.urls import path
from .views import showtripsPageView, showAfricaPageView, showAsiaPageView, showAustraliaPageView
from .views import showEuropePageView, showNorthAmericaPageView, showSouthAmericaPageView

urlpatterns = [
    path("", showtripsPageView, name = 'showtrips'),
    path("africa/", showAfricaPageView, name = 'africa'),
    path("asia/", showAsiaPageView, name = 'asia'),
    path("australia/", showAustraliaPageView, name = 'australia'),
    path("europe/", showEuropePageView, name = 'europe'),
    path("northamerica/", showNorthAmericaPageView, name = 'northamerica'),
    path("southamerica/", showSouthAmericaPageView, name = 'southamerica'),
]