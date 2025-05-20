import math

goal = input("Adja meg mire gyűjt?")
dogs = int(input("Mennyi kutyát sétáltat?"))
print(f"Anna {math.floor(dogs*20/60)} óra {dogs*20-(60*math.floor(dogs*20/60))} percet")
print(f"Anna {dogs*700}ft-ot fog keresni")
if dogs*700 > 5000:
    print(f"Anna {dogs*700}ft-ot fog keresni, ez elég.")
else:
    print(f"Anna {dogs*700}ft-ot fog keresni, ez nem elég")