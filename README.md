# StarWarsAPITestAutomation

###### This is [InterviewKickstart](https://uplevel.interviewkickstart.com/) Test Engineering course assignment implementation.

---------------------------------------------------------------
#### Assignment:

Visit the Star Wars API https://swapi.dev/ and the documentation https://swapi.dev/documentation

#### Expectation :

Create a framework with the tools and technologies of your choice.
Each validation is to be performed as a separate test.
At the end of the test execution, the framework should generate a report with the number of tests and their corresponding execution status.
Perform the following validations:

* Verify that the “people” endpoint is returning a successful response. 

* Verify that the total number of people where height is greater than 200 matches the expected count (10 at the time this was assigned).

* Verify that the ten individuals returned are:
Darth Vader, Chewbacca, Roos Tarpals, Rugor Nass, Yarael Poof, Lama Su, Tuan Wu, Grievous, Tarfful, Tion Medon

* Verify that the total number of people checked equals the expected count (82 at the time)

#### Bonus points for : 

Additional validations if you can add on “people” API
Additional API if you can test from the star wars collection as shown below.

{

    "films": "https://swapi.dev/api/films/",

    "people": "https://swapi.dev/api/people/",

    "planets": "https://swapi.dev/api/planets/",

    "species": "https://swapi.dev/api/species/",

    "starships": "https://swapi.dev/api/starships/",

    "vehicles": "https://swapi.dev/api/vehicles/"

}

---------------------------------------------------------------


The assignment implemented using **Python**, **Behave** as BDD tool, **Allure** for reports.

#### Run tests

To run tests use:

``` behave -f allure_behave.formatter:AllureFormatter -o allure-report ```

To generate test reports:

``` allure serve .\allure-report\ ```
