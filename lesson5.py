def GetIndexList(listInput):
    listResult=[]
    for i in range(len(listInput)):
        if i%2==0:
            listResult.append(listInput[i])
    return listResult
def GetIndexList1(listInput):
    listResult=[]
    for i in range(len(listInput)):
        if i%2==1:
            listResult.append(listInput[i])
    return listResult 
def MakeForPoint(listFirst, listNext):
    listFirst1=[]
    listNext0=[]
    listResult=[]
    for k in range(len(listFirst)):
        newListSub1=[]
        for k1 in range(len(listFirst[k])):
            if k1%2==1:
                newListSub1.append(listFirst[k][k1])
        listFirst1.append(newListSub1)
    for j in range(len(listNext)):
        newListSub2=[]
        for j1 in range(len(listNext[j])):
            if j1%2==0:
                newListSub2.append(listNext[j][j1])
        listNext0.append(newListSub2)
    for m in range(len(listFirst1)-1):
        listNear1= listNext0[m]
        for n in range(len(listFirst1[m])-1):
            listPoint=[listFirst1[m][n],listNear1[n],listFirst1[m+1][n],listNear1[n+1]] 
            listResult.append(listPoint)
    return listResult
    
def MakeForPoint2(listFirst, listNext):
    listFirst1=[]
    listNext0=[]
    listResult=[]
    for k in range(len(listFirst)):
        newListSub1=[]
        for k1 in range(len(listFirst[k])):
            if k1%2==1:
                newListSub1.append(listFirst[k][k1])
        listFirst1.append(newListSub1)
    for j in range(len(listNext)):
        newListSub2=[]
        for j1 in range(len(listNext[j])):
            if j1%2==0:
                newListSub2.append(listNext[j][j1])
        listNext0.append(newListSub2)
    for m in range(len(listNext0)-1):
        listNear1= listFirst1[m+1]
        for n in range(1,len(listNext0[m]),1):
            listPoint=[listNext0[m][n],listNear1[n-1],listNext0[m+1][n],listNear1[n]] 
            listResult.append(listPoint)
    return listResult

def Make3Point(listFirst,listNext):
    listResult= []
    for i in range(1,len(listFirst[0])-1,2):
        point3=[listFirst[0][i],listFirst[0][i+2],listNext[1][i+1]]
        listResult.append(point3)
    listResult.append([listFirst[0][0],listFirst[0][1],listNext[1][0]])
    return listResult

def Make3Point2(listFirst,listNext):
    listResult= []
    n= len(listFirst[0])
    for i in range(0,len(listFirst[0])-2,2):
        point3=[listFirst[0][i],listFirst[0][i+2],listNext[0][i+1]]
        listResult.append(point3)
    listResult.append([listFirst[0][n-2],listFirst[0][n-1],listNext[0][n-1]])
    return listResult

def Make3Point3(listFirst,listNext):
    listResult= []
    for i in range(1,len(listFirst[0])-2,2):
        point3=[listFirst[0][i],listFirst[0][i+2],listNext[0][i+1]]
        listResult.append(point3)
    return listResult

def Make3Point4(listFirst,listNext):
    listResult= []
    for i in range(0,len(listFirst[0])-2,2):
        point3=[listFirst[0][i],listFirst[0][i+2],listNext[0][i+1]]
        listResult.append(point3)
    return listResult



        
    
        
