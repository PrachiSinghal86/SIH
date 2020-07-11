import pandas as pd
import re

missing_val=['None']

df=pd.read_csv("C:/Users/hp1/Documents/sih/datascientist2.csv", na_values=missing_val)
df.drop(columns=['Sponsored'],inplace=True)

#sal=list(df['Salary'])
#x=re.search("^â‚",sal)

#def remove_tags(data):
 #   yr = re.compile('a year$') 
  #  cleantext = re.sub(rup, '', data)
   # return cleantext
#df['Salary'] = df['Salary'].apply(lambda x: remove_tags(x) if x!='None' else x)
#null=df[df['Salary']=='None']
 
#s=df.iloc[34][3]
#print(s)
#stnew=st.replace('â','')
#print(type(st[0]))

#st=re.sub(r'a year$',"",st) #replace a year with null string
#st= re.sub(r'a month$',"",st)


#l=st.split('-')
#print(l)
#for i in range(0,len(l)):
 #   l[i]=re.sub("\D", "",l[i]) #\D is used to remove everything except digits
#print(l)
#s="-".join(l)
#print(s)

#print(sum(df['Salary'].isnull()))
#def solve (s):
    
def solve(s):
    x=re.findall("a month$",s)
    if x: 
        s=re.sub(r'a month$',"",s)
        s=re.sub(r',',"",s)
        if('-' in s):
            l=s.split("-")
            for i in range(0,len(l)):
                l[i]=re.sub("\D", "",l[i])
            l[0]=int(l[0])*12;
            l[1]=int(l[1])*12;
            l[0]=str(l[0])
            l[1]=str(l[1])
            s="-".join(l)
        else:
            s=re.sub("\D", "",s)
            s=int(s)*12
            s=str(s)
            
    x=re.findall("an hour$",s)
    if x: 
        s=re.sub(r'an hour$',"",s)
        s=re.sub(r',',"",s)
        l=s.split("-")
        for i in range(0,len(l)):
            l[i]=re.sub("\D", "",l[i])
        l[0]=int(l[0])*2880;
        l[1]=int(l[1])*2880;
        l[0]=str(l[0])
        l[1]=str(l[1])
        s="-".join(l)
    
    x=re.findall("a year$",s)
    if x: 
        s=re.sub(r'a year$',"",s)
        s=re.sub(r',',"",s)
        l=s.split("-")
        for i in range(0,len(l)):
            l[i]=re.sub("\D", "",l[i])
        s="-".join(l)

    return s



#print(df.info())
df.dropna(inplace=True)
df['Salary']=df['Salary'].apply(solve)
#print(df.info())
#for i in df['Salary']:
 #   i=solve(i)

df.to_csv("C:/Users/hp1/Documents/sih/datascientistnew.csv")
    
