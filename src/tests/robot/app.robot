*** Settings ***
Resource  resource.robot
Library   AppLibrary
Test Setup  Add Reading Tip

*** Test Cases ***
Add Reading Tip With Valid Title And Link
    Input Add Reading Tip Command
    Input    Tirakirja
    Input    https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/
    Input    Laaksonen
    Input    Tietokanta ja algoritmi kurssin materiaali
    Input    kommentti_testi
    Input Exit Command
    Run Application
    Output Should Contain    New Reading Tip added!

Search Reading Tip By Title
    Input Search For Reading Tip Command
    Input  Kirja1
    Input Exit Command
    Run Application
    Output Should Contain  1 reading tips found:

Modify Existing Reading Tip
    Input Modify Reading Tip Command
    Input    1
    Input    Kirja2
    Input Exit Command
    Run Application
    Output Should Contain    Modification done successfully.

Delete Existing Reading Tip
    Input Delete Reading Tip Command
    Input    1
    Input Exit Command
    Run Application
    Output Should Contain    Deleting a Reading Tip with tip id 1 done successfully.

*** Keywords ***
Add Reading Tip
    Create Reading Tip  Kirja1   Linkki1



