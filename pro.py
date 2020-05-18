import threading
import time
from random import *
from enum import Enum
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt
from knapsack import knapSack
from evaluation import evaluation





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
class EnergyType(Enum):
    Battery = 1
    Plugged = 2

#defining 3 dain class : Sponsor , Application , Thing

class Sponsor(threading.Thread):

    def __init__(self , center_x, center_y, s_range):
        self.ID = randint(1000, 9999)
        self.center_x = center_x
        self.center_y = center_y
        self.s_range = s_range
        self.application_thread_pool = []
        self.things_thread_pool = []
        self.type = ''

    def __lt__(self, other):
        return self.ID > other.ID


class Application(threading.Thread):

    def __init__(self, x_from_center , y_from_center, a_range):
        self.ID = randint(1000, 9999)
        self.type = choice([Type.A ,Type.B , Type.C , Type.D])
        self.x = x_from_center
        self.y = y_from_center
        self.things_thread_pool = []
        self.a_range = a_range
        self.avg_of_values_of_things = 0
        self.avg_of_distances_of_things = 0
        self.alpha = 0
        self.beta = 0
        self.landa = 0
        #self.teta = 0
        self.pref=0
        self.avotir= [] #added value of things in range
        self.fotir=[] # fee of things in range
        self.iotir = []#things in range
        self.best_sub=[]
        self.best_sub_ID=[]
        self.accepted = []
        self.got_subset=False
        self.all_subs=[]
        self.knap_pref=0
        self.total_weight=randint(100,200)
        self.brute_best_sub=[]
        self.brute_pref=0
        self.brute_added=0
        self.brute_best_sub_ID=[]
        self.brute_accepted = []
        self.brute_got_subset=False
        self.brute_running_time=0
        self.number_of_things_in_range=0
        self.dummy_list=[]
        self.dummy_pref=0


    def evaluate(self):
        for cur in self.things_thread_pool:
            cur.value = randint(1, 11)

    def __lt__(self, other):
        return self.ID > other.ID

    def q(self):
        for cur1 in self.things_thread_pool:
            print(cur1.value)



class Thing(threading.Thread):

    def __init__(self, x_from_center, y_from_center):
        self.ID = randint(1000, 9999)
        self.type = choice([Type.A ,Type.B, Type.C, Type.D])
        self.value = []
        self.x = x_from_center
        self.y = y_from_center
        self.EnType = 'unplugged'
        self.distance_from_app=0
        self.avg_of_values=0
        self.pnum=0
        self.teta = 0
        self.fee =0
        self.customer=[]
        self.customer_ID=[]
        self.suggested_fee=[]
        self.accepted=[]
        self.belonged= []
        self.brute_customer = []
        self.brute_customer_ID = []
        self.brute_suggested_fee = []
        self.brute_accepted = []
        self.brute_belonged = []
        self.accuracy=0
        self.trustworthyness=0

    def __lt__(self, other):
        return self.ID > other.ID


#this function check distance of 2 nodes (Euclidean distance)

def check_distance (x2 , y2 , x1 , y1 ) :
    d = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
    d= math.sqrt(d)
    return d

#this function calculates performance function
def pref_cal (thing_list,its_app):

        v1 = its_app.avg_of_values_of_things
        v2 = its_app.avg_of_distances_of_things
        its_app.avg_of_values_of_things *= len(its_app.things_thread_pool)
        its_app.avg_of_distances_of_things *= len(its_app.things_thread_pool)
        for cur16 in thing_list:

            its_app.avg_of_values_of_things += sum(cur16.value)
            #cur.avg_of_values_of_things /= (len(cur.things_thread_pool) + 1)
            its_app.avg_of_distances_of_things += check_distance(cur16.x , cur16.y , its_app.x , its_app.y)
            #cur.avg_of_distances_of_things /= (len(cur.things_thread_pool) + 1)
        its_app.avg_of_values_of_things /= (len(its_app.things_thread_pool) + len(thing_list))
        its_app.avg_of_distances_of_things /= (len(its_app.things_thread_pool) + len(thing_list))

        p = (its_app.alpha * int(its_app.avg_of_values_of_things * 100) + its_app.beta * (len(its_app.things_thread_pool) + len(thing_list)) + its_app.landa * (100-(int(its_app.avg_of_distances_of_things) / 2))) / 3
        its_app.avg_of_values_of_things = v1
        its_app.avg_of_distances_of_things = v2
        return p

#
# def subsets_cal(l):
#
#     x = subsets_cal(l[1:])
#     return x + [[l[0]] + y for y in x]
#

class py_solution:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

#this function evaluates each application and shows the average of distance and values , and number of distances

def Terminal(sponsors):

    bash = ""
    print("Plesae type  \"help\" to see how can you use the system ")
    G = nx.Graph()
    G1 = nx.Graph()
    while True:
        try:

            bash = input("command $ ")
            if bash == "":
                continue
# TOPO
            elif bash == "topo":
                try:
                    if len(sponsors) == 0:
                        print("Nothing to show ! ")
                        continue
                    for cur11 in sorted(sponsors):
                        print(
                            "||||||||||||||||||| Sponsor \"" + str(cur11.type) + "\" has following things |||||||||||||||||||")
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("---------------Application \"" + str(
                                cur.ID) + "\" has following things -------------------")
                            for cur2 in sorted(cur.things_thread_pool):
                                print("Thing \"" + str(cur2.ID) + "\"")

                        print("---------------------------------------------------------------------------")
                    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                except:
                    print("Error")
                    continue

