user_input = input('Enter two numbers separated by commas:')
operations = input('Enter the operation you want to perform:')
split_user_input = user_input.split(',')
while operations in ['+', '-', '*', '/']:
    if len(split_user_input) != 2:
        print('Invalid input. Please enter exactly two numbers.')
        user_input = input('Enter two numbers separated by commas:')
        split_user_input = user_input.split(',')
    elif len(split_user_input) == 2: 
        if operations == '+':
            print(float(split_user_input[0]) + float(split_user_input[1]))
            user_input = input('Enter two numbers separated by commas:')
            split_user_input = user_input.split(',')
        elif operations == '-':
            print(float(split_user_input[0]) - float(split_user_input[1]))
            user_input = input('Enter two numbers separated by commas:')
            split_user_input = user_input.split(',')
        elif operations == '*':
            print(float(split_user_input[0]) * float(split_user_input[1]))
            user_input = input('Enter two numbers separated by commas:')
            split_user_input = user_input.split(',')
        elif operations == '/':
            if split_user_input[1] == '0':
                print('Division by zero is not allowed. Try again')
                user_input = input('Enter two numbers separated by commas:')
                split_user_input = user_input.split(',')
            else:
                print(float(split_user_input[0]) / float(split_user_input[1]))
                user_input = input('Enter two numbers separated by commas:')
                split_user_input = user_input.split(',')
    else:
        break
else:
    print('Invalid operation')

