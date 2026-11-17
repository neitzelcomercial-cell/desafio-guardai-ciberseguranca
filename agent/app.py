"""Autenticação de usuários — versão corrigida (sem SQL Injection).

Schema esperado da tabela `usuarios`:
    username      TEXT UNIQUE NOT NULL
    password_hash TEXT NOT NULL

Formato do password_hash: pbkdf2_sha256$<iterações>$<salt_hex>$<hash_hex>

Senhas devem ser armazenadas apenas como hash com salt único por usuário.
Se o banco atual tiver senhas em texto puro, faça a migração: leia cada
senha, chame `gerar_password_hash` e substitua o valor da coluna.
"""

import hashlib
import hmac
import os
import sqlite3
from contextlib import closing

BANCO_DE_DADOS = "banco_de_dados.db"
ITERACOES = 310_000
TAMANHO_SALT = 16
ALGORITMO = "pbkdf2_sha256"


def _derivar(senha: str, salt: bytes, iteracoes: int = ITERACOES) -> bytes:
    """Deriva uma chave a partir da senha usando PBKDF2-HMAC-SHA256."""
    return hashlib.pbkdf2_hmac("sha256", senha.encode("utf-8"), salt, iteracoes)


def gerar_password_hash(senha: str) -> str:
    """Gera um hash com salt aleatório, pronto para ser salvo no banco."""
    salt = os.urandom(TAMANHO_SALT)
    digest = _derivar(senha, salt)
    return f"{ALGORITMO}${ITERACOES}${salt.hex()}${digest.hex()}"


def inicializar_banco() -> None:
    """Cria a tabela com o schema seguro (útil em ambiente novo/testes)."""
    with closing(sqlite3.connect(BANCO_DE_DADOS)) as conexao:
        with conexao:
            conexao.execute(
                """
                CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
                """
            )


def criar_usuario(username: str, senha: str) -> None:
    """Cadastra um usuário armazenando apenas o hash da senha."""
    password_hash = gerar_password_hash(senha)
    with closing(sqlite3.connect(BANCO_DE_DADOS)) as conexao:
        with conexao:
            conexao.execute(
                "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )


def fazer_login(usuario: str, senha: str) -> str:
    """Autentica um usuário. Nunca interpola entradas na consulta SQL."""
    try:
        # Query parametrizada: o valor de 'usuario' é tratado como DADO,
        # nunca como código SQL.
        with closing(sqlite3.connect(BANCO_DE_DADOS)) as conexao:
            cursor = conexao.execute(
                "SELECT password_hash FROM usuarios WHERE username = ?",
                (usuario,),
            )
            registro = cursor.fetchone()
    except sqlite3.Error:
        return "Acesso Negado."

    if registro is None:
        # Gasta o mesmo esforço computacional de um login real para reduzir
        # timing side-channel que permitiria enumerar usernames.
        _derivar(senha, b"\x00" * TAMANHO_SALT)
        return "Acesso Negado."

    try:
        algoritmo, iteracoes_txt, salt_hex, hash_hex = registro[0].split("$", 3)
        if algoritmo != ALGORITMO:
            return "Acesso Negado."
        hashes = bytes.fromhex(hash_hex)
        calculado = _derivar(senha, bytes.fromhex(salt_hex), int(iteracoes_txt))
    except (ValueError, TypeError):
        return "Acesso Negado."

    # Comparação em tempo constante evita timing attacks sobre o hash.
    if hmac.compare_digest(hashes, calculado):
        return "Acesso Permitido!"
    return "Acesso Negado."