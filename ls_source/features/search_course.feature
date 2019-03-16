Feature: Searching for course

  Scenario: Find courses for some specialization
     Given a set of specializations
        | name             |
        | Programming      |
        | Natural Sciences |
     And  a set of courses
        | name           | price |
        | Java           | 100$  |
        | JavaScript     | 50$   |
        | Biology        | 10$   |
    When we search for courses in "Programming"
    Then we will find 2 Programming items