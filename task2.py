import requests

API_ENDPOINT = 'https://api.mathjs.org/v4/'

def evaluate_expression(expression):
    response = requests.get(API_ENDPOINT, params={'expr': expression})
    if response.status_code == 200:
        result = response.text.strip()
        return result
    else:
        return None

expressions = []
print("Enter the mathematical expressions (type 'end' to finish):")
while True:
    expression = input()
    if expression == 'end':
        break
    expressions.append(expression)

print("Evaluating expressions...")

for expression in expressions:
    result = evaluate_expression(expression)
    if result is not None:
        print(f"{expression} => {result}")
    else:
        print(f"Failed to evaluate {expression}")

