*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Get User API - Success
    Create Session    mysession    ${BASE_URL}
    ${response}=    GET On Session    mysession    /users/1
    Should Be Equal As Integers    ${response.status_code}    200

Get Invalid User - Fail Case
    Create Session    mysession    ${BASE_URL}
    ${response}=    GET On Session    mysession    /users/9999
    Should Be Equal As Integers    ${response.status_code}    200
