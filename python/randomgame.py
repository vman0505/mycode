#!/usr/bin/python3

import requests

MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    result = requests.get(MYAPI)
    if "1" in result.text: ## if the value of 1 is in result.text
        print("You won!")
    else:
        print("You lost")

main()        
