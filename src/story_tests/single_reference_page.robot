*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***
At start there are no references
    Go To  ${HOME_URL}
    Page Should Not Contain Element  xpath=//li

After adding a reference, site displays it
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  Taru sormusten herrasta
    Input Text  authors  Lassi
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  Taru sormusten herrasta

Test If Single Page View Works
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  Taru sormusten herrasta
    Input Text  authors  Lassi
    Input Text  year  2000
    Click Button  Create Reference
    Click Link  View reference
    Page Should Contain  Taru sormusten herrasta
    Page Should Contain  Lassi
    Page Should Contain  2000

Test If Back To Home Page Button Works
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  Taru sormusten herrasta
    Input Text  authors  Lassi
    Input Text  year  2000
    Click Button  Create Reference
    Click Link  View reference
    Click Link  Back to home page
    Page Should Contain  Create a new reference
