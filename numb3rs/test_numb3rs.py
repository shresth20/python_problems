from numb3rs import validate

def main():
    test_format()
    test_range()
    test_charter()

def test_format():
    assert validate("111.111.111.111") == True
    assert validate("111.111.111") == False
    assert validate("111.111") == False
    assert validate("111") == False
    assert validate("") == False

def test_range():
    assert validate("555.111.111.111") == False
    assert validate("111.555.111.111") == False
    assert validate("111.111.555.111") == False
    assert validate("111.111.111.555") == False
    assert validate("555.555.555.555") == False


def test_charter():
    assert validate("aaa.bbb.ccc.ddd") == False
    assert validate("yoo") == False

if __name__  == "__main__" :
    main()