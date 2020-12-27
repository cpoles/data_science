"""Turing Test"""

while True:
    # ignore first input
    input('What is your problem?')
    # get the response for the second question
    response = input('Have you had this problem before? (yes or no)')
    # respond the user based on their answer
    if response == 'yes':
        print('Well, you have it again.')
        break
    elif response == 'no':
        print('Well, you have it now.')
        break
    else:
        print("Wrong answer. Respond 'yes' or no")
        continue


