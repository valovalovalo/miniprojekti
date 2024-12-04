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
    Select From List By Value  id=entry_type  book
    Input Text  title  test1
    Input Text  authors  test
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  test1

Test For Empty Input Fields
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Click Button  Create Reference
    Location Should Be  ${NEW_REFERENCE_URL}

Test For Minimal Input Article
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  article
    Input Text  title  articletest
    Input Text  authors  article authors
    Input Text  year  2000
    Input Text  journal  article journal
    Click Button  Create Reference
    Page Should Contain  articletest

Test For Full Input Article
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  article
    Input Text  title  articletest
    Input Text  authors  article authors
    Input Text  year  2000
    Input Text  journal  article journal
    Input Text  volume  article volume
    Input Text  number  1
    Input Text  pages  2
    Click Button  Create Reference
    Page Should Contain  articletest

Test For Minimal Input Book
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  booktest
    Input Text  authors  book authors
    Input Text  publisher  book publisher
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  booktest

Test For Full Input Book
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

Test For Minimal Input Inproceeding
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  inproceedings
    Input Text  title  inproceedingstest
    Input Text  authors  inproceedings authors
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  inproceedingstest

Test For Full Input Inproceeding
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  inproceedings
    Input Text  title  inproceedingstest
    Input Text  booktitle  inproceedingsbooktitle
    Input Text  authors  inproceedings authors
    Input Text  year  2000
    Input Text  pages  2
    Input Text  publisher  inproceedingspublisher
    Click Button  Create Reference
    Page Should Contain  inproceedingstest

#Test For Invalid Input Year
#    Go To  ${HOME_URL}
#    Click Link  Create a new reference
#    Select From List By Value  id=entry_type  book
#    Input Text  title  test2
#    Input Text  authors  test
#    Input Text  year  -1800
#    Click Button  Create Reference
#    Location Should Be  ${NEW_REFERENCE_URL}
#    Select From List By Value  id=entry_type  book
#    Input Text  year  2025
#    Location Should Be  ${NEW_REFERENCE_URL}

    
