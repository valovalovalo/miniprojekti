*** Settings ***
Resource          resource.robot
Suite Setup       Open And Configure Browser
Suite Teardown    Close Browser
Test Setup        Reset References

*** Test Cases ***
Add And Edit Book Reference
    Go To                   ${HOME_URL}
    Click Link              Create a new reference
    Select From List By Value    id=entry_type    book
    Input Text              title               Original Book Title
    Input Text              authors             Original Author
    Input Text              year                2000
    Input Text              publisher           Original Publisher
    Click Button            Create Reference
    Page Should Contain     Original Book Title
    
    Go To                   ${HOME_URL}
    Click Link              View reference
    Click Button            Edit This Reference
    Input Text              title               Updated Book Title
    Input Text              authors             Updated Author
    Input Text              year                2023
    Input Text              publisher           Updated Publisher
    Click Button            Update Reference
    
    Go To                   ${HOME_URL}
    Click Link              View reference
    Page Should Contain     Updated Book Title
    Page Should Contain     Updated Author
    Page Should Contain     2023
    Page Should Contain     Updated Publisher

Test For Pre-filling
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  booktest
    Input Text  authors  book authors
    Input Text  publisher  book publisher
    Input Text  year  2000
    Input Text  isbn  1234
    Click Button  Create Reference
    Page Should Contain  booktest
    Click Button  Edit This Reference
    ${title}=  Get Value  id=title
    Should Be Equal  ${title}  booktest

Test For Returning To Single Page View
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  booktest
    Input Text  authors  book authors
    Input Text  publisher  book publisher
    Input Text  year  2000
    Click Button  Create Reference
    Click Button  Edit This Reference
    Input Text  isbn  1234
    Click Button  Update Reference
    Page Should Contain  Edit This Reference
