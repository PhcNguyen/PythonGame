# [IMPORT]
import os
import sys
import random
from time import sleep
try:
	import gspread, requests
except:
	os.system('pip install gspread')
	os.system('pip install requests')
import Menu
import System
# [CODE]
def Exit():
	os.sys.exit()
def Enter():
	a = input(" [Enter để tiếp tục] ")
def Clear():
	os.system("cls" if os.name == "nt" else "clear")
def Crossbar():
	for i in range(14):
		sys.stdout.write("▂▂▂▂")
	sys.stdout.write("\n")
def Loading(I):
	frames = ["\r[-->     ]", "\r[ -->    ]",
				"\r[  -->   ]", "\r[   -->  ]",
				"\r[    --> ]", "\r[     -->]"]
	for i in range(I, 0, -1):
		for frame in frames:
			sys.stdout.write(frame + str(i))
			sleep(0.125)
	sys.stdout.write(frames[-1])
	Clear()
def Space(Number):
	Space = ""
	for i in range(Number):
		Space += " " * i
	return Space
def MENU():
	Clear()
	Menu.Smenu()
	select = input(" CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: os.sys.exit,
		1: lambda: Register(),
		2: lambda: Login(),
		3: lambda: BXH(0),
		9: lambda: ChangeCoin()
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			Loading(3) 
			MENU()
	else:
		print(f" Vui Lòng Nhập Số !")
		Loading(3)
		MENU()
def Login():
	Clear()
	Menu.Slogin()
	username = input(" Account: ")
	if username.strip() == "":
		print(f"{Space(2)}Error !")
		print(f"{Space(2)}Auto exit enabled")
		Loading(3)
		MENU()
	password = input(" Password: ")
	id = System.CheckLogin(username, password)
	if (id == 0):
		print(" Đăng Nhập Thất Bại !")
		Loading(3)
		MENU()
	print(" Login Success !")
	id -= 1
	MenuMain(id)
def Register():
	def User():
		Clear()
		Menu.Sregister()
		user = input(" Account Name: ")
		user = user.lower()
		if (len(user) < 3):
			print(" Tên Quá Ngắn !")
			Loading(3)
			User()
		elif (len(user) > 10):
			print(" Tên Quá Dài !")
			Loading(3)
			User()
		ID = System.CheckUser(user)
		if (ID == 0):
			print(" Tên đã được sử dụng !")
			Loading(3)
			User()
		if (ID == 1):
			return user
	def Password(user):
		Clear()
		Menu.Sregister()
		print(f" Account Name: {user}")
		pwd = input(" Enter Password: ")
		if (len(pwd) < 3):
			print(" Pass Quá Ngắn !")
			Loading(3)
			Password(user)
		elif (len(pwd) > 10):
			print(" Pass Quá Dài !")
			Loading(3)
			Password(user)
		return pwd
	user = User()
	pwd = Password(user)
	System.SaveData(user, pwd)
	Loading(3)
	MENU()
def ChangeCoin():
	def Coin():
		Clear()
		Menu.SchangeCoin2()
		pwd = input(" Nhập Mật Khẩu: ")
		if (pwd != '12345'):
			MENU()
		id = input(" ID: ")
		Check = System.CheckID(id)
		if (Check == 0):
			print(" User not exists !!")
			Loading(3)
			ChangeCoin()
		print(f" User: {Check}")
		Continue = input(" Continue(y/n): ")
		if (Continue.lower() == 'y'):
			coin = input(" Coin: ")
			System.CoinRepair(coin, id)
		else:
			Loading(2)
			ChangeCoin()
	def List():
		Clear()
		Menu.SchangeCoin1()
		System.ListOfAccount()
		Enter()
		Loading(3)
		ChangeCoin()
	Clear()
	SchangeCoin()
	select = input(" CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: lambda: MENU(),
		1: lambda: List(),
		2: lambda: Coin(),
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			Loading(3)
			ChangeCoin()
	else:
		print(f" Vui Lòng Nhập Số !")
		Loading(3)
		ChangeCoin()
def MenuMain(id):
	Clear()
	Menu.Sbanner()
	user, coin = System.LoadDataUser(id)
	print(f" User: {user}          Coin: {coin} Xu")
	select = input(" CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: lambda: Exit(),
		1: lambda: XS(id),
		2: lambda: CoinMining(id),
		3: lambda: BXH(id),
		4: lambda: MenuMain(id),
		5: lambda: Dice(id)
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			Loading(2)
			MenuMain(id)
	else:
		print(f" Vui Lòng Nhập Số !")
		Loading(2)
		MenuMain(id)
def XS(id):
	Clear()
	def Check(id):
		Menu.SXs1()
		user, coin = System.LoadDataUser(id)
		coin = System.LoadDataCoin(id)
		if (coin < 0 or coin == 0):
			print(" Không đủ xu !")
			Loading(3)
			MenuMain(id)
		print(f" User: {user}{Space(4)}Coin: {coin} Xu")
		select = input(" CHỌN CỬA(1/2): ")
		if select.isdigit():
			select = int(select)
			if (select == 1):
				return 1 #Chan
			elif (select == 2):
				return 2 #Le
			else:
				print(f" Lựa Chọn Không Hợp Lệ !")
				Loading(3)
				XS(id)
		else:
			print(f" Vui Lòng Nhập Số !")
			Loading(3)
			XS(id)
	def Function(i):
		#i = 1 70chan 30le
		#i = 2 70le 30chan
		Percent = 0.7
		if i == 2:
			even_count = int( 100 * Percent)
			odd_count = 100 - even_count
		elif i == 1:
			odd_count = int( 100 * Percent)
			even_count = 100 - odd_count
		odd = [random.randrange(1, 99, 2) for _ in range(odd_count)]
		even = [random.randrange(2, 99, 2) for _ in range(even_count)]
		result_list = odd + even
		random.shuffle(result_list)
		return random.choice(result_list)
	def CoinBet(id, select):
		Clear()
		Menu.SXs2()
		select = int(select)
		user, coin = System.LoadDataUser(id)
		print(f" User: {user}{Space(4)}Coin: {coin} Xu")
		if (select == 1):
			title = f"Chẳn"
		else:
			title = f"Lẻ"
		print(f" Chọn : {title}")
		Bet = input(" Bet: ")
		if Bet.isdigit():
			Bet = int(Bet)
			coin = System.LoadDataCoin(id)
			if (Bet > coin or Bet < 0 or Bet == 0):
				print(" Cược Sai !!")
				Loading(2)
				CoinBet(id, select)
			else:
				return Bet
		else:
			print(f" Vui Lòng Nhập Số !")
			Loading(2); CoinBet(id, select)
	def Spin(id, num):
		crossbar1 = "\n    ╔══════════╗"
		crossbar2 = "\n    ╚══════════╝\n"
		delay = 0.002
		print(crossbar1)
		while delay < 0.1:
			num = (num % 98) + 1 
			sys.stdout.write(f"\r    ║ -> {num:02d} <- ║")
			sys.stdout.flush()  
			sleep(delay)
			delay += 0.001
		print(crossbar2)
	def Reward(id, Se, Be, Nu):
		TitleWin = f" Chúc mừng chiến thắng !"
		TitleLose = f" Chúc may mắn lần sau !"
		if (Se == 1 and Nu % 2 == 0):
			print(TitleWin)
			System.CoinRepair(Be, id)
			print(f"Coin: +{Be} Xu\n")
		elif (Se == 2 and Nu % 2 != 0):
			print(TitleWin)
			System.CoinRepair(Be, id)
			print(f"Coin: +{Be} Xu\n")
		elif (Se == 1 and Nu % 2 != 0):
			print(TitleLose)
			System.CoinRepair(-Be, id)
			print(f"Coin: -{Be} Xu\n")
		elif (Se == 2 and Nu % 2 == 0):
			print(TitleLose)
			System.CoinRepair(-Be, id)
			print(f"Coin: -{Be} Xu\n")
	select = Check(id)
	Bet = CoinBet(id, select)
	num = Function(select)
	Spin(id, num)
	Reward(id, select, Bet, num)
	Enter()
	MenuMain(id)
def CoinMining(id):
	Clear()
	Menu.Scoinmining()
	user, coin = System.LoadDataUser(id)
	print(f" User: {user}{Space(4)}Coin: {coin} Xu")
	blocks = input(f" Nhập Số Block Đào: ")
	coinlist = list(range(200, 3000, 200))
	if blocks.isdigit():
		for i in range(int(blocks)):
			blockchain = random.randint(10, 50)
			nimed = 0
			difficulty = random.randint(3000, 3500)
			A = blockchain * difficulty
			for _ in range(A):
				nimed += 1 
				sys.stdout.write(f"\r[{i}] Mine: {nimed:06d}")
				sleep(0)
			mined_coin = random.choice(coinlist)
			System.CoinRepair(mined_coin, id)
			user, coin = System.LoadDataUser(id)
			print(f"\n[{i}] +{mined_coin} Xu | Tổng: {coin} Xu\n")
		Loading(5)
		MenuMain(id)
	elif blocks.lower() == 'n':
		MenuMain(id)
	else:
		print(f" Vui Lòng Nhập Số !!")
		Loading(3)
		CoinMining(id)
def BXH(id):
	Clear()
	User, user, Coin, coin = System.Charts(id)
	Menu.Scharts(1, User, Coin)
	Menu.Scharts(2, user, coin)
	Enter()
	if (id == 0):
		MENU()
	else:
		MenuMain(id)
def Dice(id):
	def Check(id):
		user, coin = System.LoadDataUser(id)
		coin = System.LoadDataCoin(id)
		if (coin < 0 or coin == 0):
			print(" Không Đủ Xu !!")
			Loading(3)
			MenuMain(id)
	def Select(id):
		Clear()
		Menu.Sdice()
		Select = input(" Chọn Cửa: ")
		if Select.isdigit():
			Select = int(Select)
			if (Select == 0):
				MenuMain(id)
			elif (Select > 0.9 and Select < 4.1):
				return Select
			else:
				print(" Số Nhập Không Hợp Lệ !!")
				Loading(3)
				Dice(id)
		else:
			print(" Vui Lòng Nhập Số !!")
			Loading(3)
			Dice(id)
	def BetCoin(id, Select):
		XP = {
			1: 'Tài', 2: 'Xỉu',
			3: 'Chẳn', 4: 'Lẻ'
		}
		Clear()
		Menu.SXs2()
		user, coin = System.LoadDataUser(id)
		print(f" User: {user}{Space(4)}Coin: {coin} Xu")
		print(f" Chọn: {XP[Select]}")
		Bet = input(" Bet: ")
		if Bet.isdigit():
			Bet = int(Bet)
			coin = System.LoadDataCoin(id)
			if (Bet > coin or Bet == 0 or Bet < 0):
				print(" Cược Sai !!")
				Loading(3)
				BetCoin(id)
			else:
				return Bet
		else:
			print(" Vui Lòng Nhập Số !!")
			Loading(3)
			BetCoin(id)
	def Dice_icons():
		Dice_icon = {
		1: '⚀', 2: '⚁', 3: '⚂',
		4: '⚃', 5: '⚄', 6: '⚅'
		}
		Numbers = random.sample(range(1,7), 3)
		Number = Numbers
		List = []
		for i in Numbers:
			List.append(Dice_icon[i])
		Numbers = sum(Numbers)
		return Numbers, List, Number
	def CheckDice(Select, Numbers):
		def check_condition(Numbers, conditions):
			return Numbers in conditions
		conditions = {
			1: [11, 12, 13, 14, 15, 16, 17],  # Tai
			2: [4, 5, 6, 7, 8, 9, 10],        # Xiu
			3: [4, 6, 8, 10, 12, 14, 16, 18], # Chan
			4: [3, 5, 7, 9, 11, 13, 15, 17]   # Le
		}
		if Select in conditions:
			return int(check_condition(Numbers, conditions[Select]))
		else:
			return 2
	def Reward(id, Bet, Return):
		win = " Chúc Mừng Bạn Đã Thắng !"
		loss = " Chúc Bạn May Mắn Lần Sau !"
		if (Return == 1):
			System.CoinRepair(Bet, id)
			return win
		elif (Return == 0):
			System.CoinRepair(-Bet, id)
			return loss
		elif (Return == 2):
			return " [ERROR] Liên Hệ Admin !!"
	def Print(List, Number):
		Lst = []
		for dice in List:
				X = (f"  {dice}  ")
				Lst.append(X)
		i = 0
		for num in Number:
			Lst.insert(i, num)
			i += 2
		print(' '.join(map(str, Lst)))
	List = {
			1: 'Tài', 2: 'Xỉu',
			3: 'Chẳn', 4: 'Lẻ'
		}
	Check(id)
	Select = Select(id)
	Bet = BetCoin(id, Select)
	Numbers, List, Number = Dice_icons()
	XI = CheckDice(Select, Numbers)
	Print(List, Number)
	print(f"Kết Quả: {Numbers}")
	Jk = Reward(id, Bet, XI)
	print(Jk)
	Enter()
	MenuMain(id)
Clear()
MENU()