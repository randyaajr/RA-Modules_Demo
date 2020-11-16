from lib_num import conversion

from colorama import Fore

print(Fore.LIGHTYELLOW_EX + "Values available for conversion: \n 'cm to m'\t 'm to cm' \n 'cm to mm'\t 'mm to cm' \n 'mm to m'\t 'm to mm' \n 'ft to cm'\t 'ft to inch' \n 'inch to cm'\t 'inch to mm'")

input_num = input(Fore.LIGHTCYAN_EX + 'Enter the a numeric value: ')
con_from = input(Fore.LIGHTBLUE_EX +
                 'Which unit of measurement do you wish to converted from:  ')
con_to = input(Fore.LIGHTMAGENTA_EX +
               'Which unit of measurement do you want it converted to: ')

conversion(input_num, con_from, con_to)
