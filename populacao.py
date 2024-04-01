populacaoA = 80000
populacaoB = 200000

taxaAnualA = 1.03
taxaAnualB = 1.015

ano = 0
novaPopulacaoA = 0
novaPopulacaoB = 0

while populacaoA < populacaoB:
    populacaoA = (populacaoA * taxaAnualA)
    populacaoB = (populacaoB * taxaAnualB)

    print(f"Pais A: {populacaoA}")
    print(f"Pais B: {populacaoB}")
    print(f"Anos: {ano }")
    ano+=1