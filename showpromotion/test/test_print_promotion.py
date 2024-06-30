# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Paweesuda Thippayanasa ปวีณ์สุดา ทิพยนาสา
# Student ID: 653380137-5


import pytest
from source.print_promotion import print_promotion

@pytest.mark.parametrize("total_cost, expected_output", [
    (0, "Thank you and see you next time"),
    (150, "Thank you and see you next time"),
    (300, "Thank you and see you next time"),
    (499, "Thank you and see you next time"),
    (500, "Free ice cream cone = 1"),
    (550, "Free ice cream cone = 1"),
    (600, "Free ice cream cone = 1"),
    (699, "Free ice cream cone = 1"),
    (700, "Free chocolate cake = 1"),
    (750, "Free chocolate cake = 1"),
    (800, "Free chocolate cake = 1"),
    (999, "Free chocolate cake = 1"),
    (1200, "Free ice cream cone = 1 and Free chocolate cake = 1"),
    (1250, "Free ice cream cone = 1 and Free chocolate cake = 1"),
    (1300, "Free ice cream cone = 1 and Free chocolate cake = 1"),
    (1399, "Free ice cream cone = 1 and Free chocolate cake = 1"),
    (2400, "Free ice cream cone = 2 and Free chocolate cake = 2"),
    (2500, "Free ice cream cone = 2 and Free chocolate cake = 2"),
    (2600, "Free ice cream cone = 2 and Free chocolate cake = 2"),
    (2699, "Free ice cream cone = 2 and Free chocolate cake = 2"),
    (3500, "Free ice cream cone = 2 and Free chocolate cake = 3"),
    (3600, "Free ice cream cone = 2 and Free chocolate cake = 3"),
    (3700, "Free ice cream cone = 2 and Free chocolate cake = 3"),
    (3799, "Free ice cream cone = 2 and Free chocolate cake = 3"),
    (-5, "Error/Invalid Input"),
    ("5 hundred", "Error/Invalid Input"),
    
])
def test_print_promotion(total_cost, expected_output):
    result = print_promotion(total_cost)
    assert result == expected_output

