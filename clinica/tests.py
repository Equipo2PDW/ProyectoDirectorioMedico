
from django.urls import reverse

from django.test import TestCase, RequestFactory, Client
from unittest.mock import Mock, patch, MagicMock
from clinica.forms import CitaForm
from django.contrib.messages.storage.fallback import FallbackStorage
from clinica.views import delete_cita
from clinica.models import citaMedica
from django.shortcuts import get_object_or_404
from clinica.views import create_cita

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta


import time

#PRUEBAS DE INTERFAZ
"""
class InicialTest(LiveServerTestCase):
	 
	def testinicial(self):
		print("hola")
		driver = webdriver.Chrome()

		driver.get('http://localhost:8000/clinica/list_view')

		time.sleep(1)

		#medico = driver.find_element_by_id('nombre_medico')
		medico = driver.find_element(By.ID, 'nombre_medico')
		
		time.sleep(3)

		submit = driver.find_element(By.ID,'buscar_button')

		medico.send_keys('Alonso')

		submit.click()
		time.sleep(5)
		assert 'Alonso' in driver.page_source"""

class CrearCitaTest(LiveServerTestCase):
	 
	def test_crear_cita_correcta(self):

		driver = webdriver.Chrome()

		driver.get('http://localhost:8000/clinica/create_cita')

		time.sleep(1)

		medico = driver.find_element(By.ID, 'id_medico')
		paciente = driver.find_element(By.ID, 'id_paciente')
		fecha = driver.find_element(By.ID, 'id_fecha')
		hora = driver.find_element(By.ID, 'id_hora')
		centro = driver.find_element(By.ID, 'id_centro')       
		
		select_medico = Select(medico)
		select_paciente = Select(paciente)
		#select_fecha = Select(fecha)
		#select_hora = Select(hora)
		select_centro = Select(centro)

		select_medico.select_by_value('15') #alonso
		select_paciente.select_by_value('1') #debora
		#select_fecha.select_by_value('2023-12-01')
		#select_hora.select_by_value('08:00')
		select_centro.select_by_value('2')

		fecha.send_keys('20-12-2023')
		hora.send_keys('22:50')
		time.sleep(2)
		

		submit = driver.find_element(By.ID,'crear')

		#medico.send_keys('Alonso')

		submit.click()
		time.sleep(5)
		assert 'Cita añadida correctamente.' in driver.page_source

	def test_crear_cita_hora_incorrecta(self):
		driver = webdriver.Chrome()

		driver.get('http://localhost:8000/clinica/create_cita')

		time.sleep(1)

		medico = driver.find_element(By.ID, 'id_medico')
		paciente = driver.find_element(By.ID, 'id_paciente')
		fecha = driver.find_element(By.ID, 'id_fecha')
		hora = driver.find_element(By.ID, 'id_hora')
		centro = driver.find_element(By.ID, 'id_centro')       
		
		select_medico = Select(medico)
		select_paciente = Select(paciente)
		select_centro = Select(centro)

		select_medico.select_by_value('15') #alonso
		select_paciente.select_by_value('1') #debora
		
		select_centro.select_by_value('2')

		fecha.send_keys('20-12-2023')
		# Obtener la hora actual
		hora_actual = datetime.now()

		# Restar una cantidad de tiempo (por ejemplo, una hora)
		hora_menos_una_hora = hora_actual - timedelta(hours=1)
		formato_hora = "%H:%M"  # Formato para mostrar solo la hora:Minuto:Segundo
		hora_menos_una_hora_str = hora_menos_una_hora.strftime(formato_hora)

		hora.send_keys(hora_menos_una_hora_str)
		time.sleep(2)
		

		submit = driver.find_element(By.ID,'crear')


		submit.click()
		time.sleep(5)
		assert 'La hora no puede ser anterior a la hora actual.' in driver.page_source

#PRUEBAS UNITARIAS

"""class CreateCitaViewTest(TestCase):

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

class DeleteCitaViewTest(TestCase):
	def setUp(self):
		self.factory = RequestFactory()

	@patch('clinica.views.get_object_or_404')
	def test_delete_cita(self, mock_get):
		# Crea una instancia de citaMedica simulada
		cita_instance = citaMedica()
		cita_instance.id = 1  # Establece un ID simulado

		# Simula el comportamiento del método delete en la instancia simulada
		cita_instance.delete = MagicMock()

		# Configura el mock de get_object_or_404 para devolver la instancia simulada
		mock_get.return_value = cita_instance

		# Crea una solicitud POST para la vista de eliminación
		response = self.client.post(reverse('delete_cita_view', args=[cita_instance.id]))

		# Verifica que el método delete se haya llamado y que la vista redirige
		cita_instance.delete.assert_called_once()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('citas_view'))

"""



"YA NO SIRVE"

"""class DeleteCitaViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.request = self.factory.post(reverse('delete_cita_view', args=[1]))  # Utiliza reverse para generar la URL
		setattr(self.request, 'session', {})
		messages = FallbackStorage(self.request)
		setattr(self.request, '_messages', messages)

	@patch('clinica.views.CitaForm')
	@patch('clinica.views.citaMedica')
	def test_delete_cita(self, mock_cita_medica, mock_cita_form):
		# Crea una instancia de citaMedica simulada sin necesidad de acceder a la base de datos
		cita_instance = mock_cita_medica()

		# Simula que el formulario es válido
		form_instance = mock_cita_form.return_value
		form_instance.is_valid.return_value = True

		# Llama a la vista con la solicitud y el formulario
		response = delete_cita(self.request, id=cita_instance.id)

		cita_instance.delete.assert_called_once()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('citas_view'))"""
	
"""class DeleteCitaViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.request = self.factory.get(reverse('delete_cita_view', args=[1]))  # Utiliza reverse para generar la URL
		setattr(self.request, 'session', {})
		messages = FallbackStorage(self.request)
		setattr(self.request, '_messages', messages)

	@patch.object(citaMedica, 'delete')
	def test_delete_cita(self, mock_delete):
		cita_instance = CitaMedicaFactory()  # Crea una citaMedica con un ID único

		response = delete_cita(self.request, id=cita_instance.id)

		mock_delete.assert_called_once()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('citas_view'))"""

"""class DeleteCitaViewTest(TestCase):
	def setUp(self):
		self.client = Client()
		self.factory = RequestFactory()
		self.request = self.factory.post(reverse('delete_cita', args=[1]))  # Utiliza reverse para generar la URL
		setattr(self.request, 'session', {})
		messages = FallbackStorage(self.request)
		setattr(self.request, '_messages', messages)

	@patch('clinica.views.citaMedica')
	def test_delete_cita(self, mock_cita_medica):
		cita_instance = CitaMedicaFactory()  # Crea una citaMedica con un ID único

		response = delete_cita(self.request, id=cita_instance.id)

		cita_instance.delete.assert_called_once()
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, reverse('citas_view'))



	@patch('clinica.views.CitaForm')
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


