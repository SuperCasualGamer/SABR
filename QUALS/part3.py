import pandas as pd

AL_league = pd.read_csv('AL.csv')
NL_league = pd.read_csv('NL.csv')

AL_league.dropna(inplace=True)
NL_league.dropna(inplace=True)
AL_league.sort_values(by='WAR/pos', inplace=True, ascending=False)
NL_league.sort_values(by='WAR/pos', inplace=True, ascending=False)

print(AL_league[['Player', 'Age']].head(10))
print(NL_league[['Player', 'Age']].head(10))
#                         Player  Age
# 3243      Mike Trout\troutmi01   20
# 5753      Mike Trout\troutmi01   24
# 5758    Mookie Betts\bettsmo01   23
# 5123      Mike Trout\troutmi01   23
# 22    Alex Rodriguez\rodrial01   31
# 3862      Mike Trout\troutmi01   21
# 5014  Josh Donaldson\donaljo02   29
# 2302     Ben Zobrist\zobribe01   30
# 2014   Josh Hamilton\hamiljo03   29
# 1174     Ben Zobrist\zobribe01   28
#                           Player  Age
# 5306      Bryce Harper\harpebr03   22
# 1344     Albert Pujols\pujolal01   29
# 680      Albert Pujols\pujolal01   28
# 784        Chase Utley\utleych01   29
# 5706  Paul Goldschmidt\goldspa01   27
# 16       Albert Pujols\pujolal01   27
# 4040      Carlos Gomez\gomezca01   27
# 187       David Wright\wrighda03   24
# 1451       Chase Utley\utleych01   30
# 3092          Matt Kemp\kempma01   26

AL_old = AL_league[AL_league['Age'] >= 30]
NL_old = NL_league[NL_league['Age'] >= 30]
AL_old.sort_values(by='WAR/pos', inplace=True, ascending=False)
NL_old.sort_values(by='WAR/pos', inplace=True, ascending=False)

print(AL_old[['Player', 'Age']].head(10))
print(NL_old[['Player', 'Age']].head(10))
#                          Player   Age
# 22     Alex Rodriguez\rodrial01   31
# 2302      Ben Zobrist\zobribe01   30
# 2579    Jose Bautista\bautijo02   30
# 3918     Robinson Cano\canoro01   30
# 1700    Adrian Beltre\beltrad01   31
# 1238    Chone Figgins\figgich01   31
# 5635   Josh Donaldson\donaljo02   30
# 3850   Miguel Cabrera\cabremi01   30
# 389   Magglio Ordonez\ordonma01   33
# 5809     Robinson Cano\canoro01   33
#                         Player  Age
# 1451     Chase Utley\utleych01   30
# 124    Chipper Jones\jonesch06   35
# 5544      Joey Votto\vottojo01   31
# 1995   Albert Pujols\pujolal01   30
# 787    Chipper Jones\jonesch06   36
# 758   Carlos Beltran\beltrca01   31
# 1062   Lance Berkman\berkmla01   32
# 2417   Matt Holliday\hollima01   30
# 4121    David Wright\wrighda03   30
# 2099     Chase Utley\utleych01   31

for year in range(2007, 2017):
    print(f"Year: {year}, Sum: {AL_league[AL_league['Year'] == year]['WAR/pos'].sum()}")
# Year: 2007, Sum: 307.99999999999994
# Year: 2008, Sum: 299.8
# Year: 2009, Sum: 294.5
# Year: 2010, Sum: 312.5
# Year: 2011, Sum: 308.8
# Year: 2012, Sum: 306.6
# Year: 2013, Sum: 310.4
# Year: 2014, Sum: 306.29999999999995
# Year: 2015, Sum: 308.99999999999994
# Year: 2016, Sum: 315.20000000000005