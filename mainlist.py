###############################################################################
# Beijing Jiaotong University School of Computer and Infomation Technology
# Sun Rui  16281079
# Subject: Operating System

# About the parameter:
# N : Virtual memory size   p : Starting point    e : Page of the working set
# m : Mobility   t : Reference parameter
###############################################################################
import random

'''
函数名称：Random_Sequence_String
功能：生成符合局部访问特性的随机序列
参数：
    start       序列的开始 p
    page_num    序列包含页数 p + e
    length      生成序列长度
    mobility    工作集移动率
    N           虚拟内存的尺寸
返回值：
    Sequence_String 随机生成的序列

'''


def Random_Sequence_String(start, page_num, length, mobility, N):  # To create a sequence string with random numbers
    start1, page_num1 = (int(start), int(page_num)) if start <= int(page_num) else (int(page_num), int(start))
    length = int(abs(int(length))) if length else 0
    Sequence_String = []
    temp = 0
    print(start)
    print(page_num)
    for i in range(length):
        if temp == mobility:
            start1 = start1 + 1
            page_num1 = page_num1 + 1
            temp = 0
        temp = temp + 1
        if page_num1 == N:
            page_num1 = page_num
            start1 = start
        Sequence_String.append(random.randint(start, page_num))
    return Sequence_String


'''
函数名称：Optimal_page_replacement_algorithm
功能：最佳置换算法
参数：
    Sequence_String 随机序列
    Memory_Length   内存大小
返回值：
    Missing_Page    缺页量
'''


def Optimal_page_replacement_algorithm(Sequence_String, Memory_Length):
    temp = 0
    temp1 = 0
    Missing_Page = 0
    mem = []
    Memory = []
    flag = 99
    for i in Sequence_String:
        if len(Memory) < Memory_Length:
            Memory.append(i)
            temp = temp + 1
        else:
            for i in Sequence_String[temp:]:
                if Memory.count(Sequence_String[temp]) != 0:
                    temp = temp + 1
                    continue
                else:
                    for j in Memory:
                        if Sequence_String[temp:].count(j) == 0:
                            flag = Memory.index(j)
                            break
                    if flag != 99:
                        Memory[flag] = Sequence_String[temp]
                        Missing_Page = Missing_Page + 1
                        flag = 99
                        break
                    while temp1 < Memory_Length:
                        mem.append(Sequence_String[temp:].index(Memory[temp1]))
                        temp1 = temp1 + 1
                    temp1 = 0
                    Memory[mem.index(max(mem))] = Sequence_String[temp]
                    Missing_Page = Missing_Page + 1
                    mem = []
    return Missing_Page



'''
函数名称：First_In_First_Out_algorithm
功能：先进先出置换算法
参数：
    Sequence_String 随机序列
    Memory_Length   内存大小
返回值：
    Missing_Page    缺页量
'''


def First_In_First_Out_algorithm(Sequence_String, Memory_Length):
    temp = 0
    temp1 = 0
    Missing_Page = 0
    Memory_Count = []
    Memory = []
    Memory_Count = Memory_Length * [0]
    for i in Sequence_String:
        if len(Memory) < Memory_Length:
            Memory.append(i)
            while temp < Memory_Length:
                while temp1 < temp:
                    Memory_Count[temp1] = Memory_Count[temp1] + 1
                    temp1 = temp1 + 1
                temp1 = 0
                temp = temp + 1
        else:
            if Memory.count(i) != 0:
                continue
            else:
                Memory[Memory_Count.index(max(Memory_Count))] = i
                Missing_Page = Missing_Page + 1
                Memory_Count = [j + 1 for j in Memory_Count]
                Memory_Count[Memory_Count.index(max(Memory_Count))] = 0
    return Missing_Page


'''
函数名称：Least_Recently_Used_algorithm
功能：最近最久未使用置换算法
参数：
    Sequence_String 随机序列
    Memory_Length   内存大小
返回值：
    Missing_Page    缺页量
'''


