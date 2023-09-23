'''
Sophie Koenig
Updated 9/22/23
SKU Generator Project

Will generate a SKU for items based off name, qty, etc.
Criteria is as follows:

3 digits for brand name (text) note: avoid using the letter O
3 digits for count of items in that brand 001-999 (numerical)
2 digitals for size (numerical)
2 digitals for selling UOM (text) note: blank for each, CP for case pack etc. 

Here's some fake examples:

BTS00103 - Botanical Science Microdermabrasion Creme, 3.3 oz
BTS00103CP - Botanical Science Microdermabrasion Creme, 3.3 oz Case Pack of 12
'''

import csv
import os.path

def main():
    inputFile = input("Enter file name: ").strip()

    while not os.path.isfile("files/" + inputFile):

        try:
            open('files/' + inputFile)
        except FileNotFoundError:
            if inputFile == 'q' or inputFile == 'Q':
                quit()
            else:
                print('\nFile does not exist.')
                inputFile = input('Enter file name. Enter "q" to quit: ').strip()

    outputFile = input("output file name")

    while os.path.isfile(f'files/{outputFile}'):
            ans = input('Overwrite file with same name? (y/n): ').lower().strip()
            while ans not in 'yn':
                 ans = input('(y/n): ')


    print("Success")

if __name__ == '__main__':
    main()