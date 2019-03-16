Feature: Registration for course

  Scenario: Register for chosen course
     Given course information
        | name             | data     |
        | Programming      | 02.03.19 |
     And  application form
        | name           | password | e-mail       |
        | Kate           | qwe123   | abc@mail.ru  |
    When we registrate for courses in "Programming"
    Then we start first lesson
