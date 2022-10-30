# Understanding how computers work with binary currents with bitwise operations AND how arithmatic operations work on that, by developing a calculator that can do the same.


# What is binary numbers? => 0 and 1, they are simply like a switch, either on or off, 1 or 0.

# What is a bit? => A bit is a single binary digit, 0 or 1.

# What is a byte? => A byte is a group of 8 bits, 8 binary digits, 8 switches, 8 0s and 1s.



# ----------------------------------------------------------------------------------------------------------------------------------------------
# LIMITATIONS:
# 1. For Positive Integers Only
# ----------------------------------------------------------------------------------------------------------------------------------------------



# Converting a decimal number to binary number.


def decimal_to_binary(decimal_number):
    # Brute Code First Try:

    # counting how many bits will be needed to form string or you can say allocating space
    count = 1
    while True:
        measurable = ((2**count)-1)
        if decimal_number > measurable:
            count += 1
        else:
            break
    
    # allocating space
    bin = [] # How can I overwrite bin, because bin is python built-in function not a operator neither keyword...
    for i in range(count):
        bin.append("0")
    
    # not playing with main argument, a good habit, maybe I'll need in future
    temp = decimal_number

    # real algorithm
    def biggest(num):
        return 2**num

    for i in range(len(bin)):
        j = len(bin) - 1 - i # just to get number of positing in reverse order, because in binary integer data left hand side has greater value

        if temp >= biggest(j):
            bin[i] = "1" # i is not disturbed here to assign bits in right order, otherwise I have to reverse the list afterwards
            temp = temp - biggest(j) # what I'm doing is iterating through every bit and finding it's turned on value, if greater than value remained from decimal value will turn that bit on and subtract that value from decimal value and loop it further until reached zero
    
    return ''.join(bin) # str is immutable so I had to convert str into list and then vice-versa


    # ------------------------------------------------------------------------------------------------------------------------------------------


    # Better Version


    # Best from co-pilot or research



# ----------------------------------------------------------------------------------------------------------------------------------------------



# Building Gates and with the help of different gates, building complex logic circuits for various operation.


# Firstly, there is an AND and a NOT gate which can't be build via code, I mean it can but it'll require if else and other high level language stuff which already build upon logic circuits, So using them don't make sense. AND and NOT can made via physical circuit easily for ex: A circuit with two switch and a led in series is a example of a AND gate with led indicating binary.

# First, I'll build NAND, OR, XOR which will be helpful in building Binary Adder...

def AND(a, b):
    return a and b


def NAND(a, b):
    '''
    Not of And
    Truth Table
    0, 0 | 1
    0, 1 | 1
    1, 0 | 1
    1, 1 | 0
    '''

    return int(not (AND(a, b)))

def OR(a, b):
    '''
    Not of inputs of Nand
    Truth Table
    0, 0 | 0
    0, 1 | 1
    1, 0 | 1
    1, 1 | 1
    '''

    return int(NAND(not(a), not(b)))

def XOR(a,b):
    '''
    And of Nand and Or
    Truth Table
    0, 0 | 0
    0, 1 | 1
    1, 0 | 1
    1, 1 | 0

    XOR is Basically Adder of Binary Numbers but Without Carry because if both inputs/binary are 1 it give zero but this 1 should be carry to next bit
    '''

    return int(AND(NAND(a, b), OR(a, b)))



# ----------------------------------------------------------------------------------------------------------------------------------------------



# Logic To Add Binary Numbers

'''
THEORY:
How bits add?
First, We need to understand that what bits depicts naturally it's just 0 and 1, true or false, but true or false of what. So, according to the place of the bit, it means something, A Value, 0 means that value is neglected and 1 means take that value into consideration.
For Example, in a 4 bit system:
1st 0,1 depicts -> 1
22t 0,1 depicts -> 2
3rd 0,1 depicts -> 4
4th 0,1 depicts -> 8

This depiction is based on binary counting system not much different then the decimal counting system we follow.
So 1st bit can show upto 2 possibility or two possible outcomes, so it can count upto 2 and so on.

For Example: 0101 represent 5 in binary. [0*8 + 1*4 + 0*2 + 1*1]

Moving forward with Binary, Coming to our main topic how does binary actually add?
As we discussed above, every bit depicts a number and same place bits will represent same number but if you have noticed closely, you'll observe that every next place is double of the previous, Means If I add two same place bit it's also say double of that bit which we just see that is the next place bit. So, If I take two 1's of same place like this: 0010 and 0010, It'll turn next bit up, but in return value of the current bit turns off, like this -->  0010 + 0010 => 0100. Just like this if I have 4 bit of same place it turns out 2 bit of next place which further mean 1 bit of even next to next bit. like this --> 0010(2) + 0010(2) + 0010(2) + 0010(2) --> 0100(4) + 0100(4) => 1000(8).
'''

