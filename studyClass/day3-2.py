responses = {}
while True:
    name = input("\n What's your name?")
    responses = input("\n What's your option?")
    responses[name] = responses
    if input("Have move? (yes/no?)") == 'no':
        break