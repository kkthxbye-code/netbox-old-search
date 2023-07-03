from django.urls import include, path
from .views import SearchView

urlpatterns = (path("search/", SearchView.as_view(), name="customsearch"),)
