# investing.com-crawler
Create a web crawler that extracts cryptocurrency news from investing.com with python3

Note: This is specifically made for investing.com, other websites will not work.

Before running make sure to have python 3 and scrapy

To get scrapy:
  
  pip install scrapy
  
  https://doc.scrapy.org/en/latest/intro/install.html
  
To run:

scrapy runspider name_of_the_file.py 

To run and save data into a csv,xml or json file

scrapy runspider name_of_the_file.py -o name_of_new_file.json
scrapy runspider name_of_the_file.py -o name_of_new_file.xml
scrapy runspider name_of_the_file.py -o name_of_new_file.csv
