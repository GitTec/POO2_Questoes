from Q03 import Filme

filmesArray = []

for i in range(3):
    print("-"*23)
    print(f"INFORMAÇÕES DO {i+1}° FILME ")
    print("-" * 23)
    tit = input("Informe o título do filme: ")
    dur = input("Informe a duração do filme: ")
    cat = input("Informe a categoria do filme: ")
    filme = Filme(titulo=tit, duracao=dur, categoria=cat)
    filmesArray.append(filme)

print("-"*30)
for i in range(3):
    filmesArray[i].verdetalhes()
