from tree import BodyBlock, CodeBlock, IfBlock

def test_code_block():
    c = CodeBlock(1, 0)
    c.end = 10
    assert c.to_dict() == {
        "CodeBlock" : {
            "start" : 1,
            "end" : 10
        }
    }

def test_body_block():
    b = BodyBlock(1, 0)
    b.end = 10

    c1 = CodeBlock(1, 0)
    c1.end = 4
    b.add_same_level_block(c1)

    c2 = CodeBlock(5, 0)
    c2.end = 10
    b.add_same_level_block(c2)

    assert b.to_dict() == {
        "BodyBlock" : {
            "start" : 1,
            "end" : 10,
            "body" : [
                {
                    "CodeBlock": {
                        "start" : 1,
                        "end" : 4
                    }
                },
                {
                    "CodeBlock" : {
                        "start" : 5,
                        "end" : 10
                    }
                }
            ]
        }
    }

def test_if_block_lone():
    i = IfBlock(1, 0)
    i.end = 20
    assert i.to_dict() == {
        "IfBlock": {
            "start" : 1,
            "end" : 20,
            "body" : [],
            "elifs" : [],
            "else" : None
        }
    }

def test_if_block_nested():
    spaces = 4

    level_2 = IfBlock(2, spaces * 2)
    level_2.end = 3

    level_1 = IfBlock(1, spaces * 1)
    level_1.end = 3
    level_1.add_same_level_block(level_2)

    root = BodyBlock(1, 0)
    root.end = 3
    root.add_same_level_block(level_1)

    assert root.to_dict() == {
        "BodyBlock" : {
            "start" : 1,
            "end" : 3,
            "body" : [
                {
                    "IfBlock" : {
                        "start" : 1,
                        "end" : 3,
                        "elifs" : [],
                        "else" : None,
                        "body" : [
                            {
                                "IfBlock" : {
                                        "start" : 2,
                                        "end" : 3,
                                        "body" : [],
                                        "elifs" : [],
                                        "else" : None
                                }
                            } 
                        ]
                    }
                }
            ]
        }
    }
