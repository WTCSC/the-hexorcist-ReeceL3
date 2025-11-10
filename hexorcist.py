DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(number_string: str, original_base: int) -> int:
    total_value = 0
    power = 0

    # Ensure all input characters are uppercase for consistent lookup in DIGITS
    # and iterate through the string in reverse (right to left)
    for char in number_string.upper()[::-1]:

        # Find the decimal value of the digit using the DIGITS string (the decoder ring)
        try:
            char_value = DIGITS.index(char)
        except ValueError:
            # Handle non-existent characters (like symbols)
            raise ValueError(f"Invalid character '{char}' in number string.")

        # Check if the digit is actually valid for the given base (e.g., 'G' is invalid in base 16)
        if char_value >= original_base:
            raise ValueError(f"Invalid digit '{char}' for base {original_base}.")

        # Calculate the positional value and add to the total:
        # total_value += (char_value * (original_base ^ power))
        total_value += char_value * (original_base ** power)

        # Increment the positional power
        power += 1

    return total_value

def from_decimal(decimal_number: int, target_base: int) -> str:
    # Handle the edge case where the number is zero
    if decimal_number == 0:
        return '0'

    result_string = ""

    # Loop while there is still a number to convert 
    while decimal_number > 0:
        #  Find the remainder 
        remainder = decimal_number % target_base

        #  Convert the remainder (0-35) into its corresponding character (0-Z)
        char_to_add = DIGITS[remainder]

        
        result_string = char_to_add + result_string

        # 4. Find the "leftovers" for the next loop iteration (integer division)
        decimal_number = decimal_number // target_base

    return result_string

def main():
    print("\n WELCOME TO THE HEXORCIST I SHALL CONVERT BASES FOR YOU!")

    try:
        # Ask the user for the number string (e.g., "C7")
        number_string = input("Enter the number you are converting: ").strip()

        #Ask for the original base (e.g., 16)
        # Note: We use int(string) without the second argument, as per the rules.
        original_base_str = input("Enter the number's current base (2-36): ").strip()
        original_base = int(original_base_str)

        #Ask for the target base (e.g., 2)
        target_base_str = input("Enter the new base you want (2-36): ").strip()
        target_base = int(target_base_str)

        #Basic Base validation
        if not (2 <= original_base <= 36 and 2 <= target_base <= 36):
            print("\nError: Bases must be between 2 and 36, inclusive.")
            return

        print("\n...calculating your new base")

        #Call your to_decimal function.
        decimal_value = to_decimal(number_string, original_base)

        #Call your from_decimal function.
        converted_string = from_decimal(decimal_value, target_base)

        #Print the final, glorious, hand-made result.
        original_base_label = f"(Base-{original_base})"
        target_base_label = f"(Base-{target_base})"

        #We use the original string input for the final message, as shown in the example run
        print(f"\n'{number_string.upper()}' {original_base_label} is '{converted_string}' {target_base_label}.")

    except ValueError as e:
        print(f"\nAn error occurred during conversion: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()