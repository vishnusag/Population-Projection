import mysql.connector as my
import chart_studio.plotly as py
import matplotlib.pyplot as go
import numpy as np

import pandas as pd

db=my.connect(host='localhost',user='root',password='1234',database='population_projection')

#print(db.connection_id)


key=db.cursor()
#key.execute("insert into population_growth(years)values(2028)")

#key.execute("update population_growth set population_in_millions = (1.16 * 0.1 * 1298 + 1298) where years = 2028")
#key.execute("update population_growth set percentage_of_growth = (1.16 * 10) where years = 2028")
#key.execute("update population_growth set percentage_of_death = (0.05 * 10) where years = 2028")
#key.execute("update population_growth set percentage_of_birth = (1.21 * 10) where years = 2028")
#db.commit()
key.execute('select years, population_in_millions from population_growth')
rows = key.fetchall()
str(rows)[0:20]

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'years', 1: 'population_in_millions'}, inplace=True);
df = df.sort_values(['population_in_millions'], ascending=[1])

'''go.plot(df['years'],df['population_in_millions'])
go.xlabel('Years')
go.ylabel('population in millions')
go.title('Population projection for 10 years')
go.show()'''
'''y_pos = np.arange(len(df['years']))
go.bar(y_pos, df['population_in_millions'], align='center', alpha=1.0)
go.xticks(y_pos,df['years'])
go.ylabel('Population growth')
go.title('Population projection for 10 years')
go.show()'''

sizes=df['population_in_millions']
labels=df['years']
go.pie(sizes, labels = labels, 
        startangle=90, shadow = True, explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1), 
        radius = 1.1, autopct = '%1.1f%%')
# title of plot
go.title('Population projection for 10 years')
  
# plotting legend 
go.legend()
  
# showing the plot 
go.show() 




