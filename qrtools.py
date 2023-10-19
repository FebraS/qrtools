#!/usr/bin/env python
#Authors : FebraS <0xfebra@gmail.com>

import argparse
import qrcode
import string
import random

parser = argparse.ArgumentParser(description="QR Code Generator")

#Membuat menu menggunakan argparse
parser.add_argument('-g','--generate',type=str,help='Generate QR Code',required=True)
parser.add_argument('-o','--output',type=str,help='Default QR Ouput Name : \"ScanMe\"',required=False)
args = parser.parse_args()

def qr_generate(generate,output):
    #Membuat nama file
    letters = string.ascii_letters
    #Mengacak nama file
    letters = ''.join(random.choice(letters)for i in range(10))
    
    #Proses mengahasilkan qrcode
    qr = qrcode.make(generate)
    if output is not None:
        #Jika user menggunakan argumen -o
        qr.save("output/"+ output + ".png")
    else:
        #Gunakan nama acak
        qr.save("output/"+ letters +".png")
        print("Your QR are Your QR Code has been created with the name "+ letters +".png")

def main():
    qr_generate(args.generate,args.output)

main()
