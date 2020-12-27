"""Using nested control statements to analyse examination results."""

#initialize variables
passes = 0
failures = 0

counter = 0

while counter < 10:
    #get user input
    result = int(input('Enter result (1=pass,2=fail): '))
    if result == 1:
        passes += 1
        counter += 1
    elif result == 2:
        failures += 1
        counter += 1
    else:
        print('Wrong input. Only 1 or 2 are allowed.')
        continue

#termination phase
print(f"Passed: {passes}\nFailed: {failures}")
