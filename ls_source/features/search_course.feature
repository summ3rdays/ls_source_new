Feature: Completing tests

  Scenario: Passing test during course
     Given current test
        | theme                 | # of questions | points |
        | Basic of programming  |       10       |   30   |
        | Python functions      |       10       |   40   |
        | Pandas                |       10       |   30   |
     #And  a set of questions
     #   | theme_id | question_name  | points |
     #   |   3      | Python_1       | 5      |
     #   |   3      | Python_2       | 15     |
     #   |   3      | Python_3       | 10     |
      And a student answers
        | student_id | theme_id | question_id  | points |
        |    4545    |    3     |     1        |    5   |
        |    4545    |    3     |     2        |    10  |
        |    4545    |    3     |     3        |    15  |
        |    4545    |    3     |     4        |    5   |
    When we pass the test in
    Then we get the result for the 1 theme
