#import twttr form shorten fun..
from twttr import shorten

#fun..for upper and lower test
def test_upper_lower_cases():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwItTeR") == "TwtTR"

#fun..for upper and lower test
def test_numbers():
    assert shorten("12345") == "12345"

#fun..for upper and lower test
def test_punction():
    assert shorten("!?.,") == "!?.,"
