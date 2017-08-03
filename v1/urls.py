
from django.conf.urls import url, include
from .views import (PersonAPIview, PersonCreateAPIview, PersonUpdateAPIview, PersonDeleteAPIview, ContactsCreateAPIview, ContactsAPIview, ContactsUpdateAPIview, ContactsDeleteAPIview)

urlpatterns = [
    url(r'^person/$', PersonAPIview.as_view(), name='person_view'),
    url(r'^person/create$', PersonCreateAPIview.as_view(), name='person_create'),
    url(r'^person/(?P<pk>[0-9]+)/update$', PersonUpdateAPIview.as_view(), name='person_update'),
    url(r'^person/(?P<pk>[0-9]+)/delete$', PersonDeleteAPIview.as_view(), name='person_delete'),
    url(r'^person/(?P<person_id>[0-9]+)/contacts/$', ContactsAPIview.as_view(), name='person_view'),
    url(r'^person/(?P<person_id>[0-9]+)/contacts/create/$', ContactsCreateAPIview.as_view(), name='contacts_create'),
    url(r'^person/(?P<person_id>[0-9]+)/contacts/(?P<pk>[0-9]+)/delete/$', PersonDeleteAPIview.as_view(), name='contacts_delete'),
    url(r'^person/(?P<person_id>[0-9]+)/contacts/(?P<pk>[0-9]+)/update/$', ContactsUpdateAPIview.as_view(), name='contacts_update'),
]