import datetime
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from v1.models import Person, Contacts



class PersonAPITests(APITestCase):

    def setUp(self):
        """Setup initial data"""
        self.client = APIClient()
        self.person = Person.objects.create(name='Samantha', date_of_birth=datetime.datetime.today())
        self.contact = Contacts.objects.create(email='sam@gmail.com', phone='+242452525', fax='35242', person=self.person)

    def test_create_person(self):
        """
        Test we can create a person
        """
        url = reverse('person_create')
        data = {'name': 'Chris'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(Person.objects.count(), 1)

    def test_get_person(self):
        """
        Test getting all people
        """
        response = self.client.get(
            reverse('person_view'))
        self.assertEqual(len(Person.objects.all()), 1)
