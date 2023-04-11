# Define a class named Solution
class Solution:
    # Define a method named isHappy which takes an integer argument n and returns a boolean value
    def isHappy(self, n: int) -> bool:
        # Initialize an empty list named 'numbers' to store the intermediate numbers during the process
        numbers = []
        
        # Continue the loop until n becomes 1
        while n != 1:
            # If n is already present in the list 'numbers', it means the process is looping endlessly,
            # and n is not a happy number, so return False
            if n in numbers:
                return False
            
            # Append the current value of n to the list 'numbers'
            numbers.append(n)
            
            # Initialize a variable named 'total' to store the sum of the squares of the digits of n
            total = 0
            
            # While n is greater than 0, continue extracting its digits and updating 'total'
            while n:
                # Extract the last digit of n using modulo operator
                temp = n % 10
                
                # Update n by removing the last digit using integer division
                n = n // 10
                
                # Add the square of the extracted digit to the variable 'total'
                total += temp * temp
            
            # Update n with the calculated sum of the squares of its digits
            n = total
        
        # If the loop terminates because n becomes 1, it means n is a happy number, so return True
        return True