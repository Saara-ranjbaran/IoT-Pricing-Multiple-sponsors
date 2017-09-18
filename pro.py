import threading
from enum import Enum
from random import randint 
import sys
class Type(Enum):
	A = 0
	B = 1
	C = 2
	D = 3

class APPType(Enum):
	A = 0
	B = 1
	C = 2
	D = 3

class Sponsor(threading.Thread):
	"""


	"""
	ID = randint(0,999999)
	type = APPType.A
	application_thread_pool = []
	things_thread_pool = []

	pass


class Apllication(threading.Thread):
	"""

	"""
	type = APPType.A
	things_thread_pool = []

	def __init__(self):
		self.evaluate()

	def evaluate(self):
		for cur in things_thread_pool:
			cur.value = rt(1 , 11)

	# def __gt__(self):
	# 	pass

class Thing(threading.Thread):
	"""

	"""
	ID = randint(0,999999)
	type = Type.A
	value = 0



def Terminal(sponsors):
	if len(sponsors) == 0:
		print("its suppoed you created at leat one sponsor!")
		return
	sponsor = sponsors[0]
	bash = ""
	while True:
		try:
			bash = input("command $ ")
			if bash == "":
				continue
			elif bash == "topo":
				apps = sorted(sponsor.application_thread_pool)
				for cur in apps:
					print ("Application \"" + cur.ID + "\" has following thins : ")
					for cur2 in cur.things_thread_pool:
						print("Thing \"" + ucr2.ID + "\"")
					print("-------------------------------------------------")

			elif bash == "create" :
				bash = input("create things or applications ? \n 1 ) things \n 2 ) Application ")

				if bash == "1" :
					if len(sponsor.application_thread_pool) < 1:
						print("Sorry its supposed to have at leat one application")
						continue

					bash = input("Which application you want to add thing on ? ")
					counter = 0
					for cur in sponsor.application_thread_pool:
						print(counter + " ) " + str(cur.ID) ) 

					try:
						bash = input("command $ ")
						number_tmp2 = int(bash)
						if not(number_tmp2 < len(sponsor.application_thread_pool) and (number_tmp2 > 0 or number_tmp2 == 0 )):
							print("HA HA  :D i knew it!")
							continue
						bash = input("How many things do you want to append ? ")
						number_tmp3 = int(bash)
						for cur4 in range(0, number_tmp3):
							t = Thing()
							sponsor.things_thread_pool.appned(t)
							sorted(sponsor.application_thread_pool)[number_tmp2].things_thread_pool.appned(t)

					except:
						print("HA HA  :D i knew it!")
						print(sys.info_exe())
						continue

					bash = input("How many things ? ")
					try:
						number_tmp = int(bash)
						for cur in range(0,number_tmp):
							sponsor.things_thread_pool.appned(Thing())
					except:
						print(sys.info_exe())
						continue
					

				elif bash == "2":
					sponsor.application_thread_pool.appned(Application())
					print("Woow! you just added new application ;)")
				else :
					print("Ha Ha :D ")
					continue
			elif bash.lower() == "q" :
				break
			else :
				print("Ha Ha :D")
				continue
		except:
			print("Ha Ha :D your first Tyr chtched!")
			continue


if __name__ == '__main__':
	sponsors = []
	sponsors.append(Sponsor())
	Terminal(sponsors)






















