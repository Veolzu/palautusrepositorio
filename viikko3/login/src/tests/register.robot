*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Registering Page

*** Test Cases ***

Register With Valid Username And Password
# ...
    Set Username  veeti
    Set Password  Veeti5000
    Set Password confirmation  Veeti5000
    Click  button >> text=Register
    Registering Should Succeed
    

Register With Too Short Username And Valid Password
    Set Username  ve
    Set Password  Veeti5000
    Set Password confirmation  Veeti5000
    Click  button >> text=Register
    Registering Should Fail With Message  Username must be at least 3 characters long
Register With Valid Username And Too Short Password
# ...
    Set Username  Veeti
    Set Password  Veeti2
    Set Password confirmation  Veeti2
    Click  button >> text=Register
    Registering Should Fail With Message  Password must be at least 8 characters long
Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Veeti5000
    Set Password confirmation  Veeti5000
    Click  button >> text=Register
    Registering Should Fail With Message  User with username kalle already exists

*** Keywords ***
Registering Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Registering Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Reset Application Create User And Go To Registering Page
    Reset Application
    Create User  kalle  kalle123
    Go To Registering Page
