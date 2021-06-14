from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Contacts
from .serializers import ContactSerializer


class ContactListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Contacts.objects.filter(owner=self.request.user)