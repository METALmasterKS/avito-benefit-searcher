# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import urllib.request


response = urllib.request.urlopen('https://www.avito.ru/sankt-peterburg?pmax=2000&pmin=300&s=101&q=ssd')

print(response.read())

if __name__ == "__main__":
    print("Hello World")
