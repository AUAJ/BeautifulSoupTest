# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:22:27 2017

@author: AJ
"""


import requests
from bs4 import BeautifulSoup


def get_link(url):
    if check_url(url) != 1:
        print "url is bad"
        
    r = requests.get(url)
    
    data = r.text
    soup = BeautifulSoup(data)
    
    for link in soup.find_all('a'):
        print(link.get('href'))
        
     
def check_url(url):
    r = requests.get(url, allow_redirects = False)
    #print(r.status_code, r.headers['Location'])
    #print response.history
    
    first_letter = str(r.status_code)
    
    if first_letter[0] == '2':
        #transmission OK on the http level
        print r.status_code
        return 1
    elif first_letter[0] =='4':
        # Client error
        print "I messed up"
        return 0
    elif first_letter[0] == '5':
        # Server error 
        print "It wasn't me"
    else:
        print r.status_code
        return 0

     
if __name__ ==  "__main__":
    #get_link("http://pythonforengineers.com/pythonforengineersbook/")
    get_link("http://pythonforengineers1.com/pythonforengineersbook/")    
    #get_link("http://httpbin.org/status/404")
    #get_link('http://httpbin.org/get')