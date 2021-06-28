from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Buyer

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        test_product = Product.objects.create(
            name='Banana', 
            description='a body here',
            price='200.53',
            location='Ogun',
            imageUrl='https://www.google.com/search?q=milk&sxsrf=ALeKk02f4IWAk9BlWbHNsJ970UN',
            isSold=False,
            seller=testuser1
            )
        test_product.save()

    def test_name_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, 'Banana')
    
    def test_description_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.description}'
        self.assertEquals(expected_object_name, 'a body here')
    
    def test_price_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.price}'
        self.assertEquals(expected_object_name, '200.53')

    def test_location_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.location}'
        self.assertEquals(expected_object_name, 'Ogun')

    def test_imageUrl_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.imageUrl}'
        self.assertEquals(expected_object_name, 'https://www.google.com/search?q=milk&sxsrf=ALeKk02f4IWAk9BlWbHNsJ970UN')

    def test_isSold_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.isSold}'
        self.assertEquals(expected_object_name, 'False')

    def test_user_content(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.seller}'
        self.assertEquals(expected_object_name, 'testuser1')


class BuyerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        test_product = Product.objects.create(
            name='Banana', 
            description='a body here',
            price='200.53',
            location='Ogun',
            imageUrl='https://www.google.com/search?q=milk&sxsrf=ALeKk02f4IWAk9BlWbHNsJ970UN',
            isSold=False,
            seller=testuser1
            )
        test_product.save()

        Buyer.objects.create(
            name='Bolanle', 
            phoneNumber='08039659662',
            emailAddress='admin@gmail.com',
            product=test_product
            )

    def test_name_content(self):
        buyer = Buyer.objects.get(id=1)
        expected_object_name = f'{buyer.name}'
        self.assertEquals(expected_object_name, 'Bolanle')
    
    def test_phoneNumber_content(self):
        buyer = Buyer.objects.get(id=1)
        expected_object_name = f'{buyer.phoneNumber}'
        self.assertEquals(expected_object_name, '08039659662')
    
    def test_emailAddress_content(self):
        buyer = Buyer.objects.get(id=1)
        expected_object_name = f'{buyer.emailAddress}'
        self.assertEquals(expected_object_name, 'admin@gmail.com')

    def test_product_content(self):
        buyer = Buyer.objects.get(id=1)
        expected_object_name = f'{buyer.product}'
        self.assertEquals(expected_object_name, 'Banana')

