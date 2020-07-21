import os, glob
import pandas as pd

#path = "/Users/jolly/Desktop/Bollywood/"

#koimoi_f = glob.glob(os.path.join(path,"Box-office*.xlsx"))
#print(koimoi_f)
#wiki_cast_f = glob.glob(os.path.join(path, "Movies list_Wiki_2012-19.xlsx"))
#koimoi = pd.read_excel("Box-office Koimoi.xlsx", index_col=1)
koimoi = pd.read_excel('Box-office Koimoi.xlsx')
koimoi['Film'] = koimoi['Film'].str.strip()
koimoi['Film'] = koimoi['Film'].str.casefold()
Movies_list_Wiki = pd.read_excel('Movies list_Wiki_2012-19.xlsx')
Movies_list_Wiki['Movie'] = Movies_list_Wiki['Movie'].str.strip()
Movies_list_Wiki['Movie'] = Movies_list_Wiki['Movie'].str.casefold()

#print(koimoi.head())
#print(Movies_list_Wiki.head())

all_data = pd.merge(koimoi, Movies_list_Wiki, how='left', left_on='Film', right_on='Movie')
print(all_data.head())
all_data.to_excel( "Join.xlsx")


