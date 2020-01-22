input_str = input()

result = input_str[:2] + input_str[-2:] if len(input_str) >= 2 else 'Empty string'

print(result)