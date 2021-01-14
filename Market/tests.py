from django.db.models import ProtectedError
from django.test import TestCase
from Users.models import User
from Market.models import *


# Create your tests here.
class MarketTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Dawid', last_name='Mantojfel', e_mail='Dawidmantojfel@gmail.com')
        self.book = Book.objects.create(title='IT', author='Stephen King', rate=4.5)
        self.market = Market.objects.create(user=self.user, book=self.book, price=12, condition='bad')

    def test_remove_book(self):
        with self.assertRaises(ProtectedError):
            self.book.delete()


class OpinionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(first_name='Karolina', last_name='Nowak', e_mail='Karolinanowak@gmail.com')
        self.book = Book.objects.create(title='103 ciasta siostry anastazji', author='Karol Marks', rate=5)
        self.opinion = Opinion.objects.create(book=self.book, user=self.user, opinion='This is really good book')

    '''i want to check what will happen with Opinion when i delete user'''
    def test_remove_user(self):
        self.user.delete()
        self.assertIsNone(self.opinion)
