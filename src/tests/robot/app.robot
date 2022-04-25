*** Settings ***
Resource  resource.robot
Library   AppLibrary
Library    ../../AppLibrary.py
Test Setup  Add Reading Tip

*** Test Cases ***
Add Reading Tip With Valid Title
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

Add Reading Tip With Invalid Title
    Input Add Reading Tip Command
    Input    \
    Input    \
    Input    \
    Input    \
    Input    \
    Input    \
    Input Exit Command
    Run Application
    Output Should Contain    Reading tip cannot have a empty title!

Search Reading Tip By Valid Title
    Input Search For Reading Tip Command
    Input  Kirja1
    Input Exit Command
    Run Application
    Output Should Contain  1 reading tips found:
    Table Row Count Should Be  1

Search Reading Tip By Almost Valid Title
    Input Search For Reading Tip Command
    Input  Krja1
    Input Exit Command
    Run Application
    Output Should Contain  1 reading tips found:
    Table Row Count Should Be  1

Search Reading Tip By Invalid Title
    Input Search For Reading Tip Command
    Input  NonExistent
    Input Exit Command
    Run Application
    Output Should Contain  No reading tips found for title query "NonExistent".
    Input Search For Reading Tip Command
    Input  JokuToinen
    Input Exit Command
    Run Application
    Output Should Contain  No reading tips found for title query "JokuToinen".

Modify Existing Reading Tip
    Input Modify Reading Tip Command
    Input    1
    Input    Kirja2
    Input Exit Command
    Run Application
    Output Should Contain    Modification done successfully.

Modify Nonexisting Reading Tip
    Input Modify Reading Tip Command
    Input    10000
    Input Exit Command
    Run Application
    Output Should Contain    Reading tip with id 10000 was not found.

Delete Existing Reading Tip
    Input Delete Reading Tip Command
    Input    1
    Input Exit Command
    Run Application
    Output Should Contain    Deleting a Reading Tip with tip id 1 done successfully.

Delete Nonexistent Reading Tip
    Input Delete Reading Tip Command
    Input    100
    Input Exit Command
    Run Application
    Output Should Contain    Reading tip with id 100 was not found.

See All Reading Tips
    Create Reading Tip  Kirja3
    Input See Reading Tips Command
    Input Exit Command
    Run Application
    Output Should Contain    4 reading tips found:
    Table Row Count Should Be  4

Add Tags To Reading Tip
    Input Add Tags to Reading Tip Command
    Input  1
    Input  tag_testi
    Input Exit Command
    Run Application
    Output Should Contain    Tag tag_testi was added successfully to tip id 1.

Add Tags To Nonexistent Reading Tip
    Input Add Tags to Reading Tip Command
    Input  10000
    Input Exit Command
    Run Application
    Output Should Contain    Reading tip with id 10000 was not found.

Add Tag 
    Input Add Tag Command
    Input  new_tag
    Input Exit Command
    Run Application
    Output Should Contain    New tag added

Existing Tag Is Not Added Again
    Input Add Tag Command
    Input  new_tag
    Input Add Tag Command
    Input  new_tag
    Input Exit Command
    Run Application
    Output Should Contain   Tag already existed

See All Tags
    Input Add Tag Command
    Input  new_tag
    Input Add Tag Command
    Input  another_tag
    Input See Tags Command
    Input Exit Command
    Run Application
    Output Should Contain    2 tags found:

See Reading Tips With Tag
    Input Add Tags to Reading Tip Command
    Input  1
    Input  tag_testi
    Input See All Reading Tips With Tag Command
    Input  tag_testi
    Input Exit Command
    Run Application
    Output Should Contain  1 reading tips found:
    Table Row Count Should Be  1

Mark Valid Reading Tip As Read
    Input Mark As Read Command
    Input  1
    Input Exit Command
    Run Application
    Output Should Contain  Reading tip status changed to 'Already read!'

Mark Invalid Reading Tip As Read
    Input Mark As Read Command
    Input  100
    Input Exit Command
    Run Application
    Output Should Contain  Reading tip with id 100 was not found.

See All Unread Tips
    Input See Unread Reading Tips Command
    Input Exit Command
    Run Application
    Output Should Contain  Following reading tips are unread.
    Table Row Count Should Be  3
    Input Mark As Read Command
    Input  1
    Input See Unread Reading Tips Command
    Input Exit Command
    Run Application
    Table Row Count Should Be  2

Print Unread Tips When Program Is Started
    Input Exit Command
    Run Application
    Output Should Contain  3 reading tips found:
    Table Row Count Should Be  3

User Cannot Give Command That Does Not Exist
    Input  100
    Input Exit Command
    Run Application
    Output Should Contain  No operation found for given number "100"!

User Cannot Give Command That Is Not Integer
    Input  command
    Input Exit Command
    Run Application
    Output Should Contain  Command should be an integer

*** Keywords ***
Add Reading Tip
    Create Reading Tip  Kirja1
    Create Reading Tip  Video
    Create Reading Tip  Book1
