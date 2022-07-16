

def summing_numbers(*numbers):
    output = 0
    for number in numbers: 
        output += number
    return output
print(summing_numbers(10, 20, 30 ,40))
