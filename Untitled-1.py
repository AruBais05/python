import re

def a_followedBy_b(text):
    return bool(re.fullmatch(r'a[b]*', text))

def a_followedBy_conditionB(text):
    return bool(re.fullmatch(r'a[b]{2,3}', text))

def lowercase_with_underscore(text):
    return re.findall(r'\b[a-z]+_[a-z]+\b', text)

def uppercase_followedBy_lowercase(text):
    return re.findall(r'[A-Z][a-z]+', text)

def a_endingWith_b(text):
    return bool(re.fullmatch(r'a.*b$', text))

def replace(text):
    return re.sub(r'[ ,.]+', ':', text)

def snake_to_camel(text):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(text.split('_')))

def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

def spaces_in_camel(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

def camel_to_snake(text):
    return re.sub(r'([A-Z])', r'_\1', text).lower().lstrip('_')

"""with open('row.txt', 'r') as file:
    lines = [line.strip() for line in file]

for line in lines:
    print(f"Match 'a' followed by 'b's: {a_followedBy_b(line)}")
    print(f"a followed by zero or more b\'s: {a_followedBy_conditionB(line)}")
    print(f"lowercase joined with a underscore: {lowercase_with_underscore(line)}")
    print(f"uppercase followed by lowercase: {uppercase_followedBy_lowercase(line)}")
    print(f"a ending with b: {a_endingWith_b(line)}")
    print(f"replace all occurrences: {replace(line)}")
    print(f"snake to camel case: {snake_to_camel(line)}")
    print(f"split at uppercase: {split_at_uppercase(line)}")
    print(f"insert spaces between capital: {spaces_in_camel(line)}")
    print(f"camel to snake case: {camel_to_snake(line)}")     """
    
text= """ OrderID: A123b
Product: apple_juice_bottle
Price: $14.99
DiscountCode: SPRINGSALE2024
Username: CoolCamelCaseUser
UserEmail: user_email_address
TransactionID: T987X
Notes: "Payment confirmed at 3:45pm."
SomeMoreCamelCaseWordsHere
Special offer ends at 12pm, 5pm, or 9pm.
"""
print(f"Match 'a' followed by b\'s: {a_followedBy_b(text)}")
print(f"a followed by zero or more b\'s: {a_followedBy_conditionB(text)}")
print(f"lowercase joined with a underscore: {lowercase_with_underscore(text)}")
print(f"uppercase followed by lowercase: {uppercase_followedBy_lowercase(text)}")
print(f"a ending with b: {a_endingWith_b(text)}")
print(f"replace all occurrences: {replace(text)}")
print(f"snake to camel case: {snake_to_camel(text)}")
print(f"split at uppercase: {split_at_uppercase(text)}")
print(f"insert spaces between capital: {spaces_in_camel(text)}")
print(f"camel to snake case: {camel_to_snake(text)}") 


