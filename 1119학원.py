class Test:

	def __init__(self):
		self.msg=['1','2']
	def test(self,a):
		print("aaaaaaaaa")
		self.msg=self.msg + a
		return self.__q(a, a)
	def __q(self,a,b):
		b=['1']
		print("qqqqqqqqqqqq")
		self.msg = a + b
		self.help=self.msg + b
		return self.msg
	def intmsg(self, msg):
		self.msg1=self.msg 
		self.msg1=int(msg[1])
		return self.msg1
test = Test()
test.test(['5'])
print(test.msg)
print(test.help)
print(test.msg)
test.intmsg(test.msg)
print(test.msg)
print(test.msg1)