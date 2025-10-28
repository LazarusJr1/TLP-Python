nrinicio = int(input(f"Numero 1 "))
nrfim = int(input(f"Numero 2 "))

for i in range(nrinicio - 1, nrfim):
    if i % 3 == 0:
        print(i)
