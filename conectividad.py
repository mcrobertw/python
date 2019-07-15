import urllib.request  as urllib2 
try:
	#http://feeds.cristalab.com/clab
	#https://www.google.com/
	#http://reddit.com
	#http://congresorest.appspot.com/diputado
	f=urllib2.urlopen("http://congresorest.appspot.com/diputado/")
	print (f.read())
	f.close()
except urllib2.error.HTTPError as e:
	print ("Ocurrió un error")
	print (e.code)
except URLError as e:
	print ("Ocurrió un error")
	print (e.reason)