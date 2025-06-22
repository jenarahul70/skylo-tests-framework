*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://ssd-api.jpl.nasa.gov

*** Test Cases ***

Check What Base URL Is
    [Documentation]    Debug step to verify BASE_URL is set correctly
    Log    BASE_URL = ${BASE_URL}

*** Test Cases ***
Test API Returns Valid Structure
    [Documentation]    Check that response is OK and contains essential top-level keys
    Create Session    nasa    ${BASE_URL}    verify=False
    ${resp}=    GET On Session    nasa    /cad.api
    Log To Console    ${resp}
    Should Be Equal As Integers    ${resp.status_code}    200
    ${json}=    Set Variable    ${resp.json()}
    Should Contain    ${json.keys()}    signature
    Should Contain    ${json.keys()}    count
    Should Contain    ${json.keys()}    data


Test API Data Count Matches Entries
    [Documentation]    Validate that count matches length of returned data array
    Create Session    nasa    ${BASE_URL}    verify=False
    ${resp}=      GET On Session    nasa    /cad.api

    # Store the parsed JSON dictionary
    ${json}=      Set Variable      ${resp.json()}

    # Convert the “count” field to an integer (safer than Evaluate)
    ${count}=     Convert To Integer    ${json['count']}

    # Store the data list as–is (no Evaluate needed)
    ${data}=      Set Variable      ${json['data']}

    # Compare list length with the declared count
    Length Should Be    ${data}    ${count}
