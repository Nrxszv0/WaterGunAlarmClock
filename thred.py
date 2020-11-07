import threading
import time

ls = []

def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)


def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target = count, args=(5,))
x.start()
x.join() 
y = threading.Thread(target = count2, args=(5,))
y.start()

# x.join() 
#dont move past line of code till thread done
y.join() 
#dont move past line of code till thread done

print(ls)










#need ot make funciotn for threading
# def func():
#     print('ran')
#     time.sleep(1)
#     print("Done")
#     time.sleep(.91)
#     print("now done")

# x = threading.Thread(target=func)#need n, to send tuple, needed argument form

# x.start()
# print(threading.activeCount())
# time.sleep(.851)
# print("finally")