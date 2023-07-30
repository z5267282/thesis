from tree_parser import parse

def test_while_whole_program():
    """Note this test will break the program rules.
    There is no other way to write a program which is entirely a while."""
    while True:
        password = "fish"
        guess = input("enter password: ")
        if guess == password:
            print("access granted!")
            break

def test_while_whole_program():
    root = parse(test_while_whole_program)
    assert root == {
        "BodyBlock" : {
            "start" : 6,
            "end"   : 11,
            "body"  : [
                {
                    "WhileBlock" : {
                        "start" : 6,
                        "end"   : 11,
                        "body"  : [
                            {
                                "CodeBlock" : {
                                    "start" : 7,
                                    "end"   : 8
                                }
                            },
                            {
                                "IfBlock" : {
                                    "start" : 9,
                                    "end"   : 11,
                                    "body"  : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 10,
                                                "end"   : 11
                                            }
                                        }
                                    ]
                                }
                            }
                        ],
                        "elifs" : [],
                        "else" : None
                    }
                }
            ]
        }
    }
