
# with open('E:/aaa.txt','w',encoding='utf-8') as file:
#     i=1
#     while i<10:
#         file.write(str(i))
#         file.write('\n')
#         i+=1

with open('E:/aaa.txt','r',encoding='utf-8') as file1:
    for i,v in enumerate(file1.readlines(),1):
        if i == 6:
            v=''.join([v.strip(),'jjjj'])
        print(v.strip())