def two_bit_adder(bit1, bit2, carry = 0):
    '''
    Need only XOR and AND Gates:
    XOR -> will act as the Result Finder for current bit, And
    AND -> will act as Carry Finder
    '''

    curr_bit = XOR(XOR(bit1, bit2), carry) # XOR for 3 bit system
    
    # carry = OR(OR(AND(bit1, bit2), AND(bit2, carry)), AND(carry, bit1)) # there are 3 posibilities of AND gate for 3 bit system, ab, bc and ca. This system is equivalent of, IF there are 2 or 3 bits turned on(1), then return 1, IF less then 2 bit is one or no bit is turned 1 return false.

    # A Better Way
    carry = OR(AND(XOR(bit1, bit2), carry), AND(bit1, bit2)) # According to A Better Carry Calculation Theory, there are two possibility for carry two result 1, rather than three as shown in previous example, First, If both Bits are True Return True, OR, Secondly, If one Bit is True and Carry is True Return True. This is just a simulation of that.

    return [curr_bit, carry]


def largest_len(ls):
    '''To find largest length of string from strings in given list'''
    temp = len(ls[0])
    for i in range(1, len(ls)):
        if len(ls[i]) > temp:
            temp = len(ls[i])
    
    return temp


def binary_adder_two_bit(a, b):
    # Equalising all binary numbers lengths. Like If one is 1 and other if 010 then first one should be 001 for optimal addition
    l_len = largest_len([a, b])

    if len(a) < l_len:
        diff = l_len - len(a)
        a = ("0"*diff) + a
    if len(b) < l_len:
        diff = l_len - len(b)
        b = ("0"*diff) + b

    # Actually Adding
    total = ""
    carry = 0
    for i in range(l_len-1, -1, -1): # Getting bits from reverse because binary number start from reverse
        bit, carry = two_bit_adder(int(a[i]), int(b[i]), int(carry)) # using two bit adder for every bit
        total += str(bit)

    return (str(carry) + total[::-1]) # We need to reverse the total as we perform addition rightfully(reversed), but don't add it to start of str but just normally to the end


# EXAMPLE:
# print(decimal_to_binary(17))
# print(binary_adder_two_bit("111", "100"))



# ----------------------------------------------------------------------------------------------------------------------------------------------



def many_bit_adder(bits_in_list, carry=0):
    '''
    THEORY:
    Every next bit is of double value of the previous bit, so two previous bit of same position will be a single bit of next position,
    We'll just take exploit this scenario, we'll just shift the to next position by reducing it to half if even or first make it even by storing one value in current bit.
    For Example:
     0001
    +0001
    +0001
    +0001
    If we have a bit number system like this, Indicating 4, What we can do is turning off all the one's value bits and turn a single 4 value bit. CONGRATULATIONS, we have invented Addition.
    Theoretically, We'll first reduce all the four bit into two bit of next position and secondly that two bit into even next to next position, So It'll become like this -> 0001+0001+0001+0001 -> 0010+0010 => 0100.

    It's also discussed in Main THEORY Section, Please Refer to That.
    '''

    # Calculating Current Bit
    bit = 0
    ones = bits_in_list.count(1) + carry
    if ones%2 == 0:
        bit = 0
    else:
        bit = 1
        ones -= 1

    # Calculating Carry
    carry = ones / 2

    return [bit, int(carry)]


def binary_adder_many_bit(*bin):
    # Equalising all binary number lengths
    ls = []

    l_len = largest_len(bin)

    for i in bin:
        if len(i) < l_len:
            diff = l_len - len(i)
            ls.append(("0"*diff) + i)
        else:
            ls.append(i)

    # Actually Adding
    total = ""
    carry = 0
    for i in range(l_len-1, -1, -1): # Getting bits from reverse because binary number start from reverse
        bits = []
        for j in ls:
            bits.append(int(j[i]))
        bit, carry = many_bit_adder(bits, int(carry))
        
        total += str(bit)

    # If iteration number get finished before calculation getting over as it's only set to length of binary number, In short What If resultant result is grater in length then the inputs, Therefore this while loop to take care of that
    while carry > 0: # Will run until it'll resolve carry, Refer to THEORY <-- many_bit_adder
        bit, carry = many_bit_adder([], int(carry))

        total += str(bit)

    return (total[::-1]) # We need to reverse the total as we perform addition rightfully(reversed), but don't add it to start of str but just normally to the end


# EXAMPLE
# print(binary_adder_many_bit('1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'))
