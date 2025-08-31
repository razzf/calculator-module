# Calculator Module

![python_badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Overview

The Calculator module provides a python class for performing basic arithmetic operations and managing memory. It supports addition, subtraction, multiplication, division, and taking the n-th root of a number. Additionally, it includes methods for resetting the memory and handles floating point errors through rounding.

## Features

- **Addition**: Adds a number to the memory.
- **Subtraction**: Subtracts a number from the memory.
- **Multiplication**: Multiplies the memory by a number.
- **Division**: Divides the memory by a number and handles division by zero.
- **Root**: Takes the n-th root of the memory.
- **Reset**: Resets the memory to 0.0.


- ***Rounding***: Rounds results to a specified number of decimal places to handle floating point errors.

## Installation

To install the Calculator module, you can simply clone the repository:

```bash
git clone https://github.com/TuringCollegeSubmissions/jwerne-DS.v3.1.2.5.git
```

## Usage

Here is a basic example of how to use the Calculator class:

```python
from calculator import Calculator

# Create an instance of the Calculator class
calc = Calculator()

# Perform operations
result_add = calc.add(5)          # Adds 5 to memory
result_subtract = calc.subtract(3) # Subtracts 3 from memory
result_multiply = calc.multiply(2) # Multiplies memory by 2
result_divide = calc.divide(4)    # Divides memory by 4
result_root = calc.root(2)        # Takes the square root of memory
result_reset = calc.reset()       # Resets memory to 0.0

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)
print(result_root)
print(result_reset)


# Change the rounding precision in terms of number of decimals (default: 10),
# ..while creating the instance
calc = Calculator(round_digit=20)
# ..or in an existing instance
calc.round_digit = 5

```

## API Reference

### `add(addend: Union[int, float]) -> float`

Adds the given number to the memory and returns the new memory value.

- **Parameters:**
  - `addend` (Union[int, float]): The number to add to memory.
- **Returns:**
  - `float`: The new memory value.

### `subtract(subtrahend: Union[int, float]) -> float`

Subtracts the given number from the memory and returns the new memory value.

- **Parameters:**
  - `subtrahend` (Union[int, float]): The number to subtract from memory.
- **Returns:**
  - `float`: The new memory value.

### `multiply(multiplicand: Union[int, float]) -> float`

Multiplies the memory by the given number and returns the new memory value.

- **Parameters:**
  - `multiplicand` (Union[int, float]): The number to multiply with memory.
- **Returns:**
  - `float`: The new memory value.

### `divide(denominator: Union[int, float]) -> float`

Divides the memory by the given number and returns the new memory value. Raises `ZeroDivisionError` if the denominator is zero.

- **Parameters:**
  - `denominator` (Union[int, float]): The number to divide memory by.
- **Returns:**
  - `float`: The new memory value.
- **Raises:**
  - `ZeroDivisionError`: If the denominator is zero.

### `root(n: Union[int, float]) -> float`

Takes the n-th root of the memory and returns the new memory value. Raises `ValueError` if `n` is zero, or if the memory is negative and `n` is even.

- **Parameters:**
  - `n` (Union[int, float]): The degree of the root.
- **Returns:**
  - `float`: The new memory value.
- **Raises:**
  - `ValueError`: If `n` is zero, or if the memory is negative and `n` is even.

### `reset() -> float`

Resets the memory to 0.0 and returns the new memory value.

- **Returns:**
  - `float`: The new memory value.

## Error Handling

The Calculator module handles errors gracefully:

- **Division by zero** raises a `ZeroDivisionError`.
- **Invalid root operations** raise a `ValueError` when attempting to take the 0th root or the root of a negative number with an even degree.
- **Invalid types** for memory and rounding digits raise `TypeError`.

## Contact
Joachim Werner

Email: joachim_werner@gmx.de

GitHub: [RazzF](https://github.com/razzf)