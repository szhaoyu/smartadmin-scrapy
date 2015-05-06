# -*- coding: utf-8 -*-
import os
from selenium import webdriver
import time
import urllib2


url='http://192.241.236.31/themes/preview/smartadmin/1.5/angularjs/#/dashboard'
driver=webdriver.Chrome()
driver.get(url)
#sleep to wait 
time.sleep( 30 )
content=driver.page_source
#save into file
file=open('dashboard.html','w')
file.write(content.encode('utf-8'))
file.close()
driver.quit()
#recgonize all affixed css or js files.
import re
rel_paths=[]
attaches = re.findall( r'href="[^"]+"', content )
for item in attaches:
    one = re.search(r'"([^"]+)"', item )
    rel_path = one.group(1)
    if rel_path.startswith('//') == False and rel_path.startswith('http') == False:
        rel_paths.append( rel_path )

for one in rel_paths:
    ps=one.split('/')
    ps.pop()
    ppath = '/'.join(ps)
    try:
        if os.path.exists( ppath ) == False:
            os.makedirs( ppath )
        #do http get
        attach_uri='http://192.241.236.31/themes/preview/smartadmin/1.5/angularjs/'+one
        print( attach_uri )
        req = urllib2.Request( attach_uri )
        #try:
        response = urllib2.urlopen(req)
        lines = response.readlines()
        file=open( one, 'w')
        for line in lines:
            file.write( line+'\n' )
        file.close()
    #except urllib2.URLError, e:
    except Exception, e:
        print e.reason
    print( one )
    time.sleep( 2 )






