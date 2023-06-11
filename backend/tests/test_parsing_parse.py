from parser import parse

def test_no_indentation():
    def simple():
        i = 0
        print(i)
    
    root = parse(simple)
    root.pretty_print()
    assert root.to_dict() == {
        "BodyBlock" : {
            "start": 2,
            "end"  : 3,
            "body" : [
                {
                    "CodeBlock" : {
                        "start": 2,
                        "end"  : 3
                    }
                }
            ]
        }
    }
