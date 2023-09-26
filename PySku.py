'''
Sophie Koenig
Updated 9/22/23
SKU Generator Project

Will generate a SKU for items based off name, qty, etc.
Uses a given csv file inside 'files' in the same directory

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
import re

def main():
    inputFile = (f'{input("Input file name: ").strip()}.csv')

    while not os.path.isfile("files/" + inputFile):

        try:
            open('files/' + inputFile)
        except FileNotFoundError:
            if inputFile == 'q' or inputFile == 'Q':
                quit()
            else:
                print('\nFile does not exist.')
                inputFile = (f'{input("Input file name: ").strip()}.csv')

    outputFile = (f'{input("Output file name: ").strip()}.csv')

    while os.path.isfile(f'files/{outputFile}'):
            
            ans = input('Overwrite file with same name? (y/n): ').lower().strip()
            while ans != 'y' and ans != 'n':
                 ans = input('(y/n): ').lower().strip()
            if ans == 'y':
                 break
            else:
                 outputFile = (f'{input("New output file name: ").strip()}.csv')
    
    uniVendors = {} #stores unique vendor as element, number of vendor products as key
    uniBrandDigs = {}

    with open(f'files/{outputFile}', 'w+', newline='') as csvfile:
         
         writer = csv.writer(csvfile)
         writer.writerow(['SKU', 'Vendor', 'Product Name', 'Size', 'Type'])

         with open(f'files/{inputFile}', 'r') as inputCSV:
            
            reader = csv.reader(inputCSV)

            for line in reader:

                brandDigs = ''
                sizeDigs = ''
                uomDigs = ''

                print(line)

                sliceStart = 1
                sliceEnd = 3
                vendor = line[0].lower().replace('o', '')

                while True:
                    if vendor.isspace() or "-" in vendor:
                        pass
                    else:
                        brandDigs = vendor[sliceStart:sliceEnd].upper()
                        print(brandDigs)
                        if brandDigs in uniBrandDigs and line[0] not in uniVendors:
                            sliceStart += 1
                            sliceEnd += 1
                        else:
                            uniBrandDigs.append(brandDigs)
                            uniVendors[line[0]] += 1
                            break

                print("help")

            if uniVendors.get(line[0]) == None:
                uniVendors[line[0]] = 1
            else:
                uniVendors[line[0]] += 1

            print(uniVendors)

    print("Success")

if __name__ == '__main__':
    main()