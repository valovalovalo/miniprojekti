*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset References

*** Test Cases ***

After Adding A Reference, Site Displays It
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test1
    Input Text  authors  test
    Input Text  year  2000
    Click Button  Create Reference
    Page Should Contain  test1

After Adding A Reference, Site Displays It 2
    Go To  ${HOME_URL}
    Click Link  Create a new reference
    Select From List By Value  id=entry_type  book
    Input Text  title  test2
    Input Text  authors  test2
    Input Text  year  2024
    Click Button  Create Reference
    Page Should Contain  test2

Test Title Sorting
    [Documentation]    Checks, that references are sorted by name
    Go To  ${HOME_URL}
    Maximize Browser Window
    Sort References By Title Ascending
    Verify Sorted By Title Ascending

Test Author Sorting
    [Documentation]    Check that references are sorted by author
    Go To  ${HOME_URL}
    Maximize Browser Window
    Sort References By Authors Ascending
    Verify Sorted By Authors Ascending

Test Year Sorting
    [Documentation]    Checks that references are sorted by year
    Go To  ${HOME_URL}
    Maximize Browser Window
    Sort References By Year Ascending
    Verify Sorted By Year Ascending

*** Keywords ***
Sort References By Title Ascending
    [Documentation]    Click title to sort by title
    Click Element    xpath=//a[contains(text(), 'Title')]

Sort References By Authors Ascending
    [Documentation]    Click authors to sort by author
    Click Element    xpath=//a[contains(text(), 'Authors')]

Sort References By Year Ascending
    [Documentation]    Click year o sort by year
    Click Element    xpath=//a[contains(text(), 'Year')]

Verify Sorted By Title Ascending
    [Documentation]    Verifies, that the references are sorted by title
    ${titles}=    Get WebElements    xpath=//table/tbody/tr/td[1]
    ${previous}=    Set Variable    ${None}
    FOR    ${title}    IN    @{titles}
        Should Be True    ${previous} < ${title.text}    ${previous} < ${title.text}
        Set Variable    ${previous}    ${title.text}
    END

Verify Sorted By Authors Ascending
    [Documentation]    Verifies, that the references are sorted by author
    ${authors}=    Get WebElements    xpath=//table/tbody/tr/td[2]
    ${previous}=    Set Variable    ${None}
    FOR    ${author}    IN    @{authors}
        Should Be True    ${previous} < ${author.text}    ${previous} < ${author.text}
        Set Variable    ${previous}    ${author.text}
    END

Verify Sorted By Year Ascending
    [Documentation]    Verifies, that the references are sorted by year
    ${years}=    Get WebElements    xpath=//table/tbody/tr/td[3]
    ${previous}=    Set Variable    ${None}
    FOR    ${year}    IN    @{years}
        Should Be True    ${previous} < ${year.text}    ${previous} < ${year.text}
        Set Variable    ${previous}    ${year.text}
    END