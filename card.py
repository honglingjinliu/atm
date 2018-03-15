class Card:
	def __init__(self,cardNum,cardPwd,money):
		self.cardNum = cardNum
		self.cardPwd = cardPwd
		self.money = money

		self.status = False  #未锁定状态