# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20


def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """
    total = '0x'
    binValues = [8, 4, 2, 1]
    hex_letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    groups = [number[0:4], number[4:8], number[8:12], number[12:16]]
    for group in groups:
        group_total = 0
        for i in range(len(group)):
            if group[i] == '1':
                group_total += (binValues[i])
        total += hex_letters[group_total]
    return total


def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    binFinal = ''
    hex_letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    realNum = number[2:]
    for i in range(len(realNum)):
        val = hex_letters.index(realNum[i])
        binGroup = ''
        for j in range(4):
            if 2 ** (4 - j - 1) <= val:
                binGroup += '1'
                val -= (2 ** (4 - j - 1))
            else:
                binGroup += '0'
        binFinal += binGroup
    return binFinal


