from rest_framework import serializers
from .models import Person, Contacts


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'date_of_birth')


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ('id', 'email', 'phone', 'fax', 'person')

    #