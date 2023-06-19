from tree_parser import parse

def test_no_nesting():
    def simple():
        i = 0
        print(i)

    root = parse(simple)
    assert root.to_dict() == {
        "BodyBlock" : {
            "start": 5,
            "end"  : 6,
            "body" : [
                {
                    "CodeBlock" : {
                        "start": 5,
                        "end"  : 6 
                    }
                }
            ]
        }
    }
