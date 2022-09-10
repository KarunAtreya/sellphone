
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Phone

class PhoneTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username = 'testuser1', password = 'abc123'
        )
        testuser1.save()

        test_phone = Phone.objects.create(
            owner = testuser1, brand = 'A', model = '8', variant = 'B', storage = '256', battery ='B', 
            touchorfaceid = 'yes working', truetone = True, screen_issues = False , body_issues = False
        )
        test_phone.save()

    def testPhoneContent(self):
        phone = Phone.objects.get(id=1)
        owner = f'{phone.owner}'
        brand = f'{phone.brand}'
        model = f'{phone.model}'
        variant = f'{phone.variant}'
        storage = f'{phone.storage}'
        battery = f'{phone.battery}'
        touchorfaceid = f'{phone.touchorfaceid}'
        truetone = phone.truetone
        screen_issues = phone.screen_issues
        body_issues = phone.body_issues
        self.assertEqual(owner, 'testuser1')
        self.assertEqual(brand, 'A')
        self.assertEqual(model, '8')
        self.assertEqual(variant, 'B')
        self.assertEqual(storage, '256')
        self.assertEqual(battery, 'B')
        self.assertEqual(touchorfaceid, 'yes working')
        self.assertEqual(truetone, True)
        self.assertEqual(screen_issues, False)
        self.assertEqual(body_issues, False)