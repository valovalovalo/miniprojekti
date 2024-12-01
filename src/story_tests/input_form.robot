*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

Input Form Is Correct When Choosing Article
    Go To  ${NEW_REFERENCE_URL}
    Select From List By Value  id=entry_type  article
    Page Should Contain  Title
    Page Should Contain  Volume
    Page Should Contain  Journal
    Page Should Contain  Pages

Input Form Is Correct When Choosing Book
    Go To  ${NEW_REFERENCE_URL}
    Select From List By Value  id=entry_type  book
    Page Should Contain  Title
    Page Should Contain  Publisher
    Page Should Contain  ISBN

Input Form Is Correct When Choosing Inproceedings
    Go To  ${NEW_REFERENCE_URL}
    Select From List By Value  id=entry_type  inproceedings
    Page Should Contain  Title
    Page Should Contain  Book Title
    Page Should Contain  Publisher
    Page Should Contain  Pages
