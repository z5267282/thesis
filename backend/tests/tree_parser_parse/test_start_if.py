from tree_parser import parse

def test_start_if():
    def start_if():
        if True:
            print("yes")
    
    root = parse(start_if)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 5,
            "end" : 6,
            "body" : [
                {
                    "IfBlock" : {
                        "start" : 5,
                        "end" : 6,
                        "body" : [
                            {
                                "CodeBlock" : {
                                    "start" : 6,
                                    "end" : 6
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
