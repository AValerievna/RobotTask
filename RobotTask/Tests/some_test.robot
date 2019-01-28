*** Settings ***
Test Template     Calculate
Library           Libraries/APIWorkerLibrary.py

*** Test Cases ***  Expected
Success test        200

*** Keywords ***
Calculate
    [Arguments]    ${expected}
    request get
    check response  ${expected}