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
	def __init__(self):
		self.ID = randint(0,999999)
		self.type = APPType.A
		self.application_thread_pool = []
		self.things_thread_pool = []

	def __lt__(self, other):
		return self.ID > other.ID


class Application(threading.Thread):
	"""

	"""
	def __init__(self):
		self.ID = randint(100000,999999)
		self.type = APPType.A
		self.things_thread_pool = []
		self.evaluate()
		

	def evaluate(self):
		for cur in self.things_thread_pool:
			cur.value = rt(1 , 11)

	def __lt__(self, other):
		return self.ID > other.ID

class Thing(threading.Thread):
	"""

	"""
	def __init__(self):
		self.ID = randint(100000,999999)
		self.type = Type.A
		self.value = 0

	def __lt__(self, other):
		return self.ID > other.ID


def Terminal(sponsors):

	bash = ""
	while True:
		try:
			bash = input("command $ ")
			if bash == "":
				continue
			elif bash == "topo":
				if len(sponsors) == 0 :
					print("Ooops! Nothing to show my lord!")
					continue
				for cur11 in sorted(sponsors):
					print("||||||||||||||||||| Sponsor \"" + str(cur11.ID) + "\" has following thins |||||||||||||||||||")
					apps = sorted(cur11.application_thread_pool)
					if len(cur11.application_thread_pool) == 0 : 
						continue
					for cur in apps:
						print("---------------Application \"" + str(cur.ID) + "\" has following thins -------------------")
						for cur2 in sorted(cur.things_thread_pool):
							print("Thing \"" + str(cur2.ID) + "\"")
					print("---------------------------------------------------------------------------")
				print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

			elif bash == "create" :
				bash = input("Which one do you wanna create ? \n1 ) Sponsors \n2 ) Application \n3 ) Things \n? ")

				if bash == "3" :
					if len(sponsors) < 1:
						print("Sorry its supposed to have at leat one sponsor")
						continue

					print ("------------------- You have following sponsor(s) ----------------------")
					counter = 0
					for cur in sorted(sponsors):
						print(str(counter) + " ) " + str(cur.ID) )
						counter = counter + 1

					print ("--------------------------------------------------------------------------")
					bash = input("Which sponsor you want to add thing on ? ")

					try:
						number_tmp4 = int(bash)
						if not(number_tmp4 < len(sponsors) and (number_tmp4 > 0 or number_tmp4 == 0 )):
							print("HA HA  :D i knew it! (9)")
							continue
						if len(sorted(sponsors)[number_tmp4].application_thread_pool) < 1:
							print("Sorry its supposed to have at leat one application in this sponsor")
							continue

						counter2 = 0
						print ("------------------- You have following sponsor(s) ----------------------")
						for cur12 in sorted(sorted(sponsors)[number_tmp4].application_thread_pool):
							print(str(counter2) + " ) " + str(cur12.ID) )
							counter2 = counter2 + 1

						print ("--------------------------------------------------------------------------")


						bash = input("Which application you want to add thing on ? ")

						try:
							number_tmp2 = int(bash)
							if not(number_tmp2 < len(sorted(sponsors)[number_tmp4].application_thread_pool) and (number_tmp2 > 0 or number_tmp2 == 0 )):
								print("HA HA  :D i knew it! (6)")
								continue
							bash = input("How many things do you want to append ? ")
							number_tmp3 = int(bash)
							for cur4 in range(0, number_tmp3):
								t = Thing()
								sorted(sponsors)[number_tmp4].things_thread_pool.append(t)
								sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].things_thread_pool.append(t)
							
						except:
							print("HA HA  :D i knew it! (5)")
							print(sys.exc_info())
							continue

					except:
							print("HA HA  :D i knew it! (10)")
							print(sys.exc_info())
							continue
					
				elif bash == "2":
					if len(sponsors) < 1:
						print("Sorry its supposed to have at leat one sponsor")
						continue

					print ("------------------- You have following Sponsor(s) ----------------------")
					counter = 0
					for cur in sorted(sponsors):
						print(str(counter) + " ) " + str(cur.ID) )
						counter = counter + 1

					print ("--------------------------------------------------------------------------")
					bash = input("Which sponsor you want to add application on ? ")

					try:
						number_tmp2 = int(bash)
						if not(number_tmp2 < len(sponsors) and (number_tmp2 > 0 or number_tmp2 == 0 )):
							print("HA HA  :D i knew it! (7)")
							continue
						bash = input("How many application(s) do you want to append ? ")
						number_tmp3 = int(bash)
						for cur4 in range(0, number_tmp3):
							t = Application()
							sorted(sponsors)[number_tmp2].application_thread_pool.append(t)

						print("Done!")
					except:
						print("HA HA  :D i knew it! (8)")
						print(sys.exc_info())
						continue
				elif bash == "1":
					bash = input("How many sponsor(s) do you want to append ? ")
					number_tmp3 = int(bash)
					for cur4 in range(0, number_tmp3):
						t = Sponsor()
						sponsors.append(t)
					print("Done!")

				else :
					print("Ha Ha :D (2)")
					continue
			# elif bash.lower() == "load file" : 
			# 	bash = input("Enter file path : ")
			# 	file  = open(bash)


				# try :
				# 	file = open(bash)
			elif bash.lower() == "q" :
				break
			else :
				print("Ha Ha :D (3)")
				continue
		except KeyboardInterrupt:
			break


if __name__ == '__main__':
	sponsors = []
	Terminal(sponsors)






















