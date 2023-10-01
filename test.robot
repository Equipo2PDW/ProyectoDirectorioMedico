*** Variables ***
${ID_TEMP}              20
${HOSTNAME}             localhost
${PORT}                 8000                
${SERVER_detail}               http://${HOSTNAME}:${PORT}/clinica/detail_view/${ID_TEMP}
${SERVER_buscador}             http://${HOSTNAME}:${PORT}/clinica/list_view
${SERVER_create}               http://${HOSTNAME}:${PORT}/clinica/create
${SERVER_update}               http://${HOSTNAME}:${PORT}/clinica/${ID_TEMP}/update
${BROWSER}              chrome


*** Settings ***

Documentation   Django Robot Tests
Library         SeleniumLibrary  timeout=15  implicit_wait=10
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=mysite/mysite  manage=manage.py  settings=DirectorioMedico.settings
Suite Setup     open Browserr
Suite Teardown  close browserr

*** Keywords ***

open Browserr
  Open Browser  ${SERVER_buscador}  ${BROWSER}

close browserr
  Close Browser


*** Test Cases ***

Scenario: Crear medico
  Go To  ${SERVER_create}
  Wait Until Page Contains Element  id=crear
  Page Should Contain  Añadir
  Input Text  id:id_nombre  MedicoTest
  Input Text  id:id_apellido  ApellidoTest
  Unselect All From List    id:id_especialidades
  Select From List By Label    id:id_especialidades   Cardiología
  Unselect All From List    id:id_sucursales
  Select From List By Label    id:id_sucursales   Sucursal Centro | comuna: Santiago
  Input Text  id:id_anos_experiencia  10
  Click Button  Crear
  Wait Until Page Contains  MedicoTest

Scenario: Actualizar informacion medico
  Go TO  ${SERVER_update}
  Wait Until Page Contains    Nombre:
  Input Text  id:id_nombre  Alonso
  Input Text  id:id_apellido  Sanchez
  Unselect All From List    id:id_especialidades
  Select From List By Label    id:id_especialidades   Cardiología
  Unselect All From List    id:id_sucursales
  Select From List By Label    id:id_sucursales   Sucursal Centro | comuna: Santiago
  Input Text  id:id_anos_experiencia  10
  Click Button  Update
  Wait Until Page Contains  Alonso Sanchez
  Wait Until Page Contains  Cardiología
  Wait Until Page Contains  Sucursal Centro | comuna: Santiago
  Wait Until Page Contains  10 años de experiencia profesional

Scenario: Buscar por Comuna
  Go To  ${SERVER_buscador}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos
  Wait Until Element Is Visible  id:comuna
  Select From List By Value    id:comuna    Santiago
  Click Button  Buscar
  Page Should Contain  Dr. Pia Diaz


Scenario: Buscar por Especialidad
  Go To  ${SERVER_buscador}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos
  Wait Until Element Is Visible  id:especialidad
  Select From List By Value    id:especialidad    Infantil
  Click Button  Buscar
  Page Should Contain  Dr. Sergio Ramirez

Scenario: Buscar por Nombre
  Go To  ${SERVER_buscador}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos
  Wait Until Element Is Visible  id:nombre_medico
  Input Text  id:nombre_medico  Joaquin
  Click Button  Buscar
  Page Should Contain  Joaquin

Scenario: Eliminar medico
  Go To  ${SERVER_DETAIL}
  Wait Until Page Contains  Nombre
  Page Should Contain  Eliminar
  Click Element  id=delete
  Wait Until Page Contains  Estas seguro que deseas eliminar a este medico?
  Click Button  Yes
  Wait Until Page Contains  Conoce a nuestros medicos