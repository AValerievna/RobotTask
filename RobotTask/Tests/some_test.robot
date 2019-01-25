*** Settings ***
Library           APIWorkerLibrary.py

*** Test Cases ***
Success
    request get
    check response  200

