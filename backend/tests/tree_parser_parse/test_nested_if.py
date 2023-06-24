from tree_parser import parse

def test_nested_if():
    def nested():
        i = 6
        if i % 2 == 0:
            if i % 3 == 0:
                print("multiple of 6")

    root = parse(nested)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end" : 8,
            "body" : [
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end" : 5
                    }
                },
                {
                    "IfBlock" : {
                        "start" : 6,
                        "end" : 8,
                        "elifs" : [],
                        "else" : None,
                        "body" : [
                            {
                                "IfBlock" : {
                                    "start" : 7,
                                    "end" : 8,
                                    "elifs" : [],
                                    "else" : None,
                                    "body" : [
                                        {
                                            "CodeBlock" : {
                                                "start" : 8,
                                                "end" : 8
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }