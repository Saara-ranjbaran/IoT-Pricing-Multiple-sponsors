import threading
from random import *
from enum import Enum
import math
import sys
import networkx as nx
import matplotlib.pyplot as plt


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
        self.pref=0


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

    def __lt__(self, other):
        return self.ID > other.ID


#this function check distance of 2 nodes (Euclidean distance)

def check_distance (x2 , y2 , x1 , y1 ) :
    d = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
    d= math.sqrt(d)
    return d

#this function evaluates each application and shows the average of distance and values , and number of distances

def evaluation():
    h = 0
    v = 0
    if len(sponsors) == 0:
        print("Nothing to show ! ")
    for cur11 in sorted(sponsors):
        print(
            "||||||||||||||||||| Sponsor \"" + str(
                cur11.type) + "\" has following Apps |||||||||||||||||||")
        apps = sorted(cur11.application_thread_pool)
        if len(cur11.application_thread_pool) == 0:
            continue
        for cur in apps:
            for cur9 in sorted(cur.things_thread_pool):
                cur9.avg_of_values = 0
            cur.avg_of_values_of_things = 0
            cur.avg_of_distances_of_things = 0



        for cur in apps:

            for cur3 in range(0, len(things)):
                things[cur3].value.append(uniform(0, 1))

        for cur in apps:
            p1=0
            print("---------------Application \"" + str(
                cur.ID) + "\" has following things -------------------")
            for cur5 in sorted(cur.things_thread_pool):
                cur5.avg_of_values = sum(cur5.value) / len(cur5.value)
            for cur4 in sorted(cur.things_thread_pool):
                cur.avg_of_values_of_things += cur4.avg_of_values
            for cur3 in sorted(cur.things_thread_pool):
                if (cur3.EnType == 'unplugged'):
                    p1+=1

            if (len(cur.things_thread_pool) != 0):
                cur.avg_of_values_of_things /= len(cur.things_thread_pool)
            for cur5 in sorted(cur.things_thread_pool):
                cur.avg_of_distances_of_things += cur5.distance_from_app
            if (len(cur.things_thread_pool) != 0):
                cur.avg_of_distances_of_things /= len(cur.things_thread_pool)

            cur.pnum=p1
            print("Average of values :" + str(cur.avg_of_values_of_things))
            print("Number of things :" + str(len(cur.things_thread_pool)))
            print("Average of distance :" + str(cur.avg_of_distances_of_things))
            print("Number of unplugged devices :"+ str(p1))
            print('')




def Terminal(sponsors):
    bash = ""
    print("Plesae type  \"help\" to see how can you use the system ")
    G = nx.Graph()
    while True:
        try:

            bash = input("command $ ")
            if bash == "":
                continue
# TOPO
            elif bash == "topo":
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
                                pluged_num= int(bash)
                                if (pluged_num>100 or pluged_num<0):
                                    print("you have to choose between 0 and 100")
                                    continue
                                else :
                                    pluged_num =int((pluged_num*number_tmp3)/100)
                                    counter1 = 0
                                print(pluged_num)

                                x2 = randrange(0, 100)
                                y2 = randrange(0, 100)

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

                                        x2 = randrange(0, 100)
                                        y2 = randrange(0, 100)
                                    t = Thing(x2,y2)
                                    sorted(sponsors)[number_tmp4].things_thread_pool.append(t)
                                    sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                        number_tmp2].things_thread_pool.append(t)
                                    things.append(t)
                                    t.distance_from_app=check_distance(x2,y2,x1,y1)



                                    x2 = randrange(0, 100)
                                    y2 = randrange(0, 100)

                                for cur20 in range(0,pluged_num):
                                    sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                                        number_tmp2].things_thread_pool[cur20].EnType = 'pluged'




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
                            x2=randrange(0,100)
                            y2=randrange(0,100)
                            r2=randrange(15,40)



                            for cur4 in range(0, number_tmp3):
                                x1 = sorted(sponsors)[number_tmp2].center_x
                                y1 = sorted(sponsors)[number_tmp2].center_y
                                r1 = sorted(sponsors)[number_tmp2].s_range
                                while True:
                                    d2=check_distance(x2,y2,x1,y1)
                                    if (d2 < r1):
                                        break
                                    else:
                                        x2 = randrange(0, 100)
                                        y2 = randrange(0, 100)

                                t = Application(x2,y2,r2)
                                sorted(sponsors)[number_tmp2].application_thread_pool.append(t)

                                x2 = randrange(0, 100)
                                y2 = randrange(0, 100)
                                r2 = randrange(15, 40)

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
                        t = Sponsor(randrange(30,70),randrange(30,70),randrange(10,30))
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
                evaluation()
