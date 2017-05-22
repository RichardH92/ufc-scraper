import io
import pycurl
import sherdog_parser

def scrape_url(url, socks_port):
	output = io.BytesIO()

	query = pycurl.Curl()
	query.setopt(pycurl.URL, url)
	query.setopt(pycurl.PROXY, 'localhost')
	query.setopt(pycurl.PROXYPORT, socks_port)
	query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
	query.setopt(pycurl.WRITEFUNCTION, output.write)

	try:
		query.perform()
		html = output.getvalue()
		return sherdog_parser.parse_sherdog_page(html)
	except pycurl.error as exc:
		return "Unable to reach %s (%s)" % (url, exc)