from .serializers import PersonSerializer, ContactsSerializer
from rest_framework.views import APIView
from .models import Person, Contacts
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView
)


class PersonAPIview(ListAPIView):
    """Handle the URL to get a list of people"""
    serializer_class = PersonSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Person.objects.all()
        return queryset_list


class PersonCreateAPIview(CreateAPIView):
    """Handle the URL to create a person"""

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        serializer.save()

class PersonUpdateAPIview(UpdateAPIView):
    """Handle the URL to update a person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_update(self, serializer):
        serializer.save()


class PersonDeleteAPIview(DestroyAPIView):
    """Handle the URL to delete a person"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ContactsCreateAPIview(CreateAPIView):
    """Handle the URL to create contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def perform_create(self, serializer):
        person_pk = self.kwargs.get('person_id')
        related_person = Person(pk=person_pk)
        serializer.save(person=related_person)


class ContactsAPIview(ListAPIView):
    """Handle the URL to get all contacts"""
    serializer_class = ContactsSerializer

    def get_queryset(self, *args, **kwargs):
        person_pk = self.kwargs.get('person_id')
        queryset_list = Contacts.objects.filter(person=person_pk)
        return queryset_list


class ContactsUpdateAPIview(UpdateAPIView):
    """Handle the URL to update contacts"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer

    def perform_update(self, serializer):
        serializer.save()


class ContactsDeleteAPIview(DestroyAPIView):
    """Handle the URL to delete a contact"""
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


