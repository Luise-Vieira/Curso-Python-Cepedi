# Pedro Henrique Santos
# Luise Vieira Castro

alunos = []

def cadastrar_aluno():
    try:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")
        notas = []
        for i in range(3):
            n = float(input(f"Digite a nota {i+1} do aluno: "))
            notas.append(n)
        aluno = {"nome": nome, "idade": idade, "curso": curso, "notas": notas}
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!\n")
    except Exception as error:
        print("Erro ao cadastrar aluno:", error)


def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("Lista de alunos cadastrados:")
    for i, a in enumerate(alunos, start=1):
        media = sum(a["notas"]) / len(a["notas"])
        print(
            f"{i}. {a['nome']} - {a['idade']} anos - Curso: {a['curso']} - Média: {media:.2f}")
    print()


def exibir_estatisticas():
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    soma_medias = 0
    melhor_media = -1
    pior_media = 11

    for a in alunos:
        media = sum(a["notas"]) / len(a["notas"])
        soma_medias += media
        if media > melhor_media:
            melhor_media = media
        if media < pior_media:
            pior_media = media

    media_geral = soma_medias / len(alunos)

    print(f"Total de alunos cadastrados: {len(alunos)}")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Melhor média: {melhor_media:.2f}")
    print(f"Pior média: {pior_media:.2f}\n")


def buscar_aluno(nome):
    for a in alunos:
        if a['nome'].lower() == nome.lower():
            print(
                f"Aluno encontrado: {a['nome']} - {a['idade']} anos - Curso: {a['curso']} - Notas: {a['notas']}")
            return
    print("Aluno não encontrado")


def excluir_aluno(nome):
    for a in alunos:
        if a['nome'].lower() == nome.lower():
            print(f"Aluno {a['nome']} removido com sucesso.")
            alunos.remove(a)
            return
    print("Aluno não encontrado")


op = -1
while op != 0:
    print("Menu de opções:")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Exibir estatísticas")
    print("4 - Buscar aluno")
    print("5 - Excluir aluno")
    print("0 - Sair")
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!\n")
        continue

    match op:
        case 1:
            cadastrar_aluno()
        case 2:
            listar_alunos()
        case 3:
            exibir_estatisticas()
        case 4:
            nome = input("Digite o nome que deseja buscar: ")
            buscar_aluno(nome)
        case 5:
            nome = input("Digite o nome que deseja excluir: ")
            excluir_aluno(nome)   
        case 0:
            print("Saindo do sistema...Até logo!")
        case _:
            print("Opção inválida!\n")
