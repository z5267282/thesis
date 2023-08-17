import helper

def test_get_stripped_line_all_whitespace():
    whitespace = "     "
    assert helper.get_stripped_line(whitespace) == ""

def test_get_leading_whitespace():
    # 4 space bars
    string = "    hello"
    space = helper.get_leading_whitespace(string)
    assert space == "    "
