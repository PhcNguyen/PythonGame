# [IMPORT]
import os
import gspread
from KEY import DATA, OPEN_KEY
# [OPEN SHEET]
gc = gspread.service_account_from_dict(DATA)
sh = gc.open_by_key(OPEN_KEY)
wks = sh.sheet1
# [CODE]
def ListSheet():
	data_list = wks.get_all_values()
	del data_list[0]
	return data_list
def CheckLogin(username, password):
	data_list = ListSheet()
	for id in range(len(data_list)):
		user = data_list[id][1]
		pwd = data_list[id][2]
		if (username.lower() == user and password.lower() == pwd):
			return id + 1
	else:
		return 0
def CheckUser(user):
	data_list = ListSheet()
	for id in range(len(data_list)):
		userITD = data_list[id][1]
		if (user.lower() == userITD):
			return 0
	else:
		return 1
def CheckID(ID):
	data_list = ListSheet()
	for id in range(len(data_list)):
		iduser = data_list[id][0]
		username = data_list[id][1]
		if (ID == iduser):
			return username
	else:
		return 0
def SaveData(user, pwd):
	StartingCoin = 1000
	data_list = ListSheet()
	current = len(data_list) + 2
	wks.update_cell(current, 1, current - 1)
	wks.update_cell(current, 2, user)
	wks.update_cell(current, 3, pwd)
	wks.update_cell(current, 4, StartingCoin)
def CoinRepair(amount, id):
	if (amount > 1000000000):
		return 0
	data_list = ListSheet()
	cell = wks.cell(int(id) + 2, 4)
	Ncoin = int(data_list[id][3]) + int(amount)
	cell.value = Ncoin
	wks.update_cell(cell.row, cell.col, cell.value)
	return Ncoin
def ListOfAccount():
	data_list = ListSheet()
	if len(data_list) == 0:
		return 0
	MSG = []
	for i in range(len(data_list) - 1):
		id = data_list[i][0]
		user = data_list[i][1]
		text = f"{id}.{user}\n"
		MSG.append(text)
	MSG = ''.join(MSG)
	print(MSG)
	return 0
def LoadDataUser(id):
	data_list = ListSheet()
	user = data_list[id][1]
	coin = data_list[id][3]
	coin = int(coin)
	if (coin >= 1000):
		coin = f"{coin:,}"
	else:
		pass
	return user, coin
def LoadDataCoin(id):
	data_list = ListSheet()
	coin = data_list[id][3]
	coin = int(coin)
	return coin
def Charts(id):
	data_list = ListSheet()
	coin1 = 0 ; coin2 = 0 
	user1 = 0 ; user2 = 0
	for i in range(len(data_list)):
		Coin = LoadDataCoin(i)
		if (int(Coin) > int(coin1)):
			coin1 = data_list[i][3]
			user1 = data_list[i][1]
			Code = i
	for i in range(len(data_list)):
		Coin = LoadDataCoin(i)
		if i == Code:
			continue
		if (int(Coin) > int(coin2)):
			coin2 = data_list[i][3]
			user2 = data_list[i][1]
	return user1, user2, coin1, coin2,