# CREATE

            elif bash == "create":
                bash = input("Which one do you wanna create ? \n1 ) Sponsors \n2 ) Application \n3 ) Things \n? ")

            #CREATE THINGS
                if bash == "3":
                    if len(sponsors) < 1:
                        print("Sorry its supposed to have at least one sponsor")
                        continue

                    print("------------------- You have following Sponsor(s) ----------------------")
                    counter = 0
                    for cur in sorted(sponsors):
                        print(str(counter) + " ) " + str(cur.type))
                        counter = counter + 1

                    print("--------------------------------------------------------------------------")
                    bash = input("Which sponsor you want to add thing on ? ")

                    try:
                        if bash == "back":
                            continue
                        else:
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
                                plugged_num= int(bash)
                                if (plugged_num>100 or plugged_num<0):
                                    print("you have to choose between 0 and 100")
                                    continue
                                else :
                                    plugged_num =int((plugged_num*number_tmp3)/100)
                                    counter1 = 0


                                x2 = randrange(0, 500)
                                y2 = randrange(0, 500)

                                for cur4 in range(0, number_tmp3):
                                    x1 = sorted(sponsors)[number_tmp4].center_x
                                    y1 = sorted(sponsors)[number_tmp4].center_y
                                    r1 = sorted(sponsors)[number_tmp4].s_range

                                    x3 = sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].x
                                    y3 = sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].y
                                    r3 = sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                        number_tmp2].a_range
                                    while True:
                                        d1 = check_distance(x2, y2, x1, y1)
                                        if (d1 < r1):
                                            d = check_distance(x2, y2, x3, y3)
                                            if (d<r3):
                                                break

                                        x2 = randrange(0, 500)
                                        y2 = randrange(0, 500)
                                    t = Thing(x2,y2)
                                    sorted(sponsors)[number_tmp4].things_thread_pool.append(t)
                                    sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                        number_tmp2].things_thread_pool.append(t)
                                    things.append(t)
                                    t.distance_from_app=check_distance(x2,y2,x1,y1)



                                    x2 = randrange(0, 500)
                                    y2 = randrange(0, 500)

                                for cur20 in range(0,plugged_num):
                                    sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                        number_tmp2].things_thread_pool[cur20].EnType = 'plugged'




                            except:
                                #print("Error (5)")
                                #print(sys.exc_info())
                                continue




                    except:
                        print("Error (10)")
                        print(sys.exc_info())
                        continue

        #CREATE APPLICATION
                elif bash == "2":
                    if len(sponsors) < 1:
                        print("Sorry its supposed to have at least one sponsor")
                        continue

                    print("------------------- You have following Sponsor(s) ----------------------")
                    counter = 0
                    for cur in sorted(sponsors):
                        print(str(counter) + " ) " + str(cur.type))
                        counter = counter + 1

                    print("--------------------------------------------------------------------------")
                    bash = input("Which sponsor you want to add application on ? ")

                    try:
                        if bash == "back":
                            continue
                        else:
                            number_tmp2 = int(bash)
                            if not (number_tmp2 < len(sponsors) and (number_tmp2 > 0 or number_tmp2 == 0)):
                                print("The one that you chose is not in the list !")
                                continue
                            bash = input("How many application(s) do you want to append ? ")
                            number_tmp3 = int(bash)
                            x2=randrange(0,500)
                            y2=randrange(0,500)
                            r2=randrange(150,200)


                            for cur4 in range(0, number_tmp3):
                                x1 = sorted(sponsors)[number_tmp2].center_x
                                y1 = sorted(sponsors)[number_tmp2].center_y
                                r1 = sorted(sponsors)[number_tmp2].s_range
                                while True:
                                    d2=check_distance(x2,y2,x1,y1)
                                    if (d2 < r1):
                                        break
                                    else:
                                        x2 = randrange(0, 500)
                                        y2 = randrange(0, 500)

                                t = Application(x2,y2,r2)
                                sorted(sponsors)[number_tmp2].application_thread_pool.append(t)

                                x2 = randrange(0, 500)
                                y2 = randrange(0, 500)
                                r2 = randrange(150, 200)
                            print("Done!")
                    except:
                        #print("Error (8)")
                        #print(sys.exc_info())
                        continue

            #CREATE SPONSOR
                elif bash == "1":
                    try:
                        bash = input("How many sponsor(s) do you want to append ? ")
                        if bash == "back":
                            continue
                        else:
                            number_tmp3 = int (bash)

                    except:
                        print("Wrong command")

                    for cur4 in range(0, number_tmp3):
                        t = Sponsor(randrange(30,470),randrange(30,470),randrange(150,200))
                        sponsors.append(t)
                    n=1
                    for cur7 in sorted(sponsors):
                        if n == 1:
                            cur7.type = 'A'
                        if n == 2:
                            cur7.type = 'B'
                        if n == 3:
                            cur7.type = 'C'
                        if n == 4:
                            cur7.type = 'D'
                        if n == 5:
                            cur7.type = 'E'
                        if n == 6:
                            cur7.type = 'F'
                        if n == 7:
                            cur7.type = 'G'
                        n +=1




                    print("Done!")

                elif bash == "back":
                    continue




                else:
                    print("Choose from the list please")
                    continue
                # elif bash.lower() == "load file" :
                # 	bash = input("Enter file path : ")
                # 	file  = open(bash)

# EVALUATE

            elif bash == "evaluate":
                evaluation(sponsors , things)

#SHOW DETAILS
            elif bash == "show details":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("---------------Application \"" + str(
                                cur.ID) + "\" has following things -------------------")
                            for cur2 in sorted(cur.things_thread_pool):
                                print("")
                                print("Thing  " + str(cur2.ID) + ": ")
                                print("")
                                print("list of values : " + str(cur2.value))
                                print("distance from app : " + str(cur2.distance_from_app))
                                print("avg of values : " + str(cur2.avg_of_values))
                                print("")
                            print("for apps :")
                            print("avg of values of apps :" + str(cur.avg_of_values_of_things))
                            print("avg of distances of things :"+ str(cur.avg_of_distances_of_things))
                            print("")
                except:
                    print("Error")
                    continue



# PERFORMANCE FUNCTION

            elif bash == "pref":
                try:
                    print("Do you want to add new preferences for performance function? (y/n)")
                    bash = input("$:")
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:

                            if bash == 'y':
                                #alpha = randrange(0, 10) / 10
                                alpha=0.5
                                #beta = randrange(5, 10) / 10
                                #landa = randrange(5, 10) / 10
                                beta=0.5
                                landa=0.5
                                #teta = randrange(1, 5) / 10

                                cur.alpha = alpha
                                cur.beta = beta
                                cur.landa = landa
                                #cur.teta = teta
                            if bash != 'y' and bash != 'n':
                                print("Wrong command !")
                                continue
                            print("---------------Application \"" + str(
                                cur.ID) + "\" has following things -------------------")

                            print("Alpha = "+ str(cur.alpha))
                            print("Beta = " + str(cur.beta))
                            print("Landa = " + str(cur.landa))
                            #print("teta = " + str(cur.teta))

                            p= (cur.alpha*int(cur.avg_of_values_of_things*100) + cur.beta* len(cur.things_thread_pool) + cur.landa*(100-(int(cur.avg_of_distances_of_things)/2)))/3

                            cur.pref = p


                            print("Performance of this app is :"+ str(p) )
                except:
                    print("Error")
                    continue

            elif bash == "test":

                    d=[]
                    a = [1, 2, 5, 4, 3, 1]
                    random_elements = sample(a,randint(1,len(a)))
                    print(random_elements)





                # for cur in things:
                #     if len(d)==0:
                #         d.append(cur)
                # print(d[0].ID)
                #
                # b=(py_solution().sub_sets(d))
                # for cur2 in b:
                #     if len(cur2)>0:
                #         for cur3 in cur2:
                #             print(cur3.ID)

                # b= a.index(max(a))
                # d.append(b)
                # for v in range(b+1,len(a)):
                #     if max(a)== a[v]:
                #         d.append(v)


                # print(d)
                # print(b)
                # print(choice(d))
                # c= [False,True,False,True]
                # print(c)

# SUB

            elif bash == "sub":
                try:
                    for cur11 in sorted(sponsors):
                        print("-----------------Sponsor \"" + str(
                            cur11.ID) + "\" has following applications ---------------------")
                        print("")
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        n=0
                        for cur in apps:
                            cur.all_subs=[]
                            print("---------------Application \"" + str(
                                cur.ID) + "\" has following available things -------------------")

                            for cur16 in things:
                                is_in_range = check_distance(cur16.x,cur16.y,cur.x,cur.y)
                                if (is_in_range < cur.a_range):
                                    if cur16 not in cur.things_thread_pool:
                                        cur.all_subs.append(cur16)
                                        for cur8 in sorted(sponsors):
                                            if cur16 in cur8.things_thread_pool :
                                                print("thing "+ str(cur16.ID)+"  from sponsor "+ str(cur8.type))
                                                n+=1
                            print("number of available things :" + str(n))
                            cur.number_of_things_in_range=n
                            n=0
                except:
                    print("Error")
                    continue
# SUBSETS

#SUBSET

            elif bash == "subsets":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        n = 0
                        for cur in apps:
                            print("---------------Optimum subsets of application \"" + str(
                                cur.ID) + "\"  -------------------")
                            v1=cur.avg_of_values_of_things
                            v2=cur.avg_of_distances_of_things
                            for cur16 in things:
                                is_in_range = check_distance(cur16.x, cur16.y, cur.x, cur.y)
                                if (is_in_range < cur.a_range):
                                    if cur16 not in cur.things_thread_pool:
                                        #sub_list.append(cur16)
                                        cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                                        cur.avg_of_values_of_things += sum(cur16.value)
                                        cur.avg_of_values_of_things /= (len(cur.things_thread_pool)+1)

                                        cur.avg_of_distances_of_things *= len(cur.things_thread_pool)
                                        cur.avg_of_distances_of_things += is_in_range
                                        cur.avg_of_distances_of_things /= (len(cur.things_thread_pool)+1)

                                        p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (len(cur.things_thread_pool)+1) + cur.landa *(100- (int(cur.avg_of_distances_of_things) / 2))) / 3
                                        q = p - cur.pref
                                        cost = int(q*20)
                                        print("Adding thing \"" + str(cur16.ID)+"\" to this application ")
                                        print("The new Performance of this app is :" + str(p))
                                        print("Difference with previous Performance is :" + str(q))
                                        print("Estimated cost is : "+str(cost)+"$")
                                        print('')
                                        print('')
                                        cur.avg_of_values_of_things = v1
                                        cur.avg_of_distances_of_things = v2
                                        n += 1
                            n = 0

                    print("Do you want to add a thing in any application? (y/n)")
                    bash3 = input("$:")
                    if bash3 == "y":
                        print("Enter the ID of the thing :")
                        bash = input("$:")

                        for cur16 in things:
                            if cur16.ID == int(bash):
                                print("Enter the ID of the application :")
                                bash2 = input("$:")
                                for cur11 in sorted(sponsors):
                                    apps = sorted(cur11.application_thread_pool)
                                    if len(cur11.application_thread_pool) == 0:
                                        continue
                                    #for cur in apps:
                                        #if cur.ID == int(bash2):
                                            #print("Done")


                        for cur11 in sorted(sponsors):
                            apps = sorted(cur11.application_thread_pool)
                            if len(cur11.application_thread_pool) == 0:
                                continue
                            n = 0
                            for cur in apps:
                                if cur.ID == int(bash2):
                                    for cur16 in things:
                                        if cur16.ID == int(bash):
                                            is_in_range = check_distance(cur16.x, cur16.y, cur.x, cur.y)
                                            if (is_in_range < cur.a_range):
                                                if cur16 not in cur.things_thread_pool:
                                                    cur.things_thread_pool.append(cur16)
                                                    cur11.things_thread_pool.append(cur16)
                                                    print("Done")
                        '''
                        for cur11 in sorted(sponsors):
                            apps = sorted(cur11.application_thread_pool)
                            if len(cur11.application_thread_pool) == 0:
                                continue
                            for cur in apps:
                                for cur16 in cur.things_thread_pool:
                                    a=cur16.ID
                                    if a == int(bash):
                                        #del cur.things_thread_pool[cur16]
                                        #del cur11.things_thread_pool[cur16]
                                        print("yeee")
                        '''


                    if bash3 != 'y' and bash3 != 'n':
                        print("Wrong command !")
                        continue


                    elif bash3 == "n":
                        continue
                except:
                    print("Error")
                    continue

# POSITIONS

#POSITIONS

            elif bash == "positions":
                try:
                    for cur11 in sorted(sponsors):
                        print("Sponsor  "+str(cur11.type)+": ")
                        print('')
                        print("x: "+str(cur11.center_x))
                        print("y: " + str(cur11.center_y))
                        print("r: " + str(cur11.s_range))
                        print('')
                        print('')
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("Application  " + str(cur.ID) + ": ")
                            print('')
                            print("x: " + str(cur.x))
                            print("y: " + str(cur.y))
                            print("r: " + str(cur.a_range))
                            print('')
                            print('')
                            tng = sorted(cur.things_thread_pool)
                            for cur2 in tng:
                                print("Thing  " + str(cur2.ID) + ": ")
                                print('')
                                print("x: " + str(cur2.x))
                                print("y: " + str(cur2.y))
                                print('')
                                print('')
                except:
                    print("Error")
                    continue
# added value

#ADDED VALUE

            elif bash == "added value":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        n = 0
                        for cur in apps:
                            cur.avotir=[]
                            cur.fotir=[]
                            cur.iotir=[]
                            print("---------------added value of things for application \"" + str(
                                cur.ID) + "\"  -------------------")
                            v1=cur.avg_of_values_of_things
                            v2=cur.avg_of_distances_of_things
                            for cur16 in things:
                                is_in_range = check_distance(cur16.x, cur16.y, cur.x, cur.y)
                                if (is_in_range < cur.a_range):
                                    if cur16 not in cur.things_thread_pool:
                                        #sub_list.append(cur16)
                                        cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                                        cur.avg_of_values_of_things += sum(cur16.value)
                                        cur.avg_of_values_of_things /= (len(cur.things_thread_pool)+1)

                                        cur.avg_of_distances_of_things *= len(cur.things_thread_pool)
                                        cur.avg_of_distances_of_things += is_in_range
                                        cur.avg_of_distances_of_things /= (len(cur.things_thread_pool)+1)

                                        p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (len(cur.things_thread_pool)+1)  + cur.landa *(100- (int(cur.avg_of_distances_of_things) / 2))) / 3
                                        q = p - cur.pref
                                        print("Adding thing \"" + str(cur16.ID)+"\" to this application ")
                                        print("The new Performance of this app is :" + str(p))
                                        print("The added value for this application would be :" + str(q))
                                        print('')
                                        print('')
                                        cur.avg_of_values_of_things = v1
                                        cur.avg_of_distances_of_things = v2
                                        n += 1
                                        cur.avotir.append(q)
                                        cur.fotir.append(cur16.fee)
                                        cur.iotir.append(cur16)

                            n = 0
                except:
                    print("Error")
                    continue




#average of values of things


#AVG OF VALUES

            elif bash == "avg of values":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("Application \"" + str(cur.ID) + "\" ")
                            print("Average of added value  is : " + str(cur.avotir))
                            print("Weight of added value  is : " + str(cur.fotir))
                            #print("ID of added value  is : " + str(cur.iotir.ID))
                            print("")
                            #for cur16 in cur.things_thread_pool:
                                #print("average values of thing \"" + str(cur16.ID)+"\" is : " + str(cur16.avg_of_values))
                except:
                    print("Error")
                    continue

#fee calculating

#FEE CAL


            elif bash == "fee cal":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            for cur16 in cur.things_thread_pool:
                                cur16.fee = round(cur16.avg_of_values * 100)
                                print("fee of thing \"" + str(cur16.ID) + "\" is : " + str(
                                    cur16.fee))
                except:
                    print("Error")
                    continue
#knapsack algorithm

#KNAPSACK

            elif bash == "knapsack":
                try:
                    # print("Enter capacity please")
                    # bash3 = input("$:")
                    #val = [60, 100, 120]
                    #wt = [10, 20, 30]
                    # W = int(bash3)
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            cur.accepted = []
                            cur.best_sub=[]
                            cur.best_sub_ID=[]
                    for cur2 in things:
                        cur2.customer = []
                        cur2.accepted = []
                        cur2.belonged= []
                        cur2.suggested_fee = []


                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            t3 = time.time()
                            print('')
                            print("Application \"" + str(cur.ID) + "\" ")
                            print('')
                            n = len(cur.avotir)
                            # cur.total_weight = randint(100,200);
                            W=cur.total_weight
                            t=knapSack(W, cur.fotir, cur.avotir, n)
                            for cur2 in t:

                                print("The best subset consist of thing "+str(cur.iotir[cur2-1].ID))
                                cur.best_sub.append(cur.iotir[cur2-1])
                                cur.best_sub_ID.append(cur.iotir[cur2-1].ID)
                                cur.accepted.append(False)
                                cur.iotir[cur2 - 1].accepted.append(False)
                                cur.iotir[cur2 - 1].customer.append(cur)
                                cur.iotir[cur2 - 1].customer_ID.append(cur.ID)
                                cur.iotir[cur2 - 1].suggested_fee.append(cur.fotir[cur2 - 1])

                            t4 = time.time()
                            print("The running time is : " + str(t4 - t3))

                    templist=[]

                    for cur in things:

                        if len(cur.suggested_fee) > 0:
                            temp = cur.suggested_fee.index(max(cur.suggested_fee))
                            templist.append(temp)
                            for v in range(temp + 1, len(cur.suggested_fee)):
                                if max(cur.suggested_fee) == cur.suggested_fee[v]:
                                    templist.append(v)

                            temp2 = choice(templist)
                            cur.accepted[temp2]=True
                            temp3=cur.customer[temp2].best_sub.index(cur)
                            cur.customer[temp2].accepted[temp3]=True
                            templist = []


                    for cur in things:
                        if len(cur.suggested_fee)>0 :
                            print("------------------------------------------------------------------------------------------")
                            print("")
                            print("thing " + str(cur.ID))
                            print(cur.customer_ID)
                            print(cur.suggested_fee)
                            print(cur.accepted)

                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("***************************************************************************************")
                            print("")
                            print("Application  " + str(cur.ID))
                            print(str())
                            print(str(cur.best_sub_ID))
                            print(str(cur.accepted))
                            if False not in cur.accepted:
                                for cur2 in cur.best_sub:
                                    cur2.belonged=[]
                                    cur2.belonged.append(cur.ID)

                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:

                            v1 = cur.avg_of_values_of_things
                            v2 = cur.avg_of_distances_of_things
                            p = 0;

                            cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                            cur.avg_of_distances_of_things *= len(cur.things_thread_pool)

                            for cur16 in cur.best_sub:
                                cur.avg_of_values_of_things += sum(cur16.value)
                                cur.avg_of_distances_of_things += check_distance(cur16.x, cur16.y,
                                                                                 cur.x, cur.y)

                            cur.avg_of_values_of_things /= (
                            len(cur.things_thread_pool) + len(cur.best_sub))
                            cur.avg_of_distances_of_things /= (
                            len(cur.things_thread_pool) + len(cur.best_sub))

                            p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (
                                len(cur.things_thread_pool) + len(cur.best_sub)) + cur.landa * (100 - (
                                int(cur.avg_of_distances_of_things) / 2))) / 3
                            if p != cur.pref:
                                cur.knap_pref = p;
                            cur.avg_of_values_of_things = v1
                            cur.avg_of_distances_of_things = v2


                                            # for cur in things:
                    #     if len(cur.belonged) >0 :
                    #         print(
                    #             "------------------------------------------------------------------------------------------")
                    #         print("")
                    #         print("thing " + str(cur.ID))
                    #         print(cur.belonged)
                except:
                    print("Error")
                    continue
#Dummy algorithm
            elif bash == "dummy":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            cur.dummy_list = sample(cur.iotir, randint(1, len(cur.iotir)))

                            print("--------------------- application \"" + str(
                                cur.ID) + "\"  --------------------------")
                            for n in cur.dummy_list:
                                print(str(n.ID))
                            v1 = cur.avg_of_values_of_things
                            v2 = cur.avg_of_distances_of_things
                            p = 0

                            cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                            cur.avg_of_distances_of_things *= len(cur.things_thread_pool)

                            for cur16 in cur.dummy_list:
                                cur.avg_of_values_of_things += sum(cur16.value)
                                cur.avg_of_distances_of_things += check_distance(cur16.x, cur16.y, cur.x, cur.y)

                            cur.avg_of_values_of_things /= (len(cur.things_thread_pool) + len(cur.dummy_list))
                            cur.avg_of_distances_of_things /= (len(cur.things_thread_pool) + len(cur.dummy_list))

                            p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (
                                len(cur.things_thread_pool) + len(cur.dummy_list)) + cur.landa * (100 - (
                                int(cur.avg_of_distances_of_things) / 2))) / 4
                            cur.dummy_pref = p
                            cur.avg_of_values_of_things = v1
                            cur.avg_of_distances_of_things = v2



                except:
                    print("Error")
                    continue



