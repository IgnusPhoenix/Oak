
import webbrowser 

#introduction
print("Hello. This is Project Oak. What is your name?")
#--------------------------------------------------------------------------------------

#name
firstName = input("Please type your first name here: ")
lastName = input("Please write your last name here: ")
#---------------------------------------------------------------------------------------

#variables
name = firstName + " " + lastName
answer = "Your answer is: "
godspeed = "Bye, have a nice day, " + name + "."
redirection = "Your will now be redirected to your default browser. Loading..."
disclaimer = "The programme can only hold two terms per mathematical operation."
requestNumber1 = "Please type the first number here: "
requestNumber2 = "Please type the second number here: "

#---------------------------------------------------------------------------------------

#main code
print("Hello, " + name + ". How may I help you?")
request = input("Write your request here, please: ")
while True == True:
    request = request.lower()

    if request == "add":
        print(disclaimer)
        number1 = float(input(requestNumber1))
        number2 = float(input(requestNumber2))
        print(answer, number1+number2)

    elif request == "subtract":
        print(disclaimer)
        number1 = float(input(requestNumber1))
        number2 = float(input(requestNumber2))
        print (answer, number1-number2)

    elif request == "multiply":
        print(disclaimer)
        number1 = float(input(requestNumber1))
        number2 = float(input(requestNumber2))
        print(answer, number1 * number2)

    elif request == "divide":
        print(disclaimer)
        number1 = float(input(requestNumber1))
        number2 = float(input(requestNumber2))
        if request == "divide" and number2 == 0:
            print("Syntax error.")
            continue
        print(answer, number1 / number2)

    elif request == "question":
        query = input("Please type your question here: ")
        print(redirection)
        webbrowser.open('https://duckduckgo.com/?t=ffab&q=' + query + '&atb=v275-1&ia=web')

    elif request == "image" or "images":
        query = input("Please type the name of the object you wish to see: ")
        print(redirection)
        webbrowser.open('https://duckduckgo.com/?t=ffab&q='+ query + '&atb=v275-1&iax=images&ia=images')

    else:
        print("Please enter a valid request")
    request = input("Write another request here, please: ")
