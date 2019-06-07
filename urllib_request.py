import urllib.request
import urllib.parse
url = "https://jsonplaceholder.typicode.com/todos/1"
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))




#url = 'http://myserver/post_service'
#data = urllib.urlencode({'name' : 'joe', 'age'  : '10'})
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#print response.read()
