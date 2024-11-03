from hero import Assasin,Tank

saber = Assasin("Saber")
tigreal = Tank("Tigreal")

print(saber.info())
print(tigreal.info())

saber.exp_up = 10000
tigreal.exp_up = 10000

print(saber.info())
print(tigreal.info())