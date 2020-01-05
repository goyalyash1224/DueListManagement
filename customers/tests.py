from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from customers.models import Customer
from customers.views import customers_home, add_new_customer
from django.contrib.auth.models import User
from datetime import datetime, date, time



class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('customers_home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/customers/')
        self.assertEquals(view.func, customers_home)


class CustomerViewTests(TestCase):

    def setUp(self):
        user=User.objects.create_user('foo', password='bar')
        user.is_authenticated = True
        Customer.objects.create(agent = user, name='#1', dob=date(2015,1,1))

    def test_customer_views_success_status_code(self):
        url = reverse('customers_home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    # def test_customer_views_not_found_status_code(self):
    #     url = reverse('customers_home', kwargs={'pk': 99})
    #     response = self.client.get(url)
    #     self.assertEquals(response.status_code, 404)

    def test_customers_home_url_resolves_customers_views(self):
        view = resolve('/customers/')
        self.assertEquals(view.func, customers_home)