import sys

n,m = map(int, input().split()) #n:포켓몬(도감)개수, m:맞춰야하는수

pocketmon_by_id = {}
pocketmon_by_name = {}
res = ""
for id in range(1,n+1):
    name = input()
    pocketmon_by_id[id]=name
    pocketmon_by_name[name]=id

for _ in range(m):
    pocketmon = sys.stdin.readline().strip()
    if pocketmon.isdigit():
        res += pocketmon_by_id[int(pocketmon)] + '\n'
    else:
        res += str(pocketmon_by_name[pocketmon]) + '\n'
                
print(res)
# 26 5
# Bulbasaur
# Ivysaur
# Venusaur
# Charmander
# Charmeleon
# Charizard
# Squirtle
# Wartortle
# Blastoise
# Caterpie
# Metapod
# Butterfree
# Weedle
# Kakuna
# Beedrill
# Pidgey
# Pidgeotto
# Pidgeot
# Rattata
# Raticate
# Spearow
# Fearow
# Ekans
# Arbok
# Pikachu
# Raichu
# 25
# Raichu
# 3
# Pidgey
# Kakuna