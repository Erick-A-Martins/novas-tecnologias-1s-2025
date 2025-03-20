nome = input("Digite seu nome: ")

turno = input(
"""
    M - Matutino
    V - Vespertino
    N - Noturno
"""
)

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))

media = (nota1+nota2+nota3)/3

match turno:
    case "M":
        turno_msg = "Estuda no Matutino"
    case "N":
        turno_msg = "Estuda no Noturno"
    case "V":
        turno_msg = "Estuda no Vespertino"
    case _:
        turno_msg = "Turno de aula inválido"

if media < 3:
    mencao = "Reprovado"
elif media >= 7 and media < 9:
    mencao = "Aprovado"
else:
    mencao = "Aprovado com excelência!"


print(
f"""
            ***************************************
            **        Boletim do Estudante       **
            ** {nome}                            **
            **                                   **
            ** Nota 1 | Nota 2 | Nota 3          **
            ** {nota1}   |{nota2}   |{nota3}     **
            **                                   **
            ** Turno: {turno_msg}                **
            **                                   **
            ** Media: {media}                    **
            ** {mencao}                          **
            ***************************************

"""
)