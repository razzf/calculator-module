from typing import Union


class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations and manage memory.

    This calculator supports the following operations:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Taking the n-th root of a number
    - Resetting memory

    The round() function is used to cope with floating point errors.

    Attributes:
        memory (float): The current value stored in the calculator's memory. 
            Initialized to 0.0.

        round_digit (int): The number of decimals to use when rounding the value. 
            Must be at least 1. Initialized to 10.

    Methods:
        add(addend: Union[int, float]) -> float:
            Adds the given number to the memory and returns the new memory value.

        subtract(subtrahend: Union[int, float]) -> float:
            Subtracts the given number from the memory and returns the new memory value.

        multiply(multiplicand: Union[int, float]) -> float:
            Multiplies the memory by the given number and returns the new memory value.

        divide(denominator: Union[int, float]) -> float:
            Divides the memory by the given number and returns the new memory value. 
            Raises ZeroDivisionError if the denominator is zero.

        root(n: Union[int, float]) -> float:
            Takes the n-th root of the memory and returns the new memory value. 
            Raises ValueError if n is zero.

        reset() -> float:
            Resets the memory to 0.0 and returns the new memory value.
    """


    def __init__(self, memory: float = 0.0, round_digit: int = 10):
        self.round_digit = round_digit
        self._memory: float = 0.0  # Initialize with a default value to ensure type annotation
        self.memory = memory

    def __str__(self):
        """Returns a string representation of the calculator's memory.

        Returns:
            str: The current memory value.
        """
        return f"Calculator with current memory: {self.memory}"

    def add(self, addend: Union[int, float]) -> float:
        """Performs an addition between the current memory and given addend
        Args:
            addend (Union[int, float]): The number to add to memory.

        Returns:
            float: The new memory value.
        """
        self.memory += addend
        return self.memory

    def subtract(self, subtrahend: Union[int, float]) -> float:
        """Performs a subtraction between the current memory and given subtrahend.

        Args:
            subtrahend (Union[int, float]): The number to subtract from memory.

        Returns:
            float: The new memory value.
        """
        self.memory -= subtrahend
        return self.memory

    def multiply(self, multiplicand: Union[int, float]) -> float:
        """Performs a multiplication between the current memory and given multiplicand.

        Args:
            multiplicand (Union[int, float]): The number to multiply with memory.

        Returns:
            float: The new memory value.
        """
        self.memory *= multiplicand
        return self.memory

    def divide(self, denominator: Union[int, float]) -> float:
        """Performs a division between the current memory value and given denominator.

        Args:
            denominator (Union[int, float]): The number to divide memory by.

        Returns:
            float: The new memory value.

        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        if denominator == 0:
            raise ZeroDivisionError("Division by zero is invalid.")
        self.memory /= denominator
        return self.memory

    def root(self, n: Union[int, float]) -> float:
        """Takes the n-th root of the current memory value.

        Args:
            n (Union[int, float]): The degree of the root.

        Returns:
            float: The new memory value.

        Raises:
            ValueError: If roots (n) is zero, or the current memory value is negative 
            and roots (n) is even.
        """
        if n == 0:
            raise ValueError("Taking the 0th root is invalid.")
        if self.memory < 0:
            if n % 2 == 1:
                # For negative memory and odd roots, the result should be real
                self.memory = -((-self.memory) ** (1 / n))
            else:
                raise ValueError(
                    "Taking the n-th root of a negative number, where n is an even number, is invalid"
                )
        else:
            self.memory = self.memory ** (1 / n)
        return self.memory

    def reset(self) -> float:
        """Resets the memory to the initial value of 0.

        Returns:
            float: The new memory value.
        """
        self.memory = float(0)
        return self.memory

    @property
    def memory(self) -> float:
        """Getter for the memory attribute."""
        return self._memory

    @memory.setter
    def memory(self, memory: Union[int, float]):
        """Setter for the memory attribute. Ensures memory is a float number.

        Args:
            memory [float, int]: The new memory value.

        Raises:
            TypeError: If the memory value is not of type float or int.
        """
        if not isinstance(memory, (float, int)):
            raise TypeError(
                "Invalid type of memory value. Value not of type float or int."
            )
        self._memory = round(float(memory), self.round_digit)

    @property
    def round_digit(self) -> int:
        """Getter for the round_digit attribute."""
        return self._round_digit

    @round_digit.setter
    def round_digit(self, round_digit: int):
        """Setter for the round_digit attribute. Ensures memory is an integer number 
        and of value between 1 and 15.

        Args:
            round_digit (int): The new round_digit value.

        Raises:
            TypeError: If the memory value is not of type int.
        """
        if not isinstance(round_digit, int):
            raise TypeError("Invalid type of round_digit value. Value not of type int.")
        elif round_digit < 1 or round_digit > 15:
            raise ValueError(
                "Invalid value for round_digit. Value must be an integer between 1 and 15."
            )
        self._round_digit = int(round_digit)
