Feature: IsPangram

  Scenario: IsPangram, abc
    When abc
    Then not a pangram

  Scenario: IsPangram, pack my box with dozen liquor jugs
    When pack my box with dozen liquor jugs
    Then not a pangram

  Scenario: IsPangram,
    When pack my box with five dozen liquor jugs
    Then is pangram

  Scenario: IsPangram, the quick brown fox jumps over the lazy dog
    When the quick brown fox jumps over the lazy dog
    Then is pangram

  Scenario: IsPangram, none
    When word is none
    Then error

  Scenario: IsPangram, ()
    When arg is the wrong type
    Then error

  Scenario: IsPangram, ""
    When word is empty
    Then empty word

  Scenario: IsPangram, 1
    When word is int
    Then error

