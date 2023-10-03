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

    print(f'\nCSV FILE SHOULD BE FORMATTED AS: Vendor, Product Name, Size, Type')
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
    
    uniVendors = {} # stores unique vendor as element, number of vendor products as key
    uniBrandDigs = set([])

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

                sliceStart = 0
                sliceEnd = 3
                vendor = line[0].lower().replace('o', '') # temp var to hold the altered vendor name. Original vendor name will not be changed, needs to be written to output file.

                # brand digits logic. As lines are iterated through it assigns updated count of unique items per vendor to uniVendors
                while True: 

                    print(uniVendors)

                    if vendor.isalnum():

                        brandDigs = vendor[sliceStart:sliceEnd].upper()
                        print(brandDigs)

                        if brandDigs in uniBrandDigs and line[0] not in uniVendors: # Checks that another vendor isn't already using the same digits
                            sliceStart += 1
                            sliceEnd += 1
                        else:
                            uniBrandDigs.add(brandDigs)
                            break

                    else:

                        vendor = re.split('\W+', vendor) 
                        sliceStart = 0
                        sliceEnd = 1
                        
                        if len(vendor) >= 3:

                            for i in range(3):
                                brandDigs += (vendor[0][sliceStart:sliceEnd]).upper()
                                vendor.pop(0)

                        else: 

                            brandDigs += vendor[0][sliceStart:sliceEnd]
                            vendor.pop(0)
                            brandDigs += vendor[0][sliceStart:sliceEnd + 1]
                            brandDigs = brandDigs.upper()
                            print(f'\nDOES IT WORK? {brandDigs}\n')

                        if brandDigs in uniBrandDigs and line[0] not in uniVendors:
                            sliceStart += 1
                            sliceEnd += 1

                        else:
                            uniBrandDigs.add(brandDigs)
                            break
                
                # Size Digits Logic...

                if uniVendors.get(line[0]) == None:
                    uniVendors[line[0]] = 1
                else:
                    uniVendors[line[0]] += 1

                print(uniVendors)
                print(brandDigs)

    print("Success")

if __name__ == '__main__':
    main()