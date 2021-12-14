import requests
import json


def getScopes(status=1,type=1):
	"""[+] usage:
	status 0 -> deactive programs
	status 1 -> active programs
	--------------------------
	type 1 -> Web Applications
	type 2 -> Applications
	type 3 -> Mobile Applications
	type 4 -> Hardware
	type 5 -> Other
	"""
	data_raw = '{"operationName":"companies","variables":{"offset":0,"limit":100,"order":"createdAt","direction":"desc","search":"","status":' +str(status)+ ',"type":' +str(type)+ '},"query":"query companies($offset: Int\u0021, $limit: Int\u0021, $search: String, $status: Int, $type: Int, $order: String, $direction: String) {\\n  companies(\\n    pagination: {limit: $limit, offset: $offset}\\n search: $search\\n order: {field: $order, direction: $direction}\\nfilters: {status: $status, type: $type}\\n){\\nrows{\\nid\\nrealname\\nemail\\nname\\navatar\\nhunts\\nrewards\\nactiveReports\\n}\\n}\\n}\\n"}'
	response = requests.post(url=api_url, data=data_raw, headers=headers)
	result = json.loads(response.text)['data']['companies']['rows']

	for item in result:
		if item.get('name') in ('comp1', 'VIP_2'):
			del result[result.index(item)]

	return result


def getDetails(name):
	data_raw = '{"operationName":"userDetails","variables":{"username":"'+str(name)+'"},"query":"query userDetails($username: String\u0021) {\\n  user(username: $username, type: \\"company\\") { realname\\n    website\\n    name}\\n}\\n"}'
	response = requests.post(url=api_url, data=data_raw, headers=headers)
	result = json.loads(response.text)['data']['user']
	return result


def main():
	"""
	*** This process may take some time ****
	_________________________________
	  Give me morale :)
	- Twitter: https://twitter.com/ReymoRed
	- Instagram: https://instagram.com/ReymoRed
	"""
	Scopes=getScopes()
	urls = []
	for item in Scopes:
		urls.append(getDetails(item.get('name')))

	print(list(urls))

if __name__ == '__main__':
	api_url= 'https://www.ravro.ir/api/graphql'
	headers={'Content-Type': 'application/json', 'origin': 'https://www.ravro.ir'}
	main()
