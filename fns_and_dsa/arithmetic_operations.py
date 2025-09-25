def perform_operation(num1, num2, operation):
    if operation == 'add':
        return float(num1) + float(num2)
    elif operation == 'subtract':
        return float(num1) - float(num2)
    elif operation == 'multiply':
        return float(num1) * float(num2)
    elif operation == 'divide':
        if float(num2) == 0:
            return "Error: Division by zero"
        return float(num1) / float(num2)
    else:
        return "Error: Invalid operation"
    
