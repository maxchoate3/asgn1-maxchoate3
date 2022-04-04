# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Spring '22


def add(addend_a, addend_b):
    """
    Add two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    total = ''
    carry = False
    for i in range(len(addend_a)):
        numOnes = 0
        if addend_a[len(addend_a) - 1 - i] == '1':
            numOnes += 1
        if addend_b[len(addend_b) - 1 - i] == '1':
            numOnes += 1
        if carry:
            numOnes += 1
            carry = False
        if numOnes == 0:
            total = '0' + total
        if numOnes == 1:
            total = '1' + total
        if numOnes == 2:
            total = '0' + total
            carry = True
        if numOnes == 3:
            total = '1' + total
            carry = True
    return total


def negate(number):
    """
    Negate a 16-bit, two's complement number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    newNum = ''
    for i in range(len(number)):
        if number[len(number) - 1 - i] == '0':
            newNum = '1' + newNum
        else:
            newNum = '0' + newNum
    return newNum


def subtract(minuend, subtrahend):
    """
    Subtract one 16-bit, two's complement number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    return negate(add(negate(minuend), subtrahend))


def multiply(multiplicand_a, multiplicand_b):
    """
    Multiply two 16-bit, two's complement numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param multiplicand_a: A bitstring representing the first number
    :param multiplicand_b: A bitstring representing the second number
    :return: A bitstring representing the product
    """
    total = '0000000000000000'
    for i in range(len(multiplicand_b)):
        if multiplicand_b[len(multiplicand_b) - 1 - i] == '1':
            currTotal = '0' * i
            currTotal = multiplicand_a + currTotal
            total = add(total, currTotal)
    return total


def binary_to_decimal(number):
    """
    Convert a 16-bit, two's complement number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    total = 0
    for i in range(len(number)):
        if number[len(number) - 1 - i] == '1':
            total += (2 ** i)
    return total

def decimal_to_binary(number):
    """
    Convert a decimal number to 16-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 16 bits
    """
    total = ''
    for i in range(16):
        if 2 ** (16 - i - 1) <= number:
            total += '1'
            number -= (2 ** (16 - i - 1))
        else:
            total += '0'
    if number is not 0:
        raise OverflowError
    return total

