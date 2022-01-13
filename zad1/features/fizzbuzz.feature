Feature: FizzBuzz

  Scenario: FizzBuzz, 3
    Given FizzBuzz game
    When 3
    Then Fizz

    Scenario: FizzBuzz, 5
      Given FizzBuzz game
      When 5
      Then Buzz

    Scenario: FizzBuzz, 15
      Given FizzBuzz game
      When 15
      Then FizzBuzz

    Scenario: FizzBuzz, 7
      Given FizzBuzz game
      When 7
      Then 7

    Scenario: FizzBuzz, 20
      Given FizzBuzz game
      When 20
      Then Buzz