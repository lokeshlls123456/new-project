def lower_case_count(s: str, n: int) -> str:
    # Use a list comprehension to collect all lowercase letters
    lowercase_letters = ''.join([char for char in s if char.islower()])
    lowercase_count = len(lowercase_letters)
    
    # Return the formatted result
    return f"{lowercase_letters} {lowercase_count}"

# Sample Input
input1 = "This is A Test STRING with LOwer Case"
input2 = 37
result = lower_case_count(input1, input2)
print(result)