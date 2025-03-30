print('This program will create a Datafram using 2D Dictionary of Panda Series/')
import pandas as pd
popltn=pd.Series([1000, 1200, 4600, 4300],\
                     index=['Oslo', 'Tromso', 'Trondheim','Bergen'])
avginc=pd.Series([10000, 60000, 12500, 43000],\
                     index=['Oslo', 'Tromso', 'Trondheim','Bergen'])
percap=avginc/popltn
dic={'Population':popltn,'Average Income':avginc,'Per Capita':percap}
print("Your 2D Dictionary looks like :- \n\n",dic,"\n\n")
df=pd.DataFrame(dic)
print(" Your dataframe looks like :- \n\n",df)                        
                    
