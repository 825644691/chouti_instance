import queue
#队列 FIFO先进先出
#队列自己有一把shuo

d = queue.Queue(2)

d.put("hjw")
d.put("goupang")
d.put("goulin")

print(d.get())

print(d.get())
print(d.get())