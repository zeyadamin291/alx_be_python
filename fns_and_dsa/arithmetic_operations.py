def perform_operation(num1, num2, operation):
    result =0
    num1 = float(num1)
    num2 = float(num2)
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result= num1 - num2
    elif operation == 'multiply':
        result= num1 * num2 
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    else:
        return "Error: Invalid operation"
    return result
    