#SHOW DETAILS
            elif bash == "show details":
                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        print("---------------Application \"" + str(
                            cur.ID) + "\" has following things -------------------")
                        for cur2 in sorted(cur.things_thread_pool):
                            print("list of values : " + str(cur2.value))
                            print("distance from app : " + str(cur2.distance_from_app))
                            print("avg of values : " + str(cur2.avg_of_values))
                        print("for apps :")
                        print("avg of values of apps :" + str(cur.avg_of_values_of_things))
                        print("avg of distances of things :"+ str(cur.avg_of_distances_of_things))


# PREF
            elif bash == "pref":
                print("Do you want to add new attribute for preference function? (y/n)")
                bash = input("$:")

                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:

                        if bash == 'y':
                            alpha = randrange(0, 10) / 10
                            beta = randrange(0, 10) / 10
                            landa = randrange(0, 10) / 10
                            teta = randrange(1, 5) / 10

                            cur.alpha = alpha
                            cur.beta = beta
                            cur.landa = landa
                        if bash != 'y' and bash != 'n':
                            print("Wrong command !")
                            continue
                        print("---------------Application \"" + str(
                            cur.ID) + "\" has following things -------------------")

                        print("Alpha = "+ str(cur.alpha))
                        print("Beta = " + str(cur.beta))
                        print("Landa = " + str(cur.landa))
                        print("teta = " + str(teta))

                        p= cur.alpha*int(cur.avg_of_values_of_things*100) + cur.beta* len(cur.things_thread_pool)*2 + cur.landa*(int(cur.avg_of_distances_of_things))*2+ teta *cur.pnum
                        cur.pref = p


                        print("Preference of this app is :"+ str(p) )


# SUB
            elif bash == "sub":
                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    n=0
                    for cur in apps:
                        print("---------------Application \"" + str(
                            cur.ID) + "\" has following available things -------------------")

                        for cur16 in things:
                            is_in_range = check_distance(cur16.x,cur16.y,cur.x,cur.y)
                            if (is_in_range < cur.a_range):
                                if cur16 not in cur.things_thread_pool:
                                    for cur8 in sorted(sponsors):
                                        if cur16 in cur8.things_thread_pool :
                                            print("thing "+ str(cur16.ID)+"  from sponsor "+ str(cur8.type))
                                            n+=1
                        print("number of available things :" + str(n))
                        n=0

# SUBSETS
            elif bash == "subsets":
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
                                    cur.avg_of_values_of_things *= len(cur.things_thread_pool)
                                    cur.avg_of_values_of_things += sum(cur16.value)
                                    cur.avg_of_values_of_things /= (len(cur.things_thread_pool)+1)

                                    cur.avg_of_distances_of_things *=len(cur.things_thread_pool)
                                    cur.avg_of_distances_of_things += is_in_range
                                    cur.avg_of_distances_of_things /= (len(cur.things_thread_pool)+1)

                                    p = cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * (len(cur.things_thread_pool)+1) * 2 + cur.landa * (50 - int(cur.avg_of_distances_of_things)) * 2
                                    q = p - cur.pref
                                    cost = int(q*2)
                                    print("Adding thing \"" + str(cur16.ID)+"\" to this application ")
                                    print("The new preference of this app is :" + str(p))
                                    print("Difference with previous preference is :" + str(q))
                                    print("Estimated cost is : "+str(cost)+"$")
                                    print('')
                                    print('')
                                    cur.avg_of_values_of_things=v1
                                    cur.avg_of_distances_of_things=v2
                                    n += 1
                        n = 0
                print("Do you want to add a thing in any application? (y/n)")
                bash2 = input("$:")
                if bash2 == "y":
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
                                for cur in apps:
                                    if cur.ID == int(bash2):
                                        print("Done")


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

                if bash2 != 'y' and bash2 != 'n':
                    print("Wrong command !")
                    continue


                elif bash2 == "n":
                    continue

