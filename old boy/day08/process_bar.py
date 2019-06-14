import sys,time
for i in range(30):
    p = i/30
    # sys.stdout.write("*")
    # sys.stdout.flush()
    text = ''.join("*")
    # print("*   %s"%p)
    sys.stdout.write("*   %s"%p)
    sys.stdout.flush()
    time.sleep(0.1)