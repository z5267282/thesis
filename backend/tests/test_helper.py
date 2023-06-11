import helper

def test_get_stripped_line_all_whitespace():
    whitespace = "     "
    assert helper.get_stripped_line(whitespace) == ""