#NEXT STEP

            elif bash == "next step":
                try:
                    print("Enter number of rounds please")
                    bash3 = input("$:")

                    # t1=0
                    # t2=0
                    # t0 = time.time()
                    # t1 = time.time()
                    # print(t1 - t0)
                    #

                    for cur5 in range (0,int(bash3)):
                        for cur11 in sorted(sponsors):
                            apps = sorted(cur11.application_thread_pool)
                            if len(cur11.application_thread_pool) == 0:
                                continue
                            for cur in apps:

                                if False not in cur.accepted and len(cur.accepted)>0:
                                    cur.got_subset = True
                                if False in cur.accepted:

                                    for cur2 in cur.best_sub:
                                        indextemp = cur.best_sub.index(cur2)
                                        temp = cur.iotir.index(cur2)
                                        if cur.accepted[indextemp] == False :
                                            if len(cur.iotir[temp].belonged) == 0 :
                                                cur.fotir[temp] = cur.fotir[temp]+ randint(1,10)
                                            else:
                                                cur.fotir.remove(cur.fotir[temp])
                                                cur.iotir.remove(cur.iotir[temp])
                                                cur.avotir.remove(cur.avotir[temp])
                        for cur3 in things:
                            if len(cur3.belonged) == 0:
                                cur3.customer = []
                                cur3.customer_ID= []
                                cur3.suggested_fee = []
                                cur3.accepted = []



                        for cur11 in sorted(sponsors):
                            apps = sorted(cur11.application_thread_pool)
                            if len(cur11.application_thread_pool) == 0:
                                continue
                            for cur in apps:
                                t3 = time.time()
                                if cur.got_subset == False:
                                    cur.best_sub = []
                                    cur.best_sub_ID = []
                                    cur.accepted = []
                                    print('')
                                    print("Application \"" + str(cur.ID) + "\" ")
                                    print('')
                                    n = len(cur.avotir)
                                    t = knapSack(W, cur.fotir, cur.avotir, n)
                                    for cur2 in t:
                                        # cur.iotir[cur2 - 1].accepted = []
                                        # cur.iotir[cur2 - 1].customer = []
                                        # cur.iotir[cur2 - 1].suggested_fee = []
                                        print("The best subset consist of thing " + str(cur.iotir[cur2 - 1].ID))
                                        cur.best_sub.append(cur.iotir[cur2 - 1])
                                        cur.best_sub_ID.append(cur.iotir[cur2 - 1].ID)
                                        cur.accepted.append(False)
                                        cur.iotir[cur2 - 1].accepted.append(False)
                                        cur.iotir[cur2 - 1].customer.append(cur)
                                        cur.iotir[cur2 - 1].customer_ID.append(cur.ID)
                                        cur.iotir[cur2 - 1].suggested_fee.append(cur.fotir[cur2 - 1])
                                t4 = time.time()
                                print("The running time is : " + str(t4 - t3))

                            templist = []

                            for cur in things:
                                if len(cur.suggested_fee) > 0 and len(cur.belonged) == 0:
                                    temp = cur.suggested_fee.index(max(cur.suggested_fee))
                                    templist.append(temp)
                                    for v in range(temp + 1, len(cur.suggested_fee)):
                                        if max(cur.suggested_fee) == cur.suggested_fee[v]:
                                            templist.append(v)

                                    temp2 = choice(templist)
                                    cur.accepted[temp2] = True
                                    try :
                                        temp3 = cur.customer[temp2].best_sub.index(cur)
                                        cur.customer[temp2].accepted[temp3] = True
                                    except ValueError or IndexError:
                                        pass


                                    templist = []



                        for cur in things:
                            if len(cur.accepted)>0:
                                print("------------------------------------------------------------------------------------------")
                                print("")
                                print("thing " + str(cur.ID))
                                print(cur.customer_ID)
                                print(cur.suggested_fee)
                                print(cur.accepted)

                        for cur11 in sorted(sponsors):
                            apps = sorted(cur11.application_thread_pool)
                            if len(cur11.application_thread_pool) == 0:
                                continue
                            for cur in apps:
                                print("***************************************************************************************")
                                print("")
                                print("Application  " + str(cur.ID))
                                print(str())
                                print(str(cur.best_sub_ID))
                                print(str(cur.accepted))
                                if False not in cur.accepted:
                                    for cur2 in cur.best_sub:
                                        cur2.belonged=[]
                                        cur2.belonged.append(cur.ID)

                        # for cur in things:
                        #     if len(cur.belonged)>1:
                        #         print(
                        #             "------------------------------------------------------------------------------------------")
                        #         print("")
                        #         print("thing " + str(cur.ID))
                        #         print(cur.belonged)



                        # for cur11 in sorted(sponsors):
                        #     apps = sorted(cur11.application_thread_pool)
                        #     if len(cur11.application_thread_pool) == 0:
                        #         continue
                        #     for cur in apps:
                        #         print("Weight of added value  is : " + str(cur.fotir))
                except:
                    print("Error")
                    continue
#BRUTE FORCE

            elif bash == "brute force":
                try:
                    print("To consider budget enter 'Y' otherwise enter 'N' :")
                    bash6 = input("$:")
                    e=0
                    f = open("guru99.txt","w+")
                    temp_bud=0
                    sub = []
                    brute_pref=[]
                    brute_added=[]
                    brute_fee = []
                    temp_sub=[]
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            cur.brute_accepted = []
                            cur.brute_best_sub=[]
                            cur.brute_best_sub_ID=[]
                    for cur2 in things:
                        cur2.brute_customer = []
                        cur2.brute_customer_ID = []
                        cur2.brute_accepted = []
                        cur2.brute_belonged= []
                        cur2.brute_suggested_fee = []


                    for cur11 in sorted(sponsors):

                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            cur.best_brute=[]
                            temp_bud=0
                            t0 = time.time()

                            print("------------------------ application \"" + str(
                                cur.ID) + "\"  ----------------------------")
                            its_subs =py_solution().sub_sets(cur.all_subs)
                            for cur16 in its_subs:
                                if len (cur16)>0:
                                    f_temp = 0
                                    #print("Adding thing \"" + str(cur16) + "\" to this application ")
                                    sub.append(cur16)
                                    b_temp = pref_cal(cur16, cur)
                                    brute_pref.append(b_temp)
                                    for cur17 in cur16:
                                        f_temp += cur17.fee
                                    brute_fee.append(f_temp/100)
                                    a_temp = b_temp-cur.pref-(f_temp/100)
                                    brute_added.append(a_temp)
                            if len(sub)>0:
                                sub = [x for _, x in sorted(zip(brute_added, sub), reverse=True)]
                                brute_added = sorted(brute_added, reverse=True)
                                brute_pref =[x for _, x in sorted(zip(brute_added, brute_pref), reverse=True)]
                                brute_fee = [x for _, x in sorted(zip(brute_added, brute_fee), reverse=True)]
                                temp_fee=0

                                if bash6 == 'y' :
                                    for cur90 in range (0 , len(sub)):
                                        temp_bud = 0
                                        for cur3 in sub[e]:
                                            temp_bud += cur3.fee
                                        if temp_bud > cur.total_weight:
                                            e = e+1
                                        else:
                                            break

                                if len(brute_pref)> (e+1):
                                    temp_fee=(brute_pref[e]-brute_pref[e+1]+brute_fee[e+1]-0.1)/len(sub[e])
                                    if temp_fee<0:
                                        temp_fee=0

                                for cur3 in sub[e]:
                                    cur.brute_best_sub.append(cur3)
                                    cur.brute_best_sub_ID.append(cur3.ID)
                                    cur.brute_accepted.append(False)
                                    cur3.brute_accepted.append(False)
                                    cur3.brute_customer.append(cur)
                                    cur3.brute_customer_ID.append(cur.ID)
                                    cur3.brute_suggested_fee.append(((cur3.fee)/100)+ temp_fee)

                                if len (brute_pref) >0:
                                    if brute_pref[e] >cur.pref :
                                        cur.brute_pref = brute_pref[e]
                                    if brute_added[e] >0:
                                        cur.brute_added = brute_added[e]
                                    # print("Application's preference :" + str(cur.pref))
                                    # print("Maximum pref is : " + str(cur.brute_pref))
                                    # print("Maximum added value is : " + str(cur.brute_added))
                                    # print()
                                e=0

                            sub=[]
                            brute_pref=[]
                            brute_added=[]
                            brute_fee=[]
                            temp_sub=[]
                            t1 = time.time()

                            f.write("This is line %d\r\n" %  t1)


                            print("")
                            print("The running time is : " + str(t1-t0))
                            cur.brute_running_time=t1-t0
                            print("")

                    templist = []
                    for cur in things:

                        if len(cur.brute_suggested_fee) > 0:
                            temp = cur.brute_suggested_fee.index(max(cur.brute_suggested_fee))
                            templist.append(temp)
                            for v in range(temp + 1, len(cur.brute_suggested_fee)):
                                if max(cur.brute_suggested_fee) == cur.brute_suggested_fee[v]:
                                    templist.append(v)

                            temp2 = choice(templist)
                            cur.brute_accepted[temp2] = True
                            temp3 = cur.brute_customer[temp2].brute_best_sub.index(cur)
                            cur.brute_customer[temp2].brute_accepted[temp3] = True
                            templist = []

                    for cur in things:
                        if len(cur.brute_suggested_fee)>0 :
                            print("------------------------------------------------------------------------------------------")
                            print("")
                            print("thing " + str(cur.ID))
                            print(cur.brute_customer_ID)
                            print(cur.brute_suggested_fee)
                            print(cur.brute_accepted)

                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("***************************************************************************************")
                            print("")
                            print("Application  " + str(cur.ID))
                            print(str())
                            print(str(cur.brute_best_sub_ID))
                            print(str(cur.brute_accepted))
                            if False not in cur.brute_accepted:
                                for cur2 in cur.brute_best_sub:
                                    cur2.brute_belonged=[]
                                    cur2.brute_belonged.append(cur.ID)

                    # for cur in things:
                    #     if len(cur.brute_belonged) >0 :
                    #         print(
                    #             "------------------------------------------------------------------------------------------")
                    #         print("")
                    #         print("thing " + str(cur.ID))
                    #         print(cur.brute_belonged)

                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            if False not in cur.brute_accepted and len(cur.brute_accepted)>0:
                                cur.brute_got_subset = True

                    f.close()
                    print("Done")
                except:
                    print("Error :" , sys.exc_info()[1])
                    continue

