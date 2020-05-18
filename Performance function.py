try:
    print("Do you want to add new preferences for performance function? (y/n)")
    bash = input("$:")
    for cur11 in sorted(sponsors):
        apps = sorted(cur11.application_thread_pool)
        if len(cur11.application_thread_pool) == 0:
            continue
        for cur in apps:

            if bash == 'y':
                # alpha = randrange(0, 10) / 10
                alpha = 0.5
                # beta = randrange(5, 10) / 10
                # landa = randrange(5, 10) / 10
                beta = 0.5
                landa = 0.5
                # teta = randrange(1, 5) / 10

                cur.alpha = alpha
                cur.beta = beta
                cur.landa = landa
                # cur.teta = teta
            if bash != 'y' and bash != 'n':
                print("Wrong command !")
                continue
            print("---------------Application \"" + str(
                cur.ID) + "\" has following things -------------------")

            print("Alpha = " + str(cur.alpha))
            print("Beta = " + str(cur.beta))
            print("Landa = " + str(cur.landa))
            # print("teta = " + str(cur.teta))

            p = (cur.alpha * int(cur.avg_of_values_of_things * 100) + cur.beta * len(
                cur.things_thread_pool) + cur.landa * (100 - (int(cur.avg_of_distances_of_things) / 2))) / 3

            cur.pref = p

            print("Performance of this app is :" + str(p))
except:
    print("Error")
    continue