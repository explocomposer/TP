année = int(input("Saisissez une année: "))
if 4 % année == 0:
    bissextile = True
elif 100 % année == 0:
    bissextile == True
elif 400 % année == 0:
    bissextile = True
    print("L'année est bissextile")
else:
    bissextile = True
    print("L'année est bissextile")




# Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
# Si elle est multiple de 4, on regarde si elle est multiple de 100.
#   Si c'est le cas, on regarde si elle est multiple de 400.
#       Si c'est le cas, l'année est bissextile.
#       Sinon, elle n'est pas bissextile.
# Sinon, elle est bissextile.
