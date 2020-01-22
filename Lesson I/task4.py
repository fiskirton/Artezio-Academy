str_lst = ['abc', 'xyx', 'aba', '1221', 'olopolo']

result = len(list(filter(lambda x: len(x) >= 2 and x[0] == x[-1], str_lst)))

print(result)