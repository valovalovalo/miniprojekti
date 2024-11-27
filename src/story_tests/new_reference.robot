*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***
At Start There Are No References
    Go To  ${HOME_URL}
    Page Should Not Contain Element  xpath=//li

After Adding A Reference, Site Displays It
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Input Text  title  test1
    Input Text  authors  test
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  test1

Test For Empty Input Fields
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Click Button  Create Reference
    Location Should Be  ${NEW_REFERENCE_URL}

Test For Invalid Input Year
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Input Text  title  test2
    Input Text  authors  test
    Input Text  year  1800
    Click Button  Create Reference
    Location Should Be  ${NEW_REFERENCE_URL}
    Input Text  year  2025
    Location Should Be  ${NEW_REFERENCE_URL}

    