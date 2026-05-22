from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from .permissions import IsOwnerOrEditorReadOnly

class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEditorReadOnly]
    
    def get_queryset(self):
        user = self.request.user
        is_editor = user.groups.filter(name='Editor').exists()
        
        if is_editor:
            return JournalEntry.objects.all()
        return JournalEntry.objects.filter(author=user)
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PublicJournalEntryListView(generics.ListAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return JournalEntry.objects.filter(is_public=True)