# POSITIONS
            elif bash == "positions":
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


# GRAPHICAL SHOW
            elif bash == "g":
                for cur50 in sorted(sponsors):
                    G.add_node(cur50.ID)
                    pos = {cur50.ID: (cur50.center_x, cur50.center_y)}
                    nx.draw_networkx_nodes(G, pos, node_size=cur50.s_range * 800, nodelist=[cur50.ID], node_color='r',
                                           alpha=0.1)
                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        G.add_node(cur.ID)
                        pos = {cur.ID: (cur.x, cur.y)}
                        nx.draw_networkx_nodes(G, pos, nodelist=[cur.ID], node_color='b', alpha=0.8)

                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        tng = sorted(cur.things_thread_pool)
                        for cur2 in tng:
                            G.add_node(cur2.ID)
                            pos = {cur2.ID: (cur2.x, cur2.y)}
                            nx.draw_networkx_nodes(G, pos, nodelist=[cur2.ID], node_size=50, node_color='g', alpha=0.8)
                            #G.add_edge(sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID,t.ID)
                            #pos = {sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].ID: (sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].x,sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[number_tmp2].y),t.ID: (t.x, t.y)}
                            #G.draw_networkx_edges(G, pos)


                G.add_node(1)
                G.add_node(2)
                G.add_node(3)
                G.add_node(4)
                pos1 = {1: (0, 0), 2: (0, 500), 3: (500, 500), 4: (500, 0)}
                nx.draw_networkx_nodes(G, pos=pos1, node_size=1, nodelist=[1, 2, 3, 4], node_color='b',alpha=0.1)
                plt.show()
# RANDOM
            elif bash == "random":
                rand1 = randrange(1,4)
                rand2 = randrange(1,5)
                rand3 = randrange(0,15)

                number_tmp3 = rand1

                for cur4 in range(0, number_tmp3):
                    t = Sponsor(randrange(30, 470), randrange(30, 470), randrange(50, 100))
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
                    number_tmp4 = randrange(1, 5)
                    x2 = randrange(0, 500)
                    y2 = randrange(0, 500)
                    r2 = randrange(150, 200)

                    for cur4 in range(0, number_tmp4):
                        x1 = cur13.center_x
                        y1 = cur13.center_y
                        r1 = cur13.s_range
                        while True:
                            d2 = check_distance(x2, y2, x1, y1)
                            if (d2 < r1):
                                break
                            else:
                                x2 = randrange(0, 500)
                                y2 = randrange(0, 500)

                        t = Application(x2, y2, r2)
                        cur13.application_thread_pool.append(t)

                        x2 = randrange(0, 500)
                        y2 = randrange(0, 500)
                        r2 = randrange(150, 200)


                for cur11 in sorted(sponsors):
                    apps = sorted(cur11.application_thread_pool)
                    if len(cur11.application_thread_pool) == 0:
                        continue
                    for cur in apps:
                        number_tmp5 = randrange(0, 15)
                        pluged_num = randrange(0,100)

                        pluged_num = int((pluged_num * number_tmp5) / 100)
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

                        for cur20 in range(0, pluged_num):
                            cur.things_thread_pool[cur20].EnType = 'pluged'




                print("Done")
                print('')
                for cur11 in sorted(sponsors):
                    print("Sponsor  "+str(cur11.type)+": ")
                    print("Number of apps :"+ str(len(cur11.application_thread_pool)))
                    print("Number of things :" + str(len(cur11.things_thread_pool)))
                    print('')
                    print('')






                                #HELP
            elif bash == "help":
                print (" \"create\" : to create Sponsor/Application/Thing ")
                print (" \"topo\" : to view designed system")
                print(" \"back\" : go back to the first step")
                print (" \"help\" : to show more information about using the system" )
                print(" \"evaluate\" : to evaluate things in each sponsor")
                print(" \"show details\" : to show details of evaluation")
                print(" \"pref\" : preferece funtion of each thing")
                print(" \"sub\" : show available things in each application range briefly")
                print(" \"subsets\" : add available things in choosen application and calculate cost")
                print(" \"positions\" : show position of each created Sponsor , Application , Things")
                print(" \"g\" : graphical show of scenario")
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
    Terminal(sponsors)


