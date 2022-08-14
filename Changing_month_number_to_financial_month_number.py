import pandas as pd

def financial_month_convertor(i):
    fmn=0
    if i<=3:
       i=i+9
       fmn=i
    else:
        i = i-3
        fmn=i
    return fmn
   
month_no = [1,2,3,4,5,6,7,8,9,10,11,12]
month_no=pd.DataFrame(month_no,columns=['original'])
#print(month_no)

month_no['financil_month'] = month_no['original'].apply(financial_month_convertor)
print(month_no)
