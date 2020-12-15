import pandas as pd

d = {'name': ["aretha", "mariah","celine","alanis"], 'birth': [1945, 1979,1965,1985],'death':[2005,2019,2013,1985]}
df = pd.DataFrame(data=d)
df

years=list(range(min(df.birth),max(df.death)))
pop=[0]*len(years)
for x in range(0,len(years)): #O(Y*N)
    for y in range(0,len(df)):
        if df.loc[y].at['birth']<=years[x] and df.loc[y].at['death']>=years[x]:
            pop[x]=pop[x]+1 #

index=pop.index(max(pop))
print(years[index])