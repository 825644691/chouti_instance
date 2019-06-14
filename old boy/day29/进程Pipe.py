from multiprocessing import Process,Pipe


def f(conn):
    conn.send([42,None,'hello'])
    print(conn.recv())
    conn.close()



if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    print(parent_conn,child_conn)
    p = Process(target=f,args=(parent_conn,))
    p.start()
    print(child_conn.recv())
    child_conn.send("约")
    p.join()