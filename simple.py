from bs4 import BeautifulSoup
import urllib.request as urllib2

def main():
	bad_tags = ["fees"]
	
	privacy_tags = ["privacy"]	
	
	url = "https://www.jetblue.com/legal/flights-terms"
	
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, features="html.parser")
	
	bad_urls = []
	
	for line in soup.get_text().split("."):
		for tag in bad_tags:
			if tag.strip() in line.strip() and "[" not in line and "{" not in line and "/" not in line and line.strip() not in bad_urls:
				bad_urls.append(line.strip())
	
	for url in bad_urls:
		print(url)
		print("\n")
	
if __name__ == '__main__':
    main()
