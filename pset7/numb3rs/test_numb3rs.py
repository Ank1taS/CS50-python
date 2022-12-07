from numb3rs import validate
import pytest

def test_format():
    assert validate("127.0.0.1") == True
    assert validate("1.2.3.1000") == False
    assert validate("255.") == False
    assert validate("255.255.") == False
    assert validate("255.255") == False

    assert validate("cat") == False

def test_range():
    assert validate("100.100.100.100") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("255.355.255.255") == False
    assert validate("1000.1000.1000.1000") == False
    
