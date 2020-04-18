import requests
import json
import time

url = 'https://explorer.geekcash.org/mn/fetch'

headers = {
	"Host": "explorer.geekcash.org",
	"Content-Type": "application/json",
}

# request_data = {"page":2,"offset":50,"pageSize":50,"limit":50,"search":"","sort":[]}

# x = requests.post(url, data = json.dumps(request_data), headers = headers)

# json_data = json.loads(x.text)

# # print(json_data)
# print(json_data["totalDocs"])
# print(json_data["totalPages"])

page_size = 50;


def get_summary_data():
	request_data = {"page":1,"offset":0,"pageSize":50,"limit":50,"search":"","sort":[]}
	x = requests.post(url, data = json.dumps(request_data), headers = headers)
	json_data = json.loads(x.text)

	totalPages = json_data["totalPages"]



def download_data_of_page(page):
	offset = (page - 1) * page_size;
	request_data = {"page": page, "offset": offset,"pageSize":page_size,"limit":page_size,"search":"","sort":[]}
	x = requests.post(url, data = json.dumps(request_data), headers = headers)
	json_data = json.loads(x.text)

	file_path = "d:/mn/%d.json" % page

	with open(file_path, 'w') as f:
		f.write(x.text)

	has_next_page = json_data["hasNextPage"]
	print("CurrentPage: ", page, " HasNextPage: ", has_next_page)
	return has_next_page


if __name__ == '__main__':
	curr_page = 1
	has_next_page = download_data_of_page(curr_page)
	time.sleep(1)
	while has_next_page:
		curr_page += 1
		has_next_page = download_data_of_page(curr_page)
		time.sleep(1)

