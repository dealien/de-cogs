# Taken from https://gist.github.com/4060082
# If you have BeautifulSoup, you can test this locally via:
# curl https://gist.githubusercontent.com/RichardBronosky/4060082/raw/test.py | python
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint
import re

soup = BeautifulSoup(urlopen('https://gist.githubusercontent.com/RichardBronosky/4060082/raw/test.html').read())
# I'm going to assume that Peter knew that re.compile is meant to cache a computation result for a performance benefit. However, I'm going to do that explicitly here to be very clear.
pattern = re.compile('Fixed text')

# Peter's suggestion here returns a list of what appear to be strings
columns = soup.findAll('td', text=pattern, attrs={'class' : 'pos'})
# ...but it is actually a BeautifulSoup.NavigableString
print type(columns[0])
#>> <class 'BeautifulSoup.NavigableString'>

# you can reach the tag using one of the convenience attributes seen here
pprint(columns[0].__dict__)
#>> {'next': <br />,
#>>  'nextSibling': <br />,
#>>  'parent': <td class="pos">\n
#>>       "Fixed text:"\n
#>>       <br />\n
#>>       <strong>text I am looking for</strong>\n
#>>   </td>,
#>>  'previous': <td class="pos">\n
#>>       "Fixed text:"\n
#>>       <br />\n
#>>       <strong>text I am looking for</strong>\n
#>>   </td>,
#>>  'previousSibling': None}

# I feel that 'parent' is safer to use than 'previous' based on http://www.crummy.com/software/BeautifulSoup/bs4/doc/#method-names
# So, if you want to find the 'text' in the 'strong' element...
pprint([t.parent.find('strong').text for t in soup.findAll('td', text=pattern, attrs={'class' : 'pos'})])
#>> [u'text I am looking for']

# Here is what we have learned:
print soup.find('strong')
#>> <strong>some value</strong>
print soup.find('strong', text='some value')
#>> u'some value'
print soup.find('strong', text='some value').parent
#>> <strong>some value</strong>
print soup.find('strong', text='some value') == soup.find('strong')
#>> False
print soup.find('strong', text='some value') == soup.find('strong').text
#>> True
print soup.find('strong', text='some value').parent == soup.find('strong')
#>> True
