import time
import csv
import requests
from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

datalist = [] #empty list


#launch url
with open('worlds.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range (0,40):

            bu_url = "https://www.bu.edu/phpbin/course-search/section/?t=cascs"+ row[i]+ '/'


# create a new Firefox session
            driver = webdriver.Firefox(executable_path='/home/classdash/projectclassdash/geckodriver-v0.19.1-linux64.tar.gz')
            driver.get(bu_url)
            driver.implicitly_wait(100)
            time.sleep(10)


            
            soup_level2=BeautifulSoup(driver.page_source, 'html.parser')

    #Beautiful Soup grabs the HTML table on the page
            try:
                table = soup_level2.find_all('table')[-1]

        
            except IndexError as error:
                pass
            
            data = table.findAll('td')
            p = 0
            while p < len(data)-1:
                data1 = data[p].string
                p=p+1
                data2 = data[p].string
                p=p+1
                data3 = data[p].string
                p= p+1
                data4 = data[p].string
                flag = 0
                if (type(data1)is bs4.element.NavigableString):
                    flag = 1
                else:
                    flag = 0
                if (type(data2)is bs4.element.NavigableString):
                    flag = flag+1
                else:
                    flag = 0
                if (type(data3)is bs4.element.NavigableString):
                    flag = flag+1
                else:
                    flag = 0
                if (type(data4)is bs4.element.NavigableString):
                    flag =flag+1
                else:
                    flag = 0
                
                if flag == 4:
                        mydic = {'code':row[i], 'section':data1, 'title':data4, 'semester':'Fall 2019', 'seats':data2, 'instructor':data3}
                        datalist.append(mydic)
                        f = open('test1.csv','a')
                        f.write(row[i]+ ", ") 
                        f.write(data1 + ", ") 
                        f.write(data4 + ", ")
                        f.write("Fall 2019, ")
                        f.write(data2+ ", ")
                        f.write(data3 + "\n")
                        p = p+5
                elif (type(data1)is not bs4.element.NavigableString):
                    p = p+9
                else:
                    p = p+5
            driver.quit()
f.close()