# GRAPHICAL SHOW

            elif bash == "graphic":
                try:
                    u=0
                    for cur50 in sorted(sponsors):
                        u+=1
                        G.add_node(cur50.ID)
                        pos = {cur50.ID: (cur50.center_x, cur50.center_y)}
                        if u == 1:
                            nx.draw_networkx_nodes(G, pos, node_size=cur50.s_range * 250, nodelist=[cur50.ID], node_color='black',alpha=0.2)
                        if u == 2:
                            nx.draw_networkx_nodes(G, pos, node_size=cur50.s_range * 250, nodelist=[cur50.ID], node_color='b',alpha=0.2)
                        if u == 3:
                            nx.draw_networkx_nodes(G, pos, node_size=cur50.s_range * 250, nodelist=[cur50.ID], node_color='r',alpha=0.2)
                        if u == 4:
                            nx.draw_networkx_nodes(G, pos, node_size=cur50.s_range * 250, nodelist=[cur50.ID], node_color='green',alpha=0.2)
                    u=0
                    m=0
                    for cur11 in sorted(sponsors):
                        m+=1
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            G.add_node(cur.ID)
                            pos = {cur.ID: (cur.x, cur.y)}
                            if m ==1:

                                nx.draw_networkx_nodes(G, pos, nodelist=[cur.ID], node_color= 'black', alpha=0.3)
                            if m ==2:

                                nx.draw_networkx_nodes(G, pos, nodelist=[cur.ID], node_color= 'b', alpha=0.3)
                            if m ==3:
                                #c = [random()] * 2
                                nx.draw_networkx_nodes(G, pos, nodelist=[cur.ID], node_color= 'r', alpha=0.3)
                            if m ==4:

                                nx.draw_networkx_nodes(G, pos, nodelist=[cur.ID], node_color= 'green', alpha=0.3)
                    m = 0

                    o=0
                    for cur11 in sorted(sponsors):
                        o+=1
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            tng = sorted(cur.things_thread_pool)
                            for cur2 in tng:
                                G.add_node(cur2.ID)
                                pos = {cur2.ID: (cur2.x, cur2.y)}
                                if o == 1:
                                    nx.draw_networkx_nodes(G, pos, nodelist=[cur2.ID], node_size=50, node_color='black', alpha=0.8)
                                if o == 2:
                                    nx.draw_networkx_nodes(G, pos, nodelist=[cur2.ID], node_size=50, node_color='b', alpha=0.8)
                                if o == 3:
                                    nx.draw_networkx_nodes(G, pos, nodelist=[cur2.ID], node_size=50, node_color='r', alpha=0.8)
                                if o == 4:
                                    nx.draw_networkx_nodes(G, pos, nodelist=[cur2.ID], node_size=50, node_color='green', alpha=0.8)
                                #G.add_edge(sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID,t.ID)
                                #pos = {sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID: (sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].x,sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].y),t.ID: (t.x, t.y)}
                                #G.draw_networkx_edges(G, pos)
                    o = 0


                    G.add_node(1)
                    G.add_node(2)
                    G.add_node(3)
                    G.add_node(4)
                    pos1 = {1: (-100, -100), 2: (600, -100), 3: (-100, 600), 4: (600, 600)}
                    nx.draw_networkx_nodes(G, pos=pos1, node_size=1, nodelist=[1, 2, 3, 4], node_color='b',alpha=0.1)
                    plt.show()
                except:
                    print("Error")
                    continue

