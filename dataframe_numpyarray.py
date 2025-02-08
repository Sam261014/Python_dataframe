print("This program will create Dataframe using 2D Dictionar of Numpy Array \n\n")
import numpy as np
dic={'Student':np.array(['Aditya', 'Naman', 'Junaid', 'Nishant']),\
     'Marks':np.array([90.5, 80, 70.5,60]),\
     'Sports':np.array(['Cricket', 'Badminton', 'Football', 'Kabaddi'])}
print("Your 2D Numpy Array Look Like:- \n\n",dic,"\n\n")
import pandas as pd
df=pd.DataFrame(dic)
print("Your DataFrame Look Like:- \n\n", df)
df['Marks']=df['Marks']-10
print("\nAfter deduct 10 marks DataFrame Look Like :- \n\n",df)
df.loc[0,'Marks']=df.loc[0,'Marks']-10
print("\nAfter deduct 10 marks DataFrame Look Like :- \n\n",df)
