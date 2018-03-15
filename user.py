class User:
	def __init__(self,name,idCard,phone,cardInfo):
		self.name = name
		self.idCard = idCard
		self.phone = phone
		
		self.cardInfo = cardInfo #用户开卡信息(卡对象)
