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
    Input    testi_tagi
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

See All Reading Tips
    Create Reading Tip  Kirja3   Linkki3
    Input See Reading Tips Command
    Input Exit Command
    Run Application
    Output Should Contain    2 reading tips found:

See All Reading Tips
    Create Reading Tip  Kirja3   Linkki3
    Input See Reading Tips Command
    Input Exit Command
    Run Application
    Output Should Contain    2 reading tips found:

Add Tags To Reading Tips
    Input Add Tags to Reading Tip Command
    Input  1
    Input  tag_testi
    Input Exit Command
    Run Application
    Output Should Contain    Tag tag_testi was added successfully to tip id 1.

Add Tag 
    Input Add Tag Command
    Input  new_tag
    Input Exit Command
    Run Application
    Output Should Contain    New tag added

See All Tags
    Input Add Tag Command
    Input  new_tag
    Input See Tags Command
    Input Exit Command
    Run Application
    Output Should Contain    New tag added
    Output Should Contain    1 tags found:

*** Keywords ***
Add Reading Tip
    Create Reading Tip  Kirja1   Linkki1



