from grading import calculate_grade

def test_grade_a():
    assert calculate_grade(85) == "A"

def test_grade_b():
    assert calculate_grade(75) == "B"

def test_grade_c():
    assert calculate_grade(65) == "C"

def test_grade_f():
    assert calculate_grade(40) == "F"

def test_invalid_marks():
    assert calculate_grade(110) == "Invalid marks"
