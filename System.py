# [IMPORT]
import os
import gspread
from threading import Thread
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
	data_list = ListSheet()
	current = len(data_list) + 2
	wks.update_cell(current, 1, current - 1)
	wks.update_cell(current, 2, user)
	wks.update_cell(current, 3, pwd)
	wks.update_cell(current, 4, 1000)
def CoinRepair(amount, id):
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
		id1 = data_list[i+1][0]
		user1 = data_list[i+1][1]
		space = 12 - int(len(user))
		text = f"{id}.{user}{' '*space}{id1}.{user1}"
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