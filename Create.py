def creation(sponsors , things , bash):
    bash = input("Which one do you wanna create ? \n1 ) Sponsors \n2 ) Application \n3 ) Things \n? ")

    # CREATE THINGS
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
                    bash = input("Percentage of Plugged Devices ? ")
                    plugged_num = int(bash)
                    if (plugged_num > 100 or plugged_num < 0):
                        print("you have to choose between 0 and 100")
                        continue
                    else:
                        plugged_num = int((plugged_num * number_tmp3) / 100)
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
                                if (d < r3):
                                    break

                            x2 = randrange(0, 500)
                            y2 = randrange(0, 500)
                        t = Thing(x2, y2)
                        sorted(sponsors)[number_tmp4].things_thread_pool.append(t)
                        sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                            number_tmp2].things_thread_pool.append(t)
                        things.append(t)
                        t.distance_from_app = check_distance(x2, y2, x1, y1)

                        x2 = randrange(0, 500)
                        y2 = randrange(0, 500)

                    for cur20 in range(0, plugged_num):
                        sorted(sorted(sponsors)[number_tmp4].application_thread_pool)[
                            number_tmp2].things_thread_pool[cur20].EnType = 'plugged'




                except:
                    # print("Error (5)")
                    # print(sys.exc_info())
                    continue




        except:
            print("Error (10)")
            print(sys.exc_info())
            continue

            # CREATE APPLICATION
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
                x2 = randrange(0, 500)
                y2 = randrange(0, 500)
                r2 = randrange(150, 200)

                for cur4 in range(0, number_tmp3):
                    x1 = sorted(sponsors)[number_tmp2].center_x
                    y1 = sorted(sponsors)[number_tmp2].center_y
                    r1 = sorted(sponsors)[number_tmp2].s_range
                    while True:
                        d2 = check_distance(x2, y2, x1, y1)
                        if (d2 < r1):
                            break
                        else:
                            x2 = randrange(0, 500)
                            y2 = randrange(0, 500)

                    t = Application(x2, y2, r2)
                    sorted(sponsors)[number_tmp2].application_thread_pool.append(t)

                    x2 = randrange(0, 500)
                    y2 = randrange(0, 500)
                    r2 = randrange(150, 200)
                print("Done!")
        except:
            # print("Error (8)")
            # print(sys.exc_info())
            continue

            # CREATE SPONSOR
    elif bash == "1":
        try:
            bash = input("How many sponsor(s) do you want to append ? ")
            if bash == "back":
                continue
            else:
                number_tmp3 = int(bash)

        except:
            print("Wrong command")

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

        print("Done!")

    elif bash == "back":
        continue




    else:
        print("Choose from the list please")
        continue
        # elif bash.lower() == "load file" :
        # 	bash = input("Enter file path : ")
        # 	file  = open(bash)

