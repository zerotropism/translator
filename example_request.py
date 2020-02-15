# importing the requests library 
import requests 

# defining the api-endpoint 
API_ENDPOINT = "http://localhost:8080"

# data to be sent to api 
data = {'text2translate': 'The Polish nobility enjoyed many rights that were not available to the noble classes of other countries and, typically, each new monarch conceded them further privileges. Those privileges became the basis of the Golden Liberty in the Polish–Lithuanian Commonwealth. Despite having a king, Poland was called the nobility\'s Commonwealth because the king was elected by all interested members of hereditary nobility and Poland was considered to be the property of this class, not of the king or the ruling dynasty. This state of affairs grew up in part because of the extinction of the male-line descendants of the old royal dynasty (first the Piasts, then the Jagiellons), and the selection by the nobility of the Polish king from among the dynasty\'s female-line descendants.'} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

print(r.text) 