from random import *
def evaluation(sponsors , things):
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

            for cur5 in sorted(cur.things_thread_pool):
                if cur5.EnType == 'unplugged':

                    cur5.teta=random()
                    cur5.avg_of_values+=cur5.avg_of_values * cur5.teta



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