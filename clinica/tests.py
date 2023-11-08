from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory, Client
from unittest.mock import Mock, patch
from clinica.forms import CitaForm
from django.contrib.messages.storage.fallback import FallbackStorage

from clinica.views import create_cita

class CreateCitaViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.request = self.factory.post('/create_cita/', data={})
        setattr(self.request, 'session', {})
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)

    @patch('clinica.views.CitaForm')
    def test_create_cita_with_valid_form(self, mock_cita_form):
        # Create a mock instance of the form
        form_instance = mock_cita_form.return_value
        form_instance.is_valid.return_value = True

        # Create a mock request
        request = self.factory.post('/create_cita/', data={})
        
        # Call the view function
        response = create_cita(self.request)

        # Check that the form is saved
        form_instance.save.assert_called_once()

        # Check that the view redirects to the expected URL (replace 'nombre_de_la_vista' with the actual view name)
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect
        self.assertEqual(response.url, '/clinica/citas_view')  # Replace with the actual URL

    """@patch('clinica.views.CitaForm')
    def test_create_cita_with_invalid_form(self, mock_cita_form):
        # Create a mock instance of the form
        form_instance = mock_cita_form.return_value
        form_instance.is_valid.return_value = False

        # Call the view function using the Django test client
        response = self.client.post('/create_cita/', data={})

        # Check that the form is not saved
        form_instance.save.assert_not_called()

        # Check that the view renders the expected template
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for a successful response
        self.assertTemplateUsed(response, 'create_cita.html')"""


"""import unittest
from unittest.mock import Mock, patch
from django.test import RequestFactory
from clinica.forms import CitaForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase

from clinica.views import create_cita

class CreateCitaViewTest(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.post('/create_cita/', data={})
        setattr(self.request, 'session', {})
        messages = FallbackStorage(self.request)
        setattr(self.request, '_messages', messages)

    @patch('clinica.views.CitaForm')
    def test_create_cita_with_valid_form(self, mock_cita_form):
        # Create a mock instance of the form
        form_instance = mock_cita_form.return_value
        form_instance.is_valid.return_value = True

        # Create a mock request
        request = self.factory.post('/create_cita/', data={})
        
        # Call the view function
        response = create_cita(self.request)

        # Check that the form is saved
        form_instance.save.assert_called_once()

        # Check that the view redirects to the expected URL (replace 'nombre_de_la_vista' with the actual view name)
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for a redirect
        self.assertEqual(response.url, '/clinica/citas_view')  # Replace with the actual URL

    @patch('clinica.views.CitaForm')
    def test_create_cita_with_invalid_form(self, mock_cita_form):
        # Create a mock instance of the form
        form_instance = mock_cita_form.return_value
        form_instance.is_valid.return_value = False

        # Create a mock request
        request = self.factory.post('/create_cita/', data={})
        
        # Call the view function
        response = create_cita(self.request)

        # Check that the form is not saved
        form_instance.save.assert_not_called()

        # Check that the view renders the expected template
        self.assertEqual(response.status_code, 200)  # 200 is the HTTP status code for a successful response
        self.assertTemplateUsed(response, 'create_cita.html')
"""


