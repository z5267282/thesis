def program():
    i = 1
    twos, fives = 0, 0
    while i < 6:
        if i % 2 == 0:
            print("two")
            twos += 1
        elif i % 5 == 0:
            print("five")
            fives += 1
    
        j = 0
        while j < i:
            print("X", end="")
            j += 1
    
        i += 1
    
    print(f"2s: {twos}, 5s: {fives}")

from generate import generate_dataframes

def test_counters():
    dataframes = generate_dataframes(program)
    assert len(dataframes) >= 3
    start, top_level, while_ = dataframes[:3]
    assert len(start.counters) == 0
    assert start.lines == ["1", "2", "3", "", "18"]
    assert start.path == []

    assert len(top_level.counters) == 0
    assert top_level.lines == ["1", "2", "3", "", "18"]
    assert top_level.path == [1]

    assert while_.lines == ["1", "2", "3", "", "18"]
    assert while_.path == [1, 2]

    assert len(while_.counters) == 1
    counter, = while_.counters
    print(counter.start, counter.end)
    print(repr(counter))
    assert not counter.has_valid_range()
