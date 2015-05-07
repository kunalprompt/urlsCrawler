from one_page_crawler import crawlPage

urls_list = []
def main():
	global urls_list
	url_to_crawl = raw_input("Enter URL to crawl\n")
	urls_list.append(url_to_crawl)
	current_index = 0
	while(current_index<len(urls_list)):
		print "--------------------------------------------------------------------------"
		print "Current Index - %d  Total Unique URLs - %d"%(current_index+1, len(urls_list))
		fetched_urls = crawlPage(urls_list[current_index])
		for a_url in fetched_urls:
			if a_url not in urls_list:
				urls_list.append(a_url)
		current_index+=1
	print "-------------------------------------------------------------------------------"
	print "URL parsed - %s"%(url_to_crawl)
	print "Total Unique URLs Found - %d"%(len(urls_list))
	print urls_list
if __name__=="__main__":
	try: main()
	except KeyboardInterrupt:
		print "-------------------------------------------------------------------------------"
		print "KeyboardInterrupt"
		print urls_list
		exit(0)