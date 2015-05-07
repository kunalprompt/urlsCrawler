import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse

def crawlPage(page_url):
	print "Crawling URL - %s"%(page_url)
	url_schema = urlparse(page_url)
	if url_schema.scheme=='' or url_schema.netloc=='':
		print "Page URL not defined properly."
		return []
	# constructing the base url
	base_url = str(url_schema.scheme) + "://" + str(url_schema.netloc)
	# the list of urls to be returned from this page
	page_urls_list = []
	page_urls_list.append(page_url)
	try:
		req = urllib2.Request(page_url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}) 
		resp = urllib2.urlopen(req)
	except Exception, e: 
		print e
		# print "Page %s can not be opened."%(page_url)
		return page_urls_list
	else:
		html = resp.read()
		soup = BeautifulSoup(html)
		anchors = soup.find_all('a')
		for i in anchors: # iterating over all anchor tags
			# print i
			try: a_href = i["href"] # dropping al javascript calls in <a>
			except: continue
			j = urlparse(a_href)
			if j.scheme=='' and j.netloc=='': # checking the whole url
				url_path = str(j.path).strip()
				if j.path!='':
					if url_path[0]=="/":
						k = base_url + url_path
					else:
						k = base_url + "/" + url_path
					if k not in page_urls_list:
						page_urls_list.append(k)
		print "Urls found - %d"%(len(page_urls_list))
		return page_urls_list
# https://www.linkedin.com/wvmx/profile/rankings?trk=wvmx-profile
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
# //www.cwi.nl:80/%7Eguido/Python.html
# https://www.facebook.com/tutorialspointindia
# https://www.facebook.com/directory/pages/
# http://www.treselle.com/careers/open-positions/python-developer/
# http://www.treselle.com/services/cloud-computing/
# 
# print crawlPage('http://www.treselle.com/services/big-data/')