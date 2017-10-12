import threading
from random import *
from enum import Enum

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

def EnergyType(En):
     """for cur in range(1,En):
"""
'''
def Valuation():

from thing_thread_ pool evaluation
if thing's type is unplugged (battery) : there is an increasing function
if thing's type in plugged : 0


'''



class Sponsor(threading.Thread):
    """


	"""

    def __init__(self):
        self.ID = randint(1000, 9999)
        self.application_thread_pool = []
        self.things_thread_pool = []

    def __lt__(self, other):
        return self.ID > other.ID


class Application(threading.Thread):
    """

	"""

    def __init__(self):
        self.ID = randint(1000, 9999)
        self.type = choice(['A','B','C','D'])
        self.things_thread_pool =[]
        self.evaluate()


    def evaluate(self):
        for cur in self.things_thread_pool:
            cur.value = randint(1, 11)

    def __lt__(self, other):
        return self.ID > other.ID

    def q(self):
        for cur1 in self.things_thread_pool:
            print(cur1.value)


class Thing(threading.Thread):
    """

	"""

    def __init__(self):
        self.ID = randint(1000, 9999)
        self.type = choice(['A','B','C','D'])
        self.value = 0
        self.EnType = 'Battery'

    def __lt__(self, other):
        return self.ID > other.ID




def Terminal(sponsors):
    bash = ""
    print("Plesae type  \"help\" to see how can you use the system ")
    while True:
        try:

            bash = input("command $ ")
            if bash == "":
                continue
            elif bash == "topo":
                if len(sponsors) == 0:
                    print("Nothing to show ! ")
                    continue
                for cur11 in sorted(sponsors):
                    print(
                        "||||||||||||||||||| Sponsor \"" + str(cur11.ID) + "\" has following thins |||||||||||||||||||")
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        print("---------------Application \"" + str(
                            cur.ID) + "\" has following thins -------------------")
                        for cur2 in sorted(cur.things_thread_pool):
                            print("Thing \"" + str(cur2.ID) + "\"")
                    print("---------------------------------------------------------------------------")
                print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

            elif bash == "create":
                bash = input("Which one do you wanna create ? \n1 ) Sponsors \n2 ) Application \n3 ) Things \n? ")

                if bash == "3":
                    if len(sponsors) < 1:
                        print("Sorry its supposed to have at least one sponsor")
                        continue

                    print("------------------- You have following Sponsor(s) ----------------------")
                    counter = 0
                    for cur in sorted(sponsors):
                        print(str(counter) + " ) " + str(cur.ID))
                        counter = counter + 1

                    print("--------------------------------------------------------------------------")
                    bash = input("Which sponsor you want to add thing on ? ")

                    try:
                        number_tmp4 = int(bash)
                        if not (number_tmp4 < len(sponsors) and (number_tmp4 > 0 or number_tmp4 == 0)):
                            print("The one that you chose is not in the list !")
                            continue
                        if len(sorted(sponsors)[number_tmp4].application_thread_pool) < 1:
                            print("Sorry its supposed to have at least one application in this sponsor")
                            continue

                        counter2 = 0
                        print("------------------- You have following Application(s) ----------------------")
                        for cur12 in sorted(sorted(sponsors)[number_tmp4].application_thread_pool):
                            print(str(counter2) + " ) " + str(cur12.ID))
                            counter2 = counter2 + 1

                        print("--------------------------------------------------------------------------")

                        bash = input("Which application you want to add thing on ? ")

                        try:
                            number_tmp2 = int(bash)
                            if not (number_tmp2 < len(sorted(sponsors)[number_tmp4].application_thread_pool) and (
                                    number_tmp2 > 0 or number_tmp2 == 0)):
                                print("The one that you chose is not in the list !")
                                continue
                            bash = input("How many things do you want to append ? ")
                            number_tmp3 = int(bash)
                            bash = input( "Percentage of Plugged Devices ? ")
                            pluged_num= int(bash)
                            if (pluged_num>100 or pluged_num<0):
                                print("you have to choose between 0 and 100")
                                continue

                            pluged_num =int((pluged_num*number_tmp3)/100)
                            counter1 = 0

                            for cur4 in range(0, number_tmp3):
                                t = Thing()
                                sorted(sponsors)[number_tmp4].things_thread_pool.append(t)
                                sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                    number_tmp2].things_thread_pool.append(t)


                            '''for cur5 in range(0,pluged_num):
                                sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                    number_tmp2].things_thread_pool.EnType = 'Plugged'
                            '''
                            for cur20 in sorted(sponsors):
                                for cur21 in sorted(cur20.application_thread_pool):
                                    for cur22 in sorted(cur21.things_thread_pool):
                                        while (counter1<pluged_num):
                                            cur22.EnType='plugged'
                                            counter1=counter1+1
                                            '''print(cur22.EnType)

                            print("--------------------------------------------------------------------------")

                            counter4 =pluged_num
                            for cur in sorted(sponsors):
                                for cur2 in sorted(cur.application_thread_pool):
                                    for cur3 in sorted(cur2.things_thread_pool):
                                        if(counter4<30):
                                            print(str(cur3.EnType))
                                            counter4 =counter4+1
                                        '''

                        except:
                            print("Error (5)")
                            print(sys.exc_info())
                            continue

                    except:
                        print("Error (10)")
                        print(sys.exc_info())
                        continue

                elif bash == "2":
                    if len(sponsors) < 1:
                        print("Sorry its supposed to have at least one sponsor")
                        continue

                    print("------------------- You have following Sponsor(s) ----------------------")
                    counter = 0
                    for cur in sorted(sponsors):
                        print(str(counter) + " ) " + str(cur.ID))
                        counter = counter + 1

                    print("--------------------------------------------------------------------------")
                    bash = input("Which sponsor you want to add application on ? ")

                    try:
                        number_tmp2 = int(bash)
                        if not (number_tmp2 < len(sponsors) and (number_tmp2 > 0 or number_tmp2 == 0)):
                            print("The one that you chose is not in the list !")
                            continue
                        bash = input("How many application(s) do you want to append ? ")
                        number_tmp3 = int(bash)
                        for cur4 in range(0, number_tmp3):
                            t = Application()
                            sorted(sponsors)[number_tmp2].application_thread_pool.append(t)

                        print("Done!")
                    except:
                        print("Error (8)")
                        print(sys.exc_info())
                        continue
                elif bash == "1":
                    bash = input("How many sponsor(s) do you want to append ? ")
                    number_tmp3 = int(bash)
                    for cur4 in range(0, number_tmp3):
                        t = Sponsor()
                        sponsors.append(t)
                    print("Done!")




                else:
                    print("Choose from the list please")
                    continue
                # elif bash.lower() == "load file" :
                # 	bash = input("Enter file path : ")
                # 	file  = open(bash)

            elif bash == "evaluate":

                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        print("---------------Application \"" + str(
                            cur.ID) + "\" has following thins -------------------")
                        for cur2 in sorted(cur.things_thread_pool):

                            print("Thing \"" + str(cur2.ID) + "\"")
                    print("---------------------------------------------------------------------------")

            elif bash == "help":
                print (" \"create\"  to create Sponsor/Application/Thing ")
                print (" \"topo\" to view designed system")
                print (" \"quit\" to exit from the system")
                print (" \"help\" to show more information about using the system" )





                    #for cur4 in range(0, number_tmp3):
                 #   t = Application()
                  #  sorted(sponsors)[number_tmp2].application_thread_pool.append(t)






                    # try :
                # 	file = open(bash)
            elif bash.lower() == "quit":
                break
            else:
                print("Wrong command ! ")
                continue
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    sponsors = []
    Terminal(sponsors)








