*** Settings ***
Test Template     Get test
Library           Libraries/APIWorkerLibrary.py

*** Test Cases ***
Get success     [Template]  Get test
    200  Headhead    val
    200  Head   Val
    200  Someh  Somev

Auth success     [Template]  Auth success test
    200  user1    someRoot
    200  useruser    root

Auth fail     [Template]  Auth fail test
    401  user1  passw1  user2  passw
    401  someUser  passw1  someUser  passw2

Stream success     [Template]  Stream success test
    200  5
    200  100

Failing     [Template]     Should fail
    some        400


*** Keywords ***
Get test   [Arguments]    ${expected}  ${headername}  ${headervalue}
    request get  ${headername}  ${headervalue}
    ${code_value} =  get resp status code str
    ${header_value} =  get resp header str  ${headername}
    should be equal  ${code_value}  ${expected}
    should be equal  ${header_value}  ${headervalue}

Auth success test   [Arguments]    ${expected}  ${valid_usr}  ${valid_pswd}
    request basic auth  ${valid_usr}  ${valid_pswd}  ${valid_usr}  ${valid_pswd}
    ${code_value} =  get resp status code str
    ${auth_value} =  get resp auth str
    ${user_value} =  get resp user str
    should be equal  ${code_value}  ${expected}
    should be equal  ${auth_value}  ${true}
    should be equal  ${user_value}  ${valid_usr}

Auth fail test   [Arguments]    ${expected}  ${valid_usr}  ${valid_pswd}  ${actual_usr}  ${actual_pswd}
    request basic auth  ${valid_usr}  ${valid_pswd}  ${actual_usr}  ${actual_pswd}
    ${code_value} =  get resp status code str
    should be equal  ${code_value}  ${expected}

Stream success test   [Arguments]    ${expected}  ${number}
    request stream  ${number}
    ${code_value} =  get resp status code str
    ${line_value} =  get resp line count str
    log  ${line_value}
    should be equal  ${code_value}  ${expected}

