"""
EXEMPLO DIDÁTICO — CÓDIGO INTENCIONALMENTE VULNERÁVEL.

Este módulo reproduz de propósito uma falha de SQL Injection na função
`fazer_login()`. Ele existe apenas para laboratório e estudo: mostra como
uma entrada do usuário concatenada diretamente na consulta SQL muda o
comando que o banco executa.

NÃO USE ESTE CÓDIGO EM PRODUÇÃO, EM SISTEMAS DE TERCEIROS NEM FORA DE UM
AMBIENTE DE ESTUDO AUTORIZADO.

Detalhes didáticos:
- o banco é SQLite em memória (`:memory:`), então nenhum arquivo é criado;
- `criar_usuario()` usa consulta parametrizada — a falha existe SOMENTE em
  `fazer_login()`, para demonstrar que uma parte segura do sistema não
  protege automaticamente as outras;
- as senhas ficam em texto puro apenas para facilitar a leitura do exemplo.
  Em um sistema real, use hash com salt (PBKDF2, bcrypt ou Argon2).
"""

import sqlite3

# Uma única conexão é compartilhada porque, no SQLite, cada conexão `:memory:`
# possui o seu próprio banco isolado. Com duas conexões, a tabela criada aqui
# não existiria na conexão usada pelo login e a demonstração não funcionaria.
CONEXAO = sqlite3.connect(":memory:")


def inicializar_banco() -> None:
    """Cria a tabela `usuarios` no banco em memória.

    A coluna `senha` armazena texto puro SOMENTE para fins didáticos.
    """
    CONEXAO.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
        """
    )
    CONEXAO.commit()


def criar_usuario(usuario: str, senha: str) -> None:
    """Cadastra um usuário com consulta PARAMETRIZADA (parte segura).

    O placeholder `?` faz o driver tratar os valores como dados, nunca como
    código SQL. Note que essa boa prática, sozinha, não protege o login: a
    vulnerabilidade está em `fazer_login()`.
    """
    CONEXAO.execute(
        "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
        (usuario, senha),
    )
    CONEXAO.commit()


def fazer_login(usuario: str, senha: str) -> str:
    """Autentica concatenando as entradas na SQL — VULNERÁVEL a SQL Injection.

    O f-string abaixo cola o texto digitado dentro da consulta. Se a pessoa
    enviar aspas, elas fecham a literal e o restante vira comando SQL.

    Exemplo de payload no campo `usuario`:  ' OR 1=1 --
    A consulta resultante termina em: WHERE usuario = '' OR 1=1 --' ...
    A condição `1=1` é sempre verdadeira e o `--` comenta o restante da
    linha, então `fetchone()` devolve a primeira linha da tabela.
    """
    consulta = (
        f"SELECT * FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )

    resultado = CONEXAO.execute(consulta).fetchone()

    if resultado:
        return "Acesso Permitido!"
    return "Acesso Negado."


if __name__ == "__main__":
    print("AMBIENTE DIDÁTICO — código intencionalmente vulnerável")
    print("Credenciais fictícias: admin / senha123\n")

    inicializar_banco()
    criar_usuario("admin", "senha123")

    print("login correto:          ", fazer_login("admin", "senha123"))
    print("senha incorreta:        ", fazer_login("admin", "senha_errada"))
    print("injection no usuario:   ", fazer_login("' OR 1=1 --", "senha_errada"))
    print("injection na senha:     ", fazer_login("qualquer", "' OR '1'='1"))

    senha_salva = CONEXAO.execute("SELECT senha FROM usuarios").fetchone()[0]
    print("senha salva (texto puro):", senha_salva)
