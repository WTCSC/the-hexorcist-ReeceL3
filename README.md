# 🧙 The HEXORCIST: Universal Base Converter (Base 2 to 36)

The HEXORCIST is a Python program designed to convert numbers between any two bases from Base 2 (Binary) up to Base 36. It performs all conversions manually using fundamental arithmetic and iterative algorithms, completely avoiding built-in conversion functions like bin(), hex(), oct(), or the two-argument form of int().

# ✨ Features

    Universal Base Support: Converts numbers between any base from 2 to 36.

    Custom Implementation: All conversion logic (to_decimal and from_decimal) is hand-built using loops and basic math, demonstrating a deep understanding of number systems.

    Robust Input Handling: Includes validation for invalid characters and digits outside the allowed range for the specified base.

# 🚀 How to Run

    Save the Code: Save the provided code as a Python file (e.g., hexorcist.py).

    Execute: Run the file from your terminal:
    Bash

    python hexorcist.py

    Follow the Prompts: The program will guide you through entering the number, its current base, and the desired target base.

# Example Session
```
 WELCOME TO THE HEXORCIST I SHALL CONVERT BASES FOR YOU!
Enter the number you are converting: C7
Enter the number's current base (2-36): 16
Enter the new base you want (2-36): 2

...calculating with 1's and 0's.

'C7' (Base-16) is '11000111' (Base-2).
```

# 🛠️ Core Functions

The program is structured around a "Babel Fish" strategy: all conversions must pass through Base 10 (Decimal) as an intermediate step.

1. to_decimal(number_string: str, original_base: int) -> int

    This function handles Base-N to Base-10 conversion.
```
    Algorithm: Implements the positional notation method.

    It iterates over the input string's digits from right-to-left.

    For each digit, it determines its decimal value (e.g., 'A' = 10) using the DIGITS constant.

    It then calculates the total by summing: (digit_value * original_base ** position_power).
```
2. from_decimal(decimal_number: int, target_base: int) -> str

    This function handles Base-10 to Base-N conversion.
```
    Algorithm: Implements the remainder algorithm.

    It continuously divides the decimal number by the target_base.

    The remainder (%) of each division gives the value of the next digit in the target base. This value is mapped to a character (0-Z) using DIGITS.

    The quotient (//) becomes the number for the next iteration.

    The resulting characters are prepended to the result string in each loop to build the final number in the correct order.
```
# 🔑 Key Constant

    DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" This string serves as the "Decoder Ring" and is crucial for all conversions. It provides a simple lookup table to map decimal values (0-35) to their corresponding characters for bases up to 36.

# 🛑 Forbidden Magic 

This code strictly adheres to a set of rules, ensuring the conversion logic is built from first principles. The following methods are explicitly forbidden and NOT used in this codebase:

    bin(), hex(), oct(), format()

    int(string, base) (The two-argument version of int())