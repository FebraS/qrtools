#!/usr/bin/env python
#Authors:
#   0xFebra <0xfebra@gmail.com>

import argparse
import qrcode
import string
import random

parser = argparse.ArgumentParser(description="QR Code Generator")

#create a menu using argparse
#declare argument
parser.add_argument('-g','--generate',type=str,help='Generate QR Code',required=True)
parser.add_argument('-o','--output',type=str,help='Default QR Ouput Name : \"ScanMe\"',required=False)
args = parser.parse_args()

def qr_generate(generate,output):
    #the filename into a ascii letters
    letters = string.ascii_letters
    #random letters in 10 characters
    letters = ''.join(random.choice(letters)for i in range(10))
    
    #generating process
    qr = qrcode.make(generate)
    if output is not None:
        #if the user inputs a file name using the -o argument
        qr.save("output/"+ output + ".png")
    else:
        #if not then use random filename
        qr.save("output/"+ letters +".png")
        print("Your QR are Your QR Code has been created with the name "+ letters +".png")

def main():
    qr_generate(args.generate,args.output)
main()
