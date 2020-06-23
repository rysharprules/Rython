users_name = input('What is your name? ') # input function is used for prompt for user to type something
greeting = 'Hello, ' + users_name + '!' # user entry is saved in variable users_name
print(greeting) # print function displays greeting variable to the console

# greeting via function
def hello_world():
    print('Hello World!')

hello_world() # function call

# function with arguments
def greet_user(first_name, last_name):
    full_name = first_name + ' ' + last_name
    print('Hey there, ' + full_name)

greet_user('Earthworm', 'Jim')