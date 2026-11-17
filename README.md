# 🤖 DIO Agent

> Seu mentor com Inteligência Artificial para aprender mais e melhor na [DIO](https://dio.me).

O **DIO Agent** é um agente de IA que acompanha você na sua jornada de estudos. Ele conhece as experiências da DIO (Bootcamps, Formações, Cursos, Desafios e muito mais) e ajuda você a estudar, praticar e planejar a sua carreira.

Você não precisa saber programar nem instalar nada complicado. Em **3 passos**, o seu mentor está pronto para usar.

---

## ✨ Três palavras para começar

- 🧠 **Agente de IA:** um chatbot responde perguntas. Um *agente* vai além: lê, planeja e executa passos para ajudar você a alcançar um objetivo. É a diferença entre alguém que explica o caminho e alguém que caminha junto com você.
- 🖥️ **Harness:** é o programa onde o agente roda. O agente é o mentor, e o harness é a sala onde vocês se encontram. O mesmo mentor atende em salas diferentes, por isso o DIO Agent funciona em vários harnesses.
- 🧩 **Skill:** é uma habilidade do agente, descrita em um guia passo a passo. Você não precisa chamar a skill: o agente percebe o que você precisa e usa a certa sozinho.

Esses e outros termos estão no [Glossário](docs/glossary.md).

---

## 🚀 Comece em 3 passos

### 1️⃣ Instale um harness

Recomendamos o **Google Antigravity**, que tem limites de uso generosos para quem está começando. Mas qualquer harness da lista funciona: escolha um e siga a instalação da documentação oficial dele.

| Harness | Documentação oficial |
|---------|----------------------|
| Google Antigravity (recomendado) | https://antigravity.google/docs |
| Claude Code | https://code.claude.com/docs |
| Codex | https://developers.openai.com/codex |
| OpenCode | https://opencode.ai/docs |
| Hermes | https://hermes-agent.nousresearch.com/docs |

### 2️⃣ Baixe o DIO Agent e abra no harness

Baixe este repositório do jeito mais simples para você:

- **Com Git:** no terminal, rode `git clone https://github.com/digitalinnovationone/dio-agent.git`
- **Sem Git:** no topo desta página, clique no botão verde **Code**, depois em **Download ZIP**, e extraia a pasta.

Depois, abra no harness a pasta do projeto, a que tem o arquivo `AGENTS.md` (pelo Git, ela se chama `dio-agent`; pelo .zip, `dio-agent-main`). O harness lê esse arquivo sozinho, e o agente já sabe quem é: o seu mentor de estudos da DIO.

### 3️⃣ Converse

Fale naturalmente, com as suas palavras. Nas primeiras vezes, vale usar um dos [modelos de prompt](#-modelos-de-prompt) abaixo: quanto mais contexto você dá, melhor o agente ajuda.

---

## 🛡️ GuardAI: especialização em cibersegurança

O **GuardAI** é a especialização do DIO Agent em cibersegurança e análise de vulnerabilidades. Ele complementa o mentor descrito acima — você continua podendo pedir um plano de estudos, ajuda em desafios ou orientação de carreira — e acrescenta um modo de atuação quando o assunto é segurança.

Quando você pede uma análise de segurança, o GuardAI:

- explica o que é a falha, por que ela acontece e qual princípio ela afeta: confidencialidade, integridade e disponibilidade (Tríade CIA);
- avalia risco com probabilidade e severidade, justificando a classificação e diferenciando fatos confirmados de hipóteses;
- mostra como um profissional investiga, prioriza correções e verifica se você entendeu o conceito;
- usa exemplos práticos e demonstrações de correção para ensinar, sem entregar respostas prontas de desafios.

A melhoria escolhida para este desafio foi: **especialização do DIO Agent em cibersegurança e análise de vulnerabilidades, com orientação didática e demonstrações práticas de correção de falhas**.

A base conceitual está em `agent/knowledge/security-basics.md`, o passo a passo em `skills/vulnerability-analysis/SKILL.md`, e os exemplos práticos em `agent/app_vulnerable.py` e `agent/app.py`.

---

## 🧭 Executando o agente no Hermes

Os comandos abaixo seguem a [documentação oficial do Hermes](https://hermes-agent.nousresearch.com/docs).

1. Instale o Hermes. No Windows, em PowerShell: `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`. No Linux, macOS ou WSL2: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`. Também há instalador Desktop em https://hermes-agent.nousresearch.com/.
2. Configure o provedor do modelo com `hermes model` (ou use `hermes setup` para o assistente completo). O modelo precisa de pelo menos 64 mil tokens de contexto.
3. No terminal, entre na pasta do projeto — a que contém `AGENTS.md` — e inicie o agente com `hermes` (CLI clássica) ou `hermes --tui` (interface recomendada).
4. O Hermes carrega o `AGENTS.md` da pasta de trabalho automaticamente ao iniciar: não é preciso importar nada. Converse em linguagem natural, como nos modelos de prompt abaixo.
5. Se algo não funcionar, `hermes doctor` mostra o diagnóstico.

---

## 🧩 As skills do agente

| Skill | Para que serve | Experimente pedir |
|-------|----------------|-------------------|
| [Plano de estudos](skills/study-plan/SKILL.md) | Organiza o que estudar, em que ordem e em quanto tempo | "Quero concluir este Bootcamp em 2 meses, me ajuda?" |
| [Destravar desafio](skills/unblock-challenge/SKILL.md) | Conduz você até a solução de um desafio, sem dar a resposta pronta | "Travei nesse desafio, me ajuda?" |
| [Explicar conceito](skills/explain-concept/SKILL.md) | Explica conceitos de forma simples, com analogias e exemplos | "Não entendi o que é uma API." |
| [Pesquisa na web](skills/web-search/SKILL.md) | Responde dúvidas atuais (versões, lançamentos, mercado) com fontes citadas | "Qual a versão estável do Node hoje?" |
| [Revisão de portfólio](skills/portfolio-review/SKILL.md) | Dá feedback sobre o seu portfólio e GitHub antes de buscar vagas | "O que falta no meu GitHub para uma vaga júnior?" |
| [Caminho AI Builder](skills/ai-builder-path/SKILL.md) | Ajuda você a escolher o próximo passo na Carreira AI Builder | "Qual Formação AI Builder combina comigo?" |
| [Análise de vulnerabilidades](skills/vulnerability-analysis/SKILL.md) | Analisa falhas de segurança com abordagem defensiva e didática, avaliando risco e boas práticas | "Encontrei uma falha de segurança, como analiso o risco?" |

A pesquisa na web usa a busca do seu harness. Se ele não tiver busca própria, veja [como conectar o You.com](docs/youcom-mcp.md), que tem uma opção gratuita.

---

## 📝 Modelos de prompt

Copie, preencha o que está entre colchetes e envie. Não precisa de formato perfeito: o agente pede mais detalhes se precisar.

**🗺️ Plano de estudos**

```
Quero montar um plano de estudos.
- Meu objetivo: [ex: ser dev back-end, concluir um Bootcamp]
- O que quero fazer na DIO: [link ou nome do Bootcamp, Formação, Aceleração ou Carreira]
- O que já tenho: [um plano de ação ou de estudos, se tiver]
- Meu nível hoje: [iniciante, intermediário, avançado]
- Tempo disponível: [ex: 1 hora por dia, de segunda a sexta]
```

**🔓 Destravar desafio**

```
Estou travado em um Desafio de [Código, Projeto ou Criativo] da DIO.
- O que o desafio pede: [cole o enunciado ou, no Desafio de Projeto, o link do repositório do desafio]
- Onde eu travei: [explique o ponto da dificuldade]
- Meu código ou repositório: [cole o código ou o link, se tiver]
Me ajuda a destravar sem dar a resposta pronta.
```

**💡 Explicar conceito**

```
Me explica o conceito de [ex: API, laço de repetição, herança].
- Meu nível: [nunca vi, já ouvi falar, quero aprofundar]
```

**🧭 Caminho AI Builder**

```
Quero escolher meu próximo passo na Carreira AI Builder.
- O que quero construir com IA: [ex: um produto para o meu negócio, um software, agentes que automatizam processos, ainda não sei]
- Minha experiência com programação: [nenhuma, o básico, trabalho com desenvolvimento]
- Meu objetivo: [ex: mudar de carreira, tirar uma ideia do papel]
```

---

## 🔄 Mantenha o DIO Agent atualizado

O DIO Agent evolui com o tempo. Se você usou Git, rode `git pull` no terminal, dentro da pasta (ou peça para o próprio agente rodar). Se baixou o .zip, baixe de novo.

---

## 🗂️ Estrutura do repositório

```
dio-agent/
├── README.md                  Este guia
├── AGENTS.md                  Definição do agente (lida pelo harness)
├── CLAUDE.md                  Atalho para o Claude Code
├── agent/
│   ├── persona.md             A personalidade e o tom do agente
│   ├── app.py                 Autenticação corrigida (exemplo seguro)
│   ├── app_vulnerable.py      Exemplo didático vulnerável (laboratório)
│   └── knowledge/             O que o agente sabe sobre a DIO
│       ├── dio-platform.md    Como a DIO funciona e organiza Carreiras
│       ├── learning-experiences.md  Bootcamps, Formações, Cursos e Desafios
│       └── security-basics.md Fundamentos de segurança e Tríade CIA
├── skills/                    Uma pasta por skill, cada uma com o seu SKILL.md
│   └── vulnerability-analysis/  Análise de vulnerabilidades (GuardAI)
└── docs/
    ├── glossary.md            Glossário de termos
    └── youcom-mcp.md          Como conectar a busca do You.com
```

---

## 🛠️ Arquivos criados e modificados neste desafio

O `git status --short` conferido ao final do trabalho mostrou:

```
 M .gitignore
 M AGENTS.md
 M agent/persona.md
 M README.md
?? agent/app.py
?? agent/app_vulnerable.py
?? agent/knowledge/security-basics.md
?? skills/vulnerability-analysis/
```

- **Modificados:** `.gitignore` (ignora `__pycache__/` e `*.py[cod]`), `AGENTS.md` (base de conhecimento e seção "Security Skills"), `agent/persona.md` (seção de especialização em segurança) e `README.md` (esta documentação).
- **Criados:** `agent/knowledge/security-basics.md`, `skills/vulnerability-analysis/` (`SKILL.md`, `README.md` e `image.png`), `agent/app.py` e `agent/app_vulnerable.py`.

O diretório `agent/__pycache__/` pode aparecer no sistema de arquivos após executar o Python, mas está fora do Git pela regra adicionada ao `.gitignore`.

---

## 🔍 Diferença entre app_vulnerable.py e app.py

| Aspecto | `agent/app_vulnerable.py` | `agent/app.py` |
|---------|---------------------------|----------------|
| Finalidade | Exemplo didático intencionalmente vulnerável | Versão corrigida, usada como referência |
| Banco | SQLite em memória (`:memory:`) | SQLite em arquivo (`banco_de_dados.db`) |
| Consulta de login | f-string com `usuario` e `senha` interpolados | `SELECT password_hash ... WHERE username = ?`, com valor em tupla |
| Verificação da senha | Feita pelo próprio SQL (`AND senha = '...'`) | Derivação PBKDF2 em Python e comparação com `hmac.compare_digest` |
| Armazenamento | Senha em texto puro | `pbkdf2_sha256$310000$<salt>$<hash>` |
| Parâmetros | `INSERT` parametrizado; `SELECT` vulnerável | `INSERT` e `SELECT` parametrizados |
| Controles adicionais | Nenhum | Salt aleatório de 16 bytes, 310.000 iterações, validação de formato, mensagens uniformes e derivação dummy |

O ponto central: o `INSERT` parametrizado da versão vulnerável **não** protege o `SELECT`. Parametrização vale para a declaração em que o `?` aparece; a mesma string que é inofensiva ao ser gravada volta a ser código quando é colada dentro de outra consulta por f-string.

---

## 🧪 Testes comparativos realizados

Os testes rodaram em **ambiente isolado**, com cópias dos dois arquivos em diretório temporário e apenas credenciais fictícias (`admin` / `senha123`). A versão vulnerável usou banco em memória e a corrigida, um arquivo temporário. Não foi criado nenhum arquivo de banco de dados no repositório: `find . -name '*.db'` retornou vazio.

| Teste | `app_vulnerable.py` | `app.py` |
|-------|---------------------|----------|
| Login correto | Acesso Permitido! | Acesso Permitido! |
| Senha incorreta | Acesso Negado. | Acesso Negado. |
| Usuário inexistente | Acesso Negado. | Acesso Negado. |
| `' OR 1=1 --` no usuário | **Acesso Permitido!** | **Acesso Negado.** |
| `' OR '1'='1` na senha | **Acesso Permitido!** | **Acesso Negado.** |
| `admin' UNION SELECT 1,2,3 --` | **Acesso Permitido!** | **Acesso Negado.** |

Os três payloads de SQL Injection que burlecaram a autenticação na versão vulnerável foram **todos negados** na versão corrigida. Todas as asserções do script comparativo passaram.

Quanto ao armazenamento: na versão vulnerável a linha salva foi `senha123` em texto puro; na corrigida foi `pbkdf2_sha256$310000$...`, com salt de 16 bytes, e a string `senha123` não aparece nos bytes do arquivo do banco.

Esses resultados valem para o laboratório. Controles de produção — limites de tentativas no gateway, permissões do arquivo e registro de logs — precisam ser verificados separadamente; a versão corrigida ainda não possui rate limiting nem política de senhas.

---

## 🤝 Contribua

Tem uma ideia de skill? Veja [como criar uma skill](skills/README.md) e abra um pull request.

---

## 💬 Sobre este projeto

O DIO Agent foi criado para acompanhar você nos Bootcamps e Formações da DIO. A ideia é simples: aprender na era da IA fica mais fácil quando você tem um mentor disponível a qualquer hora.

Bons estudos, e vem com a gente. 🚀
