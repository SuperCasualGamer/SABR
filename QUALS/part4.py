import pandas as pd
#Team is Toronto Blue Jays (TOR)

blue_data = pd.read_csv('TOR.csv')
blue_data.dropna(inplace=True)
blue_data.sort_values(by='WAR/pos', inplace=True, ascending=False)

for year in range(2007, 2017):
    year_data = blue_data[blue_data['Year'] == year]
    # print(year_data[['Player', 'WAR/pos', 'Year']].head(1))
#                Player  WAR/pos  Year
# 3  Alex Rios\riosal01      5.6  2007
#                 Player  WAR/pos  Year
# 45  Alex Rios\riosal01      5.9  2008
#                  Player  WAR/pos  Year
# 77  Aaron Hill\hillaa01      5.8  2009
#                       Player  WAR/pos  Year
# 136  Jose Bautista\bautijo02      6.9  2010
#                       Player  WAR/pos  Year
# 178  Jose Bautista\bautijo02      8.1  2011
#                           Player  WAR/pos  Year
# 209  Edwin Encarnacion\encared01      5.0  2012
#                      Player  WAR/pos  Year
# 243  Colby Rasmus\rasmuco01      4.8  2013
#                       Player  WAR/pos  Year
# 302  Jose Bautista\bautijo02      6.1  2014
#                        Player  WAR/pos  Year
# 340  Josh Donaldson\donaljo02      8.8  2015
#                        Player  WAR/pos  Year
# 381  Josh Donaldson\donaljo02      7.4  2016

blue_data.sort_values(by='AB', inplace=True, ascending=False)
print(blue_data[['Player', 'AB', 'Year']].head(10))
#                           Player   AB  Year
# 77           Aaron Hill\hillaa01  682  2009
# 3             Alex Rios\riosal01  643  2007
# 45            Alex Rios\riosal01  635  2008
# 115       Vernon Wells\wellsve01  630  2009
# 340     Josh Donaldson\donaljo02  620  2015
# 303         Jose Reyes\reyesjo01  610  2014
# 1            Aaron Hill\hillaa01  608  2007
# 374  Edwin Encarnacion\encared01  601  2016
# 154       Vernon Wells\wellsve01  590  2010
# 78            Adam Lind\lindad01  587  2009