print("This program will create Dataframe using 2D Dictionary of List /n/n/ ")
dic={'Student':['Aditya', 'Naman', 'Junaid', 'Nishant'],
     'Marks':[90.5, 80, 70.5,60],
     'Sports':['Cricket', 'Badminton', 'Football', 'Kabaddi']}
print("Your 2D Dictionary Look Like:- \n\n",dic,"\n\n")
import pandas as pd
df=pd.DataFrame(dic)
print("Your Dataframe Look Like:- \n\n",df)
