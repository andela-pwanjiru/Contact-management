from rest_framework import serializers
from .models import Person, Contacts


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'date_of_birth', 'contacts')


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('email', 'phone', 'fax')