def Least_Recently_Used_algorithm(Sequence_String, Memory_Length):
    temp = 0
    Missing_Page = 0
    Memory = []
    Stack = []
    for i in Sequence_String:
        if len(Memory) < Memory_Length:
            Memory.append(i)
            Stack.insert(0, i)
        else:
            if Memory.count(i) != 0:
                Stack.remove(i)
                Stack.insert(0, i)
                continue
            else:
                temp = Stack.pop()
                Memory[Memory.index(temp)] = i
                Stack.insert(0, i)
                Missing_Page = Missing_Page + 1
    return Missing_Page



'''
函数名称：Enhanced_Not_Recently_Used_algorithm
功能：改进型Clock置换算法
参数：
    Sequence_String 随机序列
    Memory_Length   内存大小
返回值：
    Missing_Page    缺页量
'''


def Enhanced_Not_Recently_Used_algorithm(Sequence_String, Memory_Length):
    Memory = []
    Visited = []
    Modified = []
    Visited = Memory_Length * [0]
    Modified = Memory_Length * [0]
    Missing_Page = 0
    i = 0
    temp = 0
    flag = 0
    for i in Sequence_String:
        while 1:
            if Memory.count(i) == 0:
                if Visited[temp] == 0 and Modified[temp] == 0:
                    if flag == 0:
                        Memory.append(i)
                        if len(Memory) == Memory_Length:
                            flag = 1
                        if temp == Memory_Length - 1:
                            flag = 1
                            temp = 0
                            break
                        else:
                            temp = temp + 1
                            break
                    else:
                        Missing_Page = Missing_Page + 1
                        Memory[temp] = i
                        Visited[temp] = 1
                        Modified[temp] = random.randint(0, 1)
                        if temp != Memory_Length - 1:
                            temp = temp + 1
                            break
                        else:
                            temp = 0
                            break
                elif Visited[temp] == 0 and Modified[temp] == 1:
                    Missing_Page = Missing_Page + 1
                    Memory[temp] = i
                    Visited[temp] = 1
                    Modified[temp] = random.randint(0, 1)
                    if temp != Memory_Length - 1:
                        temp = temp + 1
                        break
                    else:
                        temp = 0
                        break
                else:
                    Visited[temp] = 0
                    if temp != Memory_Length - 1:
                        temp = temp + 1
                    else:
                        temp = 0
            else:
                temp = Memory.index(i)
                Visited[temp] = 1
                Modified[temp] = random.randint(0, 1)
                if temp != Memory_Length - 1:
                    temp = Memory.index(i) + 1
                    break
                else:
                    temp = 0
                    break

    return Missing_Page


#################Step 1 : Parameter input############################
# N = input("Please enter the virtual memory size(N):")
# p = input("Please enter the starting point(p):")
# e = input("Please enter the page of the working set(e):")
# m = input("Please enter the mobility of the working set(m):")
# t = input("Please enter the parameter(t):")
#####################################################################

#################Step 2 : Create the sequence string#################

Seq_Len = 200
Mem_Len = 8
N = 20
p = 0
e = 10
m = 20
t = 0.2
Sequence_String = Random_Sequence_String(p, (p + e), Seq_Len, m, N)

#####################################################################

#################Step 3&4 : Create a random number r and create new number for p#####################
'''
r = random.random()
if r > t:
    p = (p + 1) % N
else:
    p = random.randrange(0,N,1)
#####################################################################################################
'''
# Sequence_String = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
# Sequence_String = [3,4,2,6,4,3,7,4,3,6,3,4,8,4,6]
# Sequence_String = [1,2,3,1,4,7,4,2,5,5,6,6]

# Sequence_String = [12, 14, 11, 11, 13, 8, 5, 12, 8, 11, 10, 10, 13, 9, 15, 17, 5, 7, 4, 6]
# print (Sequence_String)
print(len(Sequence_String))
print("The OPR page missing rate is : " + str(
    (Optimal_page_replacement_algorithm(Sequence_String, Mem_Len)) / Seq_Len * 100) + "%")
print("The FIFO page missing rate is : " + str(
    (First_In_First_Out_algorithm(Sequence_String, Mem_Len)) / Seq_Len * 100) + "%")
print("The LRU page missing rate is : " + str(
    (Least_Recently_Used_algorithm(Sequence_String, Mem_Len)) / Seq_Len * 100) + "%")
print("The ENRU page missing rate is : " + str(
    (Enhanced_Not_Recently_Used_algorithm(Sequence_String, Mem_Len)) / Seq_Len * 100) + "%")




