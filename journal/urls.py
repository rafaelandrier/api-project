from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, PublicJournalEntryListView

router = DefaultRouter()
router.register(r'entries', JournalEntryViewSet, basename='journalentry')

urlpatterns = [
    path('journal/public/', PublicJournalEntryListView.as_view(), name='public-entries'),
    path('', include(router.urls)),
]
