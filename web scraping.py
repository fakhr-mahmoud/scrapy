#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
#import pymongo
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest


# In[2]:


MainURL= 'https://www.bbc.com/'

#Get the HTML for each article.
page_html= requests.get(MainURL)
lol= page_html.content
page_soup= BeautifulSoup(lol , 'html.parser')
results = page_soup.find_all("a", {"class":"block-link__overlay-link"})
Tilte=[]
TitleList=[]
#extract the article title from the HTML.
for result in results:
    Title= result.text.strip() 
    print(Title)
    TitleList.append(Title)


# In[3]:


list=[]
links=[]
#extract the link of each article.
for result in range(len(results)) :
    #list.append(results[result].text)
    links.append(results[result]['href'])

#arrange links list
#for result in range(len(list)):
  #  temp = list[result]
  #  list[result]=temp[2:].strip()


# In[4]:


NewLinks = []
#add (www.bbc.com) to uncompleted links. 
for link in links:
    if 'www'not in link:
        NewLink = link.replace("/", "https://www.bbc.com/",1)
        NewLinks.append(NewLink)
    else:
        NewLinks.append(link)

print(NewLinks)


# In[5]:


#Extract the Tags and print it.
Tags= []
TagList=[]
Tags = page_soup.find_all("a", {"class":"media__tag"})
for Tag in Tags:
    tag= Tag.text
    print(tag)
    TagList.append(tag)


# In[6]:


authors=[]

for link in NewLinks:
#Get the HTML for each article.
    print(len(NewLinks)-(NewLinks.index(link)))
    try:
        page_html= requests.get(link)
        lol= page_html.content
        pageSoup= BeautifulSoup(lol , 'html.parser')
        authors.append(pageSoup.find("p", {"class":["lx-commentary__meta-reporter gel-long-primer","ssrcss-1gg9z89-Contributor e5xb54n2","qa-contributor-name lx-stream-post__contributor-name gel-long-primer gs-u-m0"]}).text)
    
    except:
        authors.append("")


AuthorList=[]
for author in authors:
    #author= author.text
    print(author)
    AuthorList.append(author)


# In[7]:


#articles text
articles=[]

for link in NewLinks:
#Get the HTML for each article.
    print(len(NewLinks)-(NewLinks.index(link)))
    try:
        page_html= requests.get(link)
        lol= page_html.content
        Soup= BeautifulSoup(lol , 'html.parser')
        articles.append(Soup.find("p", {"class":["ssrcss-1q0x1qg-Paragraph eq5iqo00"]}).text)
    
    except:
        articles.append("")


ArticlesList=[]
for article in articles:
    #author= author.text
    print(article)
    ArticlesList.append(article)


# In[8]:


file_list = [TitleList,TagList,AuthorList,ArticlesList,NewLinks]
exported = zip_longest(*file_list)
#save the data in a csv file 
with open("E:/NU/4- Final Year/summer work/The_data.csv","w")as myfile:
    wr =csv.writer(myfile)
    wr.writerow(["article Title","article Tag","Author","Article","article Link"])
    wr.writerows(exported)
print("DONE")


# In[ ]:





# In[ ]:




