*** Settings ***
Test Template     Success code
Library           Libraries/APIWorkerLibrary.py

*** Test Cases ***
Suc     [Template]  Temp1   100     head    val
Success test    [Template]  Temp2   200 Head   Val

Failing     [Template]     Should fail     some        400


*** Keywords ***
Success code    [Arguments]    ${expected}  ${headername} ${headervalue}
    log   ${headername}
    request get  ${headername}  ${headervalue}
    ${code_value} =  get resp status code str
    ${header_value} =  get resp header str  C${headername}=
    should be equal  ${code_value}   ${expected}


