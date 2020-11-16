from lib_num import conversion

from colorama import Fore

print(Fore.LIGHTRED_EX + "Values available for conversion: \n 'cm to m'\t 'm to cm' \n 'cm to mm'\t 'mm to cm' \n 'mm to m'\t 'm to mm' \n 'ft to cm'\t 'ft to inch' \n 'inch to cm'\t 'inch to mm'")

input_num = input(Fore.LIGHTCYAN_EX + 'Enter the a numeric value: ')
con_from = input(Fore.LIGHTBLUE_EX +
                 'Which unit of measurement do you wish to converted from:  ')
con_to = input(Fore.LIGHTMAGENTA_EX +
               'Which unit of measurement do you want it converted to: ')

"""
This simple measurement coversion app coverts the following below:

        "cm" to "m":

        "mm" to "cm":

        "m" to "cm":

        "cm" to "mm":

        "mm" to "m":

        "m" to "mm":

        "ft" to "cm":

        "ft" to "inch":

        "inch" to "cm":

        "inch" to "mm":
"""
conversion(input_num, con_from, con_to)
