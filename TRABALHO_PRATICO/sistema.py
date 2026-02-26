import csv
import os

USUARIOS_ARQ = "usuarios.csv"
PRODUTOS_ARQ = "produtos.csv"


# =========================
# UTILIDADES ARQUIVOS
# =========================

def inicializar_arquivos():
    """Cria arquivos padrão com dados iniciais caso não existam."""
    if not os.path.exists(USUARIOS_ARQ):
        with open(USUARIOS_ARQ, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "senha", "nivel"])
            writer.writerow(["admin", "123", "gerente"])
            writer.writerow(["func1", "123", "funcionario"])

    if not os.path.exists(PRODUTOS_ARQ):
        with open(PRODUTOS_ARQ, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["codigo", "nome", "preco", "quantidade"])
            writer.writerow(["1", "Caneta", "2.5", "100"])
            writer.writerow(["2", "Caderno", "15.0", "50"])


# =========================
# USUÁRIOS
# =========================

def carregar_usuarios():
    """Carrega usuários do arquivo para lista de dicionários."""
    usuarios = []
    with open(USUARIOS_ARQ, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuarios.append(row)
    return usuarios


def salvar_usuarios(lista):
    """Salva lista de usuários no arquivo."""
    with open(USUARIOS_ARQ, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "senha", "nivel"])
        writer.writeheader()
        writer.writerows(lista)


def criar_usuario():
    """Cria novo usuário."""
    usuarios = carregar_usuarios()
    username = input("Username: ")
    senha = input("Senha: ")
    nivel = input("Nivel (gerente/funcionario): ")
    usuarios.append({"username": username, "senha": senha, "nivel": nivel})
    salvar_usuarios(usuarios)


def listar_usuarios():
    """Lista todos os usuários."""
    for u in carregar_usuarios():
        print(u)


def atualizar_usuario():
    """Atualiza senha de um usuário."""
    usuarios = carregar_usuarios()
    username = input("Username: ")
    for u in usuarios:
        if u["username"] == username:
            u["senha"] = input("Nova senha: ")
    salvar_usuarios(usuarios)


def deletar_usuario():
    """Remove usuário."""
    usuarios = carregar_usuarios()
    username = input("Username: ")
    usuarios = [u for u in usuarios if u["username"] != username]
    salvar_usuarios(usuarios)


def login():
    """Realiza login e retorna nível do usuário."""
    usuarios = carregar_usuarios()
    username = input("Login: ")
    senha = input("Senha: ")
    for u in usuarios:
        if u["username"] == username and u["senha"] == senha:
            return u["nivel"]
    return None


# =========================
# PRODUTOS
# =========================

def carregar_produtos():
    """Carrega produtos para lista de dicionários."""
    produtos = []
    with open(PRODUTOS_ARQ, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["preco"] = float(row["preco"])
            row["quantidade"] = int(row["quantidade"])
            produtos.append(row)
    return produtos


def salvar_produtos(lista):
    """Salva lista de produtos no arquivo."""
    with open(PRODUTOS_ARQ, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["codigo", "nome", "preco", "quantidade"])
        writer.writeheader()
        writer.writerows(lista)


def criar_produto():
    """Adiciona novo produto."""
    produtos = carregar_produtos()
    codigo = input("Codigo: ")
    nome = input("Nome: ")
    preco = float(input("Preco: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)


def listar_produtos():
    """Lista todos produtos."""
    for p in carregar_produtos():
        print(p)


def buscar_produto():
    """Busca produto por código."""
    codigo = input("Codigo: ")
    for p in carregar_produtos():
        if p["codigo"] == codigo:
            print(p)


def atualizar_produto():
    """Atualiza preço e quantidade."""
    produtos = carregar_produtos()
    codigo = input("Codigo: ")
    for p in produtos:
        if p["codigo"] == codigo:
            p["preco"] = float(input("Novo preco: "))
            p["quantidade"] = int(input("Nova quantidade: "))
    salvar_produtos(produtos)


def deletar_produto():
    """Remove produto."""
    produtos = carregar_produtos()
    codigo = input("Codigo: ")
    produtos = [p for p in produtos if p["codigo"] != codigo]
    salvar_produtos(produtos)


def ordenar_por_nome():
    """Imprime produtos ordenados por nome."""
    produtos = sorted(carregar_produtos(), key=lambda x: x["nome"])
    for p in produtos:
        print(p)


def ordenar_por_preco():
    """Imprime produtos ordenados por preço."""
    produtos = sorted(carregar_produtos(), key=lambda x: x["preco"])
    for p in produtos:
        print(p)


# =========================
# MENU PRINCIPAL
# =========================

def menu_usuarios():
    while True:
        print("\n1-Criar 2-Listar 3-Atualizar 4-Deletar 0-Voltar")
        op = input("Opcao: ")
        if op == "1":
            criar_usuario()
        elif op == "2":
            listar_usuarios()
        elif op == "3":
            atualizar_usuario()
        elif op == "4":
            deletar_usuario()
        elif op == "0":
            break


def menu_produtos():
    while True:
        print("\n1-Criar 2-Listar 3-Buscar 4-Atualizar 5-Deletar 6-Ordenar Nome 7-Ordenar Preco 0-Voltar")
        op = input("Opcao: ")
        if op == "1":
            criar_produto()
        elif op == "2":
            listar_produtos()
        elif op == "3":
            buscar_produto()
        elif op == "4":
            atualizar_produto()
        elif op == "5":
            deletar_produto()
        elif op == "6":
            ordenar_por_nome()
        elif op == "7":
            ordenar_por_preco()
        elif op == "0":
            break


def main():
    inicializar_arquivos()
    nivel = login()
    if not nivel:
        print("Login inválido")
        return

    while True:
        print("\n1-Usuarios 2-Produtos 0-Sair")
        op = input("Opcao: ")

        if op == "1" and nivel == "gerente":
            menu_usuarios()
        elif op == "2":
            menu_produtos()
        elif op == "0":
            break
        else:
            print("Acesso negado")


if __name__ == "__main__":
    main()