import datetime
from django.test import TestCase

from .models import Person, Contacts


class PersonModelTest(TestCase):

    def test_person_creation(self):
        """Tests that a person can be created"""
        person = Person.objects.create(name='Samantha', date_of_birth=datetime.datetime.today())
        self.assertEqual(person.name, 'Samantha')
        

class ContactModelTest(TestCase):

    def setUp(self):
        self.person = Person.objects.create(name='Samantha', date_of_birth=datetime.datetime.today())


    def test_contact_creation(self):
        """Tests that a contact can be created"""
        contact = Contacts.objects.create(email='sam@gmail.com', phone='+242452525', fax='35242', person=self.person)
        self.assertEqual(1, Contacts.objects.count())
        self.assertEqual(1, Contacts.objects.count())
