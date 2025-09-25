def perform_operation(num1, num2, operation):
    result =0
    if operation == 'add':
        result = float(num1) + float(num2)
    elif operation == 'subtract':
        result= float(num1) - float(num2)
    elif operation == 'multiply':
        result= float(num1) * float(num2)
    elif operation == 'divide':
        if float(num2) == 0:
            return "Error: Division by zero"
        result = float(num1) / float(num2)
    else:
        return "Error: Invalid operation"
    return result
    
