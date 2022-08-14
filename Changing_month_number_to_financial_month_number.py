month_no = [1,2,3,4,5,6,7,8,9,10,11,12]
fmn=[]
for i in month_no:
    if i<=3:
        i=i+9
        fmn.append(i)
    else:
        i = i-3
        fmn.append(i)
    
print(fmn)
