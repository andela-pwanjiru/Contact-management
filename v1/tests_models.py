import datetime
from django.test import TestCase

from .models import Person, Contact


class ContactModelTest(TestCase):

    def test_contacts_creation(self):
        """Tests that a person's contact can be created"""
        contact = Contact.objects.create(email='sam@gmail.com',phone='+242452525', fax='35242')
        self.assertEqual(1, Contacts.objects.count())


class PersonModelTest(TestCase):

    def setUp(self):
        self.contacts = Contacts.objects.create(email='solom@gmail.com', phone='+242452525', fax='54593')


    def test_person_creation(self):
        """Tests that a person can be created"""
        person = Person.objects.create(name='Samantha', date_of_birth=datetime.datetime.today(), contacts=self.contacts)
        self.assertEqual(Person.name, 'Samantha')
        self.assertEqual(1, Person.objects.count())