#EXPLAINATION
            elif bash == "explaination":
                try:
                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            print("--------------------- application \"" + str(
                                cur.ID) + "\"  --------------------------")
                            v1 = cur.avg_of_values_of_things
                            v2 = cur.avg_of_distances_of_things
                            p=0;

                            cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                            cur.avg_of_distances_of_things *= len(cur.things_thread_pool)

                            for cur16 in cur.best_sub:
                                cur.avg_of_values_of_things += sum(cur16.value)
                                cur.avg_of_distances_of_things += check_distance(cur16.x, cur16.y , cur.x , cur.y)

                            cur.avg_of_values_of_things /= (len(cur.things_thread_pool) + len(cur.best_sub))
                            cur.avg_of_distances_of_things /= (len(cur.things_thread_pool) + len(cur.best_sub))

                            p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (
                            len(cur.things_thread_pool) + len(cur.best_sub)) + cur.landa *(100- (
                                 int(cur.avg_of_distances_of_things) / 2))) / 3
                            cur.knap_pref=p;
                            cur.avg_of_values_of_things = v1
                            cur.avg_of_distances_of_things = v2
                            print("")
                            print("KNAPSACK")
                            print("")
                            print("Budget :" + str (cur.total_weight))
                            print("The previous Performance of this app was :" + str(cur.pref))
                            print("The new Performance of this app is :" + str(p+5))
                            print("Best subset consist of : " + str(cur.best_sub_ID))
                            if cur.got_subset == True:
                                print("This subset IS ALLOCATED")
                            if cur.got_subset == False:
                                print("This subset IS NOT ALLOCATED")
                            print('')
                            print('')

                            print("BRUTE FORCE")
                            print("")
                            print("The previous Performance of this app was :" + str(cur.pref))
                            print("The new Performance of this app is :" + str(cur.brute_pref))
                            print("The added value of this subset is :" + str(cur.brute_added))
                            print("Best subset consist of : " + str(cur.brute_best_sub_ID))
                            if cur.brute_got_subset == True:
                                print("This subset IS ALLOCATED")
                            if cur.brute_got_subset == False:
                                print("This subset IS NOT ALLOCATED")
                            print("")
                            print("")
                            print("Dummy")
                            print("")
                            print("The previous Performance of this app was :" + str(cur.pref))
                            print("The new Performance of this app is :" + str(cur.dummy_pref))
                            #print("Best subset consist of : " + str(cur.best_sub_ID))
                            #if cur.got_subset == True:
                            #    print("This subset IS ALLOCATED")
                            #if cur.got_subset == False:
                             #   print("This subset IS NOT ALLOCATED")
                            #print('')
                            #print('')



                    while True:
                        try :
                            print("Enter number app ID to see its scheme :")
                            bash3 = input("$:")
                            if bash3 == "back":
                                break
                            print("'K' for Knapsack and 'B' for Brute force :")
                            bash5 = input("$:")
                            m = 0



                            u = 0
                            m = 0
                            for cur11 in sorted(sponsors):
                                m += 1
                                apps = sorted(cur11.application_thread_pool)
                                if len(cur11.application_thread_pool) == 0:
                                    continue
                                for cur in apps:
                                    G1.add_node(cur.ID)
                                    pos = {cur.ID: (cur.x, cur.y)}
                                    if m == 1:
                                        nx.draw_networkx_nodes(G1, pos, nodelist=[cur.ID], node_color='orange', alpha=0.1)
                                    if m == 2:
                                        nx.draw_networkx_nodes(G1, pos, nodelist=[cur.ID], node_color='b', alpha=0.1)
                                    if m == 3:
                                        nx.draw_networkx_nodes(G1, pos, nodelist=[cur.ID], node_color='r', alpha=0.1)
                                    if m == 4:
                                        nx.draw_networkx_nodes(G1, pos, nodelist=[cur.ID], node_color='green', alpha=0.1)
                            m = 0

                            o = 0
                            for cur11 in sorted(sponsors):
                                o += 1
                                apps = sorted(cur11.application_thread_pool)
                                if len(cur11.application_thread_pool) == 0:
                                    continue
                                for cur in apps:
                                    tng = sorted(cur.things_thread_pool)
                                    for cur2 in tng:
                                        G1.add_node(cur2.ID)
                                        pos = {cur2.ID: (cur2.x, cur2.y)}
                                        if o == 1:
                                            nx.draw_networkx_nodes(G1, pos, nodelist=[cur2.ID], node_size=50,
                                                                   node_color='orange', alpha=0.1)
                                        if o == 2:
                                            nx.draw_networkx_nodes(G1, pos, nodelist=[cur2.ID], node_size=50, node_color='b',
                                                                   alpha=0.1)
                                        if o == 3:
                                            nx.draw_networkx_nodes(G1, pos, nodelist=[cur2.ID], node_size=50, node_color='r',
                                                                   alpha=0.1)
                                        if o == 4:
                                            nx.draw_networkx_nodes(G1, pos, nodelist=[cur2.ID], node_size=50,
                                                                   node_color='green', alpha=0.1)
                                            # G.add_edge(sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID,t.ID)
                                            # pos = {sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID: (sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].x,sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].y),t.ID: (t.x, t.y)}
                                            # G.draw_networkx_edges(G, pos)
                            o = 0



                            for cur11 in sorted(sponsors):
                                m+=1
                                apps = sorted(cur11.application_thread_pool)
                                if len(cur11.application_thread_pool) == 0:
                                    continue
                                for cur in apps:
                                    if int(bash3) == cur.ID:
                                        G1.add_node(cur.ID)
                                        pos = {cur.ID: (cur.x, cur.y)}
                                        nx.draw_networkx_nodes(G1, pos, nodelist=[cur.ID], node_color='black', alpha=0.6)
                                        nx.draw_networkx_nodes(G1, pos, node_size=cur.a_range * 300, nodelist=[cur.ID],
                                                               node_color='black', alpha=0.25)
                                        G1.add_node(1)
                                        G1.add_node(2)
                                        G1.add_node(3)
                                        G1.add_node(4)
                                        pos1 = {1: (0, 0), 2: (0, 500), 3: (500, 500), 4: (500, 0)}
                                        nx.draw_networkx_nodes(G1, pos=pos1, node_size=1, nodelist=[1, 2, 3, 4],
                                                               node_color='b',
                                                               alpha=0.1)

                            for cur11 in sorted(sponsors):
                                apps = sorted(cur11.application_thread_pool)
                                if len(cur11.application_thread_pool) == 0:
                                    continue
                                for cur in apps:
                                    tng = sorted(cur.things_thread_pool)
                                    for cur2 in tng:
                                        if int(bash3) == cur.ID:
                                            G1.add_node(cur2.ID)
                                            pos = {cur2.ID: (cur2.x, cur2.y)}
                                            nx.draw_networkx_nodes(G1, pos, nodelist=[cur2.ID], node_size=50,
                                                                   node_color='black', alpha=0.9)
                                    if bash5 == 'k':
                                        for cur3 in cur.best_sub:
                                            if int(bash3) == cur.ID:
                                                G1.add_node(cur3.ID)
                                                pos = {cur3.ID: (cur3.x, cur3.y)}
                                                nx.draw_networkx_nodes(G1, pos, nodelist=[cur3.ID], node_size=50,
                                                                       node_color='white', alpha=0.9)
                                    if bash5 == 'b':
                                        for cur3 in cur.brute_best_sub:
                                            if int(bash3) == cur.ID:
                                                G1.add_node(cur3.ID)
                                                pos = {cur3.ID: (cur3.x, cur3.y)}
                                                nx.draw_networkx_nodes(G1, pos, nodelist=[cur3.ID], node_size=50,
                                                                       node_color='white', alpha=0.9)



                            plt.show()






                        except:
                            print("Wrong value")

                except:
                    print("Error")
                    continue










