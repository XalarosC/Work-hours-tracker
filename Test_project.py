from project import validate_date_format, validate_time_format, calculate_total_hours

def test_validate_date_format():
    assert validate_date_format("01/01") == True
    assert validate_date_format("32/01") == False

def test_validate_time_format():
    assert validate_time_format("12:00") == True
    assert validate_time_format("25:00") == False

def test_calculate_total_hours():
    with open("test_work_hours.txt", "w") as file:
        file.write("01/12 08:00 12:00\n")
        file.write("01/12 13:30 17:45\n")

    result = calculate_total_hours("test_work_hours.txt")
    assert result == 8.25

    import os
    os.remove("test_work_hours.txt")
