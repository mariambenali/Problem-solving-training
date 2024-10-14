''' solution using index '''

def simpleArraySum(ar):
    x = 0
    for index in range (len(ar)):
        x = x + ar[index]
    return x


print(simpleArraySum([1, 2, 3]))


'''solution using for loop '''
'''
def simpleArraySum(ar):
    x = 0
    for y in ar:
        x = x + y
    return x

print(simpleArraySum([1, 2, 3]))

'''