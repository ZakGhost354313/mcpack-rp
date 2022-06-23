#!/usr/bin/env python3

import os
from time import sleep

def build():
    os.system('zip -r pack.zip pack')
    os.system('mv pack.zip builds/wp_RP.mcpack')

def main():
    a = input('you sure(y/n)?  ') 
    if a == "y": build()
    elif a == "n": print('bye')
    else: 
        print('error')
        main()

if __name__ == "__main__": 
    main()