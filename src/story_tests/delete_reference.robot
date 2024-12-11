*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

At Start There Are No References
    Go To  ${HOME_URL}
    Page Should Not Contain Element  xpath=//li

Delete Reference After Creation
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test3
    Input Text  authors  test
    Input Text  year  2021
    Click Button  Create Reference
    Page Should Contain  test3
    Go To  ${HOME_URL}
    Click Link  View reference
    Click Button  Delete This Reference
    Page Should Not Contain  test3