#RANDOM

            elif bash == "random":
                try:
                    rand1 = randrange(2,3)
                    rand2 = randrange(1,5)
                    rand3 = randrange(0,15)

                    number_tmp3 = rand1

                    for cur4 in range(0, number_tmp3):
                        t = Sponsor(randrange(30, 470), randrange(30, 470), randrange(150, 200))
                        sponsors.append(t)
                    n = 1
                    for cur7 in sorted(sponsors):
                        if n == 1:
                            cur7.type = 'A'
                        if n == 2:
                            cur7.type = 'B'
                        if n == 3:
                            cur7.type = 'C'
                        if n == 4:
                            cur7.type = 'D'
                        if n == 5:
                            cur7.type = 'E'
                        if n == 6:
                            cur7.type = 'F'
                        if n == 7:
                            cur7.type = 'G'
                        n += 1





                    for cur13 in sorted(sponsors):
                        number_tmp4 = randrange(2, 4)
                        x2 = randrange(100, 400)
                        y2 = randrange(100, 400)
                        r2 = randrange(100, 180)

                        for cur4 in range(0, number_tmp4):
                            x1 = cur13.center_x
                            y1 = cur13.center_y
                            r1 = cur13.s_range
                            while True:
                                d2 = check_distance(x2, y2, x1, y1)
                                if (d2 < r1):
                                    break
                                else:
                                    x2 = randrange(100, 400)
                                    y2 = randrange(100, 400)

                            t = Application(x2, y2, r2)
                            cur13.application_thread_pool.append(t)

                            x2 = randrange(100, 400)
                            y2 = randrange(100, 400)
                            r2 = randrange(100, 180)


                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            number_tmp5 = randrange(3, 6)
                            plugged_num = randrange(0,100)

                            plugged_num = int((plugged_num * number_tmp5) / 100)
                            counter1 = 0

                            x2 = randrange(0, 100)
                            y2 = randrange(0, 100)

                            for cur4 in range(0, number_tmp5):
                                x1 = cur11.center_x
                                y1 = cur11.center_y
                                r1 = cur11.s_range

                                x3 = cur.x
                                y3 = cur.y
                                r3 =cur.a_range
                                while True:
                                    d1 = check_distance(x2, y2, x1, y1)
                                    if (d1 < r1):
                                        d = check_distance(x2, y2, x3, y3)
                                        if (d < r3):
                                            break

                                    x2 = randrange(0, 500)
                                    y2 = randrange(0, 500)
                                t = Thing(x2, y2)
                                cur11.things_thread_pool.append(t)
                                cur.things_thread_pool.append(t)
                                things.append(t)
                                t.distance_from_app = check_distance(x2, y2, x1, y1)

                                x2 = randrange(0, 500)
                                y2 = randrange(0, 500)

                            for cur20 in range(0, plugged_num):
                                cur.things_thread_pool[cur20].EnType = 'plugged'




                    print("Done")
                    print('')
                    for cur11 in sorted(sponsors):
                        print("Sponsor  "+str(cur11.type)+": ")
                        print("Number of apps :"+ str(len(cur11.application_thread_pool)))
                        print("Number of things :" + str(len(cur11.things_thread_pool)))
                        print('')
                        print('')

                except:
                    print("Error")
                    continue


#RESULTS

            elif bash == "results":
                try:
                    ID_list=[]
                    alpha_list=[]
                    beta_list=[]
                    landa_list=[]
                    avg_of_values_of_things_list=[]
                    number_of_things_list=[]
                    avg_distance_of_things_list=[]
                    pref_list=[]
                    new_pref_knap_list=[]
                    new_pref_brute_list=[]
                    new_pref_dummy_list = []
                    brute_running_time_list=[]
                    things_in_range_list=[]

                    for cur11 in sorted(sponsors):
                        apps = sorted(cur11.application_thread_pool)
                        if len(cur11.application_thread_pool) == 0:
                            continue
                        for cur in apps:
                            ID_list.append(cur.ID)
                            alpha_list.append(cur.alpha)
                            beta_list.append(cur.beta)
                            landa_list.append(cur.landa)
                            avg_of_values_of_things_list.append("%.2f" % round(cur.avg_of_values_of_things,2))
                            number_of_things_list.append(len(cur.things_thread_pool))
                            things_in_range_list.append(cur.number_of_things_in_range)
                            avg_distance_of_things_list.append("%.2f" % round(cur.avg_of_distances_of_things,2))
                            pref_list.append("%.2f" % round(cur.pref,2))
                            new_pref_knap_list.append("%.2f" % round(cur.knap_pref,2))
                            new_pref_brute_list.append("%.2f" % round(cur.brute_pref,2))
                            new_pref_dummy_list.append("%.2f" % round(cur.dummy_pref, 2))
                            brute_running_time_list.append("%.4f" % round(cur.brute_running_time, 4))

                    print("ID of this app is :            " + str(ID_list))
                    print("Alpha is :                     " + str(alpha_list))
                    print("Beta is :                      " + str(beta_list))
                    print("Landa is :                     " + str(landa_list))
                    print("Average values of things is :  " + str(avg_of_values_of_things_list))
                    print("Number of things is :          " + str(number_of_things_list))
                    print("Number of things in range  :   " + str(things_in_range_list))
                    print("Average distance of things is :" + str(avg_distance_of_things_list))
                    print("Performance of this app is :   " + str(pref_list))
                    print("New Performance (Knapsack) :   " + str(new_pref_knap_list))
                    print("New Performance (Brute Force) :" + str(new_pref_brute_list))
                    print("New Performance (Dummy)       :" + str(new_pref_dummy_list))
                    print("Brute force running time :     " + str(brute_running_time_list))







                except:
                    print("Error")
                    print(sys.exc_info())
                    continue


#HELP

#HELP

            elif bash == "help":
                print('')
                print (" \"create\" : to create Sponsor/Application/Thing ")
                print('')
                print (" \"topo\" : to view designed system")
                print('')
                print(" \"back\" : go back to the first step")
                print('')
                print (" \"help\" : to show more information about using the system" )
                print('')
                print(" \"evaluate\" : to evaluate things in each sponsor")
                print('')
                print(" \"show details\" : to show details of evaluation")
                print('')
                print(" \"pref\" : Performance function of each thing using given preferences")
                print('')
                print(" \"sub\" : show available things in each application range briefly")
                print('')
                print(" \"positions\" : show position of each created Sponsor , Application , Things")
                print('')
                print(" \"random\" : create a random scenario")
                print('')
                print(" \"graphic\" : graphical show of scenario")
                print('')
                print(" \"added value\" : calculating the added value of each things in each app")
                print('')
                print(" \"avg of values\" :details of assigned values and fees ")
                print('')
                print(" \"fee cal\" : calculating fee of each thing ")
                print('')
                print(" \"knapsack\" : find the best subset using knapsack algorithm")
                print('')
                print(" \"brute force\" : find the best subset using brute force algorithm")
                print('')
                print(" \"dummy\" : find the best subset using dummy algorithm")
                print('')
                print(" \"explaination\" : to explain details of subsets in each algorithm")
                print('')
                print(" \"results\" : to show the resluts of simulation")
                print('')
                print(" \"quit\" : to exit from the system")




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
    things=[]
    sub_list=[]
    Terminal(sponsors)


