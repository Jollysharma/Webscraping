import pandas as pd

Bolly_families = pd.read_excel('imdb bollywood families(edited).xlsx')
Bolly_families['names'] = Bolly_families['names'].str.casefold()
Bolly_families['names'] = Bolly_families['names'].str.replace('\n'," ")
Bolly_families['names'] = Bolly_families['names'].str.strip()

Bolly_master = pd.read_excel('Bollywood_masterdata.xlsx')
Bolly_master['Cast'] = Bolly_master['Cast'].str.casefold()
Bolly_master['Cast'] = Bolly_master['Cast'].str.strip()

movies = []
kith_kins = []
kith_kins_flag = []
actors_list = []

for row in Bolly_master.itertuples(index = False, name ='Pandas'):

    actor_list = []

    for actor in Bolly_families['names']:

            try:
                found = (row.Cast).find(actor)
            except AttributeError:
                pass
            else:
                if found != -1:
                    print(actor)
                    actor_list.append(actor)

    if len(actor_list) != 0:
       kith_kins.append(len(actor_list))
       actors_list.append(actor_list)
       kith_kins_flag.append("Insider")
       #movies.append(getattr(row, 'Movie_name'))
    else:
       kith_kins.append(0)
       actors_list.append("")
       kith_kins_flag.append("Outsider")
       #movies.append(getattr(row, 'Movie_name'))

#print(movies)
print(actors_list)
print(kith_kins)

#print(Bolly_master.info())

Bolly_master['kith_kins_count'] = kith_kins
Bolly_master['kith_kins_actors'] = actors_list
Bolly_master['Insider_outsider_flag'] = kith_kins_flag

print(Bolly_master.info())

Bolly_master.to_excel( "Bollywood_masterdata.xlsx")

