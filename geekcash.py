import json
import time
import matplotlib.pyplot as plt

raw_balance = 132 * 100000

data_file = "d:/aaa.txt";

class Transaction:
	def __init__(self, json_item):
		self.account_name = json_item['account']
		self.address = json_item['address']
		self.category = json_item['category']
		self.amount = json_item['amount']
		self.confirmations = json_item['confirmations']
		self.time = json_item['time']
		self.txid = json_item['txid']
		self.date_time = get_local_time(self.time)
		self.formated_time_str = get_formated_time_str(self.time)
		self.formated_day = get_formated_day_str(self.time)
		self.formated_month_day = "%d.%d" % (self.date_time.tm_mon, self.date_time.tm_mday)


def get_formated_time_str(timestamp):
	localtime = get_local_time(timestamp)
	ftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
	return ftime

def get_formated_day_str(timestamp):
	localtime = get_local_time(timestamp)
	ftime = time.strftime("%Y-%m-%d", localtime)
	return ftime

def get_local_time(timestamp):
	return time.localtime(timestamp)

def get_now_local_time():
	return time.localtime(time.time())


def parse_data(json_data):
	all_transactions = []
	for item in json_data:
		all_transactions.append(Transaction(item))
	return all_transactions



def get_total_reward():
	total_amount = 0
	for item in transaction_list:
		total_amount += item.amount
	return total_amount - raw_balance;


def get_time_passed_seconds_and_day():
	start_item = transaction_list[0]
	end_item = transaction_list[-1]
	passed_seconds = end_item.time - start_item.time
	passed_day = int(passed_seconds / 86400)
	return passed_seconds, passed_day

def get_reward_of_day():
	result = {}
	for item in transaction_list:
		if item.category != 'receive':
			if not item.formated_month_day in result:
				result[item.formated_month_day] = int(item.amount)
			else:
				result[item.formated_month_day] += int(item.amount)
	return result

def get_reward_of_month():
	result = {}
	for item in transaction_list:
		if item.category != 'receive':
			key = item.date_time.tm_mon
			if not key in result:
				result[key] = int(item.amount)
			else:
				result[key] += int(item.amount)
	return result


def show_reward_plot(reward_dict):
	keys = reward_dict.keys()
	values = reward_dict.values()

	plt.rcParams["font.sans-serif"] = ["KaiTi"]
	plt.rcParams['axes.unicode_minus'] = False
	
	plt.bar(range(len(values)), values, align = "center", color = "steelblue", alpha = 0.6)
	plt.xticks(range(len(keys)), keys)
	plt.title("GeekCash 主节点日收益")

	for x, y in enumerate(values):
		plt.text(x,y+300,'%s' % round(y,1), ha='center')# y+300 标签的坐标

	plt.show()



global transaction_list;

if __name__ == '__main__':
	# global transaction_list
	with open(data_file, 'r') as f:
		data = json.load(f);
		transaction_list = parse_data(data)
	
	total_reward = int(get_total_reward())
	print("total reward: ", total_reward)

	passed_seconds, passed_day = get_time_passed_seconds_and_day()
	print("passed seconds: ", passed_seconds, passed_day)

	reward_dict = get_reward_of_day();

	for key, value in reward_dict.items():
		print(key, value)

	show_reward_plot(reward_dict);

	reward_dict = get_reward_of_month()
	show_reward_plot(reward_dict)



# test_time = 1586869900

# localtime = time.localtime(test_time)
# now_localtime = time.localtime(time.time())

# ftime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
# print(ftime)
# print(localtime)
# print(now_localtime)

