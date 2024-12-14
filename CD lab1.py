def analyze_code(sen):
    keywords = {
        'and', 'as', "assert", 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
        'except', 'false', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lamda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
    }

    identifiers = []
    operators = []
    constants = []
    found_keyword = []
    current_token = ""
    for char in sen:
        if char.isalnum() or char == '_':
            current_token += char

        elif char.isspace():
            if current_token:
                if current_token.isdigit():
                    constants.append(current_token)
                elif current_token in keywords:
                    found_keyword.append(current_token)
                else:
                    identifiers.append(current_token)
                current_token = ''

        elif char in "+-*/%=":
            operators.append(char)
            if current_token:
                if current_token.isdigit():
                    constants.append(current_token)

                else:
                    identifiers.append(current_token)
                current_token = ''
        else:
            if current_token:
                if current_token.isdigit():
                    constants.append(current_token)
                else:
                    identifiers.append(current_token)
                current_token = ''
    if current_token:
        if current_token.isdigit():
            constants.append(current_token)
        elif current_token in keywords:
            found_keyword.append(current_token)
        else:
            identifiers.append(current_token)
    return identifiers, operators, constants, found_keyword


sen = "my True name is Mahendra and My_mobile num is 3652148955 but i use my laptop todo programming in my class "
result = analyze_code(sen)
print("identifiers:", result[0])
print("operators:", result[1])
print("constants:", result[2])
print("keywords:", result[3])
a = len(result[0])
print("Total no of identifiers:", a)
b = len(result[1])
print("Total no of operators:", b)
c = len(result[2])
print("Total no of constants:", c)
d = len(result[3])
print("Total no of keywords:", d)

e = (a + b + c + d)
print("Total number of tokens :", e)