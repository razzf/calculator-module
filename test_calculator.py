import pytest

from calculator import Calculator


def test_init():
    # Test instantiation
    calculator = Calculator()
    assert calculator.memory == 0


def test_str():
    # Test __str__ method
    calculator = Calculator()
    assert str(calculator) == "Calculator with current memory: 0.0"
    calculator.add(3)
    assert str(calculator) == "Calculator with current memory: 3.0"
    calculator.divide(2)
    assert str(calculator) == "Calculator with current memory: 1.5"


def test_addition():
    # Test addition function
    calculator = Calculator()
    assert calculator.add(4) == 4
    calculator.add(4)
    assert calculator.memory == 8
    assert calculator.add(-3) == 5 
    assert calculator.memory == 5
    calculator.add(1.5)
    assert calculator.memory == 6.5
    calculator.add(0)
    assert calculator.memory == 6.5
 

def test_subtraction():
    # Test subtratction function
    calculator = Calculator()
    calculator.subtract(4)
    assert calculator.memory == -4
    calculator.subtract(0.54)
    assert calculator.memory == -4.54
    calculator.subtract(-0.54)
    assert calculator.memory == -4
 
 
def test_multiplication():
    # Test multiplication function
    calculator = Calculator()
    calculator.multiply(1)
    assert calculator.memory == 0
    calculator.add(4)
    calculator.multiply(2)
    assert calculator.memory == 8
    calculator.multiply(-0.5)
    assert calculator.memory == -4
    calculator.multiply(0)
    assert calculator.memory == 0
  
 
def test_division():
    # Test division function
    calculator = Calculator()
    calculator.divide(1)
    assert calculator.memory == 0
    calculator.add(4)
    calculator.divide(2)
    assert calculator.memory == 2
    calculator.divide(-0.5)
    assert calculator.memory == -4

def test_division_error():
    # Test division by zero
    with pytest.raises(ZeroDivisionError):
        calculator = Calculator()
        calculator.divide(0) 

def test_root():
    # Test root function
    calculator = Calculator()
    calculator.root(1)
    assert calculator.memory == 0
    calculator.add(4)
    calculator.root(2)
    assert calculator.memory == 2
    calculator.root(-0.5)
    assert calculator.memory == 0.25
    calculator.root(0.5)
    assert calculator.memory == 0.0625 

    # Test valid negative odd root
    calculator.memory = -8
    calculator.root(-3)
    assert calculator.memory == -0.5
    # Test valid negative odd root
    calculator.memory = 8
    calculator.root(-3)
    assert calculator.memory == 0.5
    # Test valid negative odd root
    calculator.memory = 16
    calculator.root(-4)
    assert calculator.memory == 0.5

def test_root_error1():
    # Test zero root error
    with pytest.raises(ValueError):
        calculator = Calculator()
        calculator.root(0) 

def test_root_error2():
    # Test negative even root error
    with pytest.raises(ValueError):
        calculator = Calculator(-16)
        calculator.root(-4)
 
def test_reset():
    # Test reset function
    calculator = Calculator()
    calculator.add(999)
    calculator.reset()
    assert calculator.memory == 0


def test_setter_error():
    # Test memory value assignment error
    with pytest.raises(TypeError):
        calculator = Calculator()
        calculator.memory = "teststring" 


def test_setter():
    # Test valid memory value assignment
    calculator = Calculator()
    calculator.memory = 6.0
    assert calculator.memory == 6.0
    calculator.memory = -455.3
    assert calculator.memory == -455.3


def test_setter_round_digit():
    # Test valid round_digit value assignment
    calculator = Calculator(round_digit=15)
    calculator.round_digit = 1


def test_setter_round_digit_error():
    # Test round_digit value assignment error
    with pytest.raises(ValueError):
        calculator = Calculator(round_digit=17)