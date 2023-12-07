from django.test import TestCase, Client
from django.urls import reverse
from .models import attendance_pool,User,subject

class YourViewFunctionTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            dept='IT',
            sem=1,
            role='Student',
            userid=123
        )

        # Create a test attendance pool
        self.attendance_pool = attendance_pool.objects.create(
            start_time='08:00:00',
            end_time='10:00:00',
            created_by=self.user,
            subject=subject.objects.get(id=1),  # Adjust this based on your actual model
            recieved_attendance=0,
            is_alive=True,
            latitude=12.345678,
            longitude=45.678912
        )

    def test_check_access_for_request_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the URL for your view, replace 'your_view_name' with the actual name or path
        url = reverse('checkpoint_request', kwargs={'pk': self.attendance_pool.id})

        # Make a POST request to the view
        response = self.client.post(url)

        # Check that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        data = response.json()

        # Check that the 'message' key is present in the response
        self.assertIn('message', data)

        # Check the value of the 'message' key
        self.assertTrue(data['message'] in ['true', 'false'])

    def tearDown(self):
        # Clean up the test data
        self.user.delete()
        self.attendance_pool.delete()
