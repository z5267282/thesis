from tree_parser import parse

def test_simple_if():
    def if_block():
        i = 0
        if i % 2 == 0:
            print("even")

    root = parse(if_block)
    print(root.pretty_print())
    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 93,
            "end"   : 95,
            "body"  : [
                {
                    "CodeBlock" : {
                        "start" : 93,
                        "end"   : 93
                    }
                },
                {
                    "IfBlock" : {
                        "start" : 94,
                        "end"   : 95,
                        "body" : [
                            {
                                "CodeBlock" : {
                                    "start" : 95,
                                    "end" : 95
                                }
                            }
                        ],
                        "elifs" : [],
                        "else"  : None
                    }
                }
            ]
        }
    }
