#
# CODE AUTHOR: About Code
# CODE CREATION DATE: January 21, 2019
# ADDITIONAL CREDITS: see last line
#

import os
import re
import requests
from bs4 import BeautifulSoup

# replace the URL below with your URL
site = 'https://www.reddit.com/r/photographs/comments/ai0rol/while_i_was_in_amsterdam/'

# site = 'file:///Users/macuser/scratch_dir/Amsterdam.html'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

# print(urls)
count = 0

os.system("mkdir data; cd data")

for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))', url)
    if(filename is None):
        continue
    count = count + 1
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

os.system("cp *.jpg data")
os.system("cp *.gif data")
os.system("cp *.png data")

print("Number of files downloaded = " + str(count))

# Adapted from code found on Stack Overflow
# URL1: https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup
# URL2: https://stackoverflow.com/questions/51485736/scraping-different-image-every-day-from-url
