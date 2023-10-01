*** Variables ***

${HOSTNAME}             localhost
${PORT}                 8000
${SERVER}               http://${HOSTNAME}:${PORT}/clinica/detail_view
${BROWSER}              chrome


*** Settings ***

Documentation   Django Robot Tests
Library         SeleniumLibrary  timeout=15  implicit_wait=0
Library         DjangoLibrary  ${HOSTNAME}  ${PORT}  path=mysite/mysite  manage=manage.py  settings=DirectorioMedico.settings
Suite Setup     open Browserr
Suite Teardown  close browserr

*** Keywords ***

open Browserr
  Open Browser  ${SERVER}  ${BROWSER}

close browserr
  Close Browser


*** Test Cases ***

Scenario: Buscar por Comuna
  Go To  ${SERVER}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos
  Wait Until Element Is Visible  id=comuna
  Select From List By Value    id:comuna    Santiago
  Page Should Contain  No se encontraron resultados.

Scenario: Buscar por Comuna ayuda
  Go To  ${SERVER}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos
  Wait Until Element Is Visible  id:comuna
  Select From List By Value    id:comuna    Santiago
  Click Button  Buscar
  Page Should Contain  Dr.

Scenario: Ayuda
  Go To  ${SERVER}
  Wait Until Page Contains Element  id=buscador
  Page Should Contain  Conoce a nuestros medicos