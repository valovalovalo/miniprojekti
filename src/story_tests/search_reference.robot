*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

Test For Searching Reference
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test1
    Input Text  authors  test
    Input Text  year  2000
    Click Button  Create Reference
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test2
    Input Text  authors  test2 authors
    Input Text  year  1999
    Click Button  Create Reference
    Click Button  Back to List
    Input Text  search  test1
    Click Button  Search
    Page Should Contain  test1
    Page Should Not Contain  test2

Test For Upper Or Lower Case Not Mattering
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  Test1
    Input Text  authors  Test
    Input Text  year  2000
    Click Button  Create Reference
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test2
    Input Text  authors  test2 authors
    Input Text  year  1999
    Click Button  Create Reference
    Click Button  Back to List
    Input Text  search  test
    Click Button  Search
    Page Should Contain  Test1
    Page Should Contain  test2

Test For Matching Words
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test for matching words
    Input Text  authors  Test
    Input Text  year  2000
    Click Button  Create Reference
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test2
    Input Text  authors  test2 authors
    Input Text  year  1999
    Click Button  Create Reference
    Click Button  Back to List
    Input Text  search  chi
    Click Button  Search
    Page Should Contain  test for matching words
    Page Should Not Contain  test2