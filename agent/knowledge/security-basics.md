
---
name: basic-security
description: Base de conhecimentos sobre fundamentos de segurança da informação, conceitos essenciais, boas práticas e princípios de proteção de sistemas e dados.
---

# Basic Security — Base de Referências

## 1. Objetivo

Reunir conhecimentos fundamentais de segurança da informação para auxiliar nos estudos, análises de segurança, identificação de riscos e aplicação de boas práticas de proteção.

## 2. Conceitos fundamentais de segurança

A segurança da informação tem como objetivo proteger dados, sistemas e serviços. Seus três princípios fundamentais são conhecidos como Tríade CIA.

### 2.1 Confidencialidade (Confidentiality)

Garante que as informações sejam acessadas somente por pessoas, sistemas ou processos autorizados.

**Exemplos:**
- Utilizar senhas fortes.
- Implementar autenticação multifator (MFA).
- Restringir o acesso a arquivos e sistemas.
- Criptografar informações sensíveis.
- Evitar compartilhar dados confidenciais.

**Riscos:** vazamento de informações, exposição de dados pessoais e acesso não autorizado.

### 2.2 Integridade (Integrity)

Garante que as informações permaneçam corretas, completas e protegidas contra alterações não autorizadas ou acidentais.

**Exemplos:**
- Controlar permissões de edição.
- Utilizar hashes para verificar a integridade de arquivos.
- Manter registros de alterações (logs).
- Realizar backups.
- Proteger bancos de dados contra modificações indevidas.

**Riscos:** adulteração de informações, corrupção de arquivos e alterações indevidas em registros.

### 2.3 Disponibilidade (Availability)

Garante que sistemas, serviços e informações estejam acessíveis quando necessário aos usuários autorizados.

**Exemplos:**
- Realizar backups regularmente.
- Manter sistemas atualizados.
- Monitorar servidores e serviços.
- Utilizar mecanismos de redundância.
- Implementar medidas de recuperação após falhas.

**Riscos:** interrupção de serviços, indisponibilidade de sistemas e perda de produtividade.

### 2.4 Relação entre os três princípios

Os três princípios trabalham em conjunto:

- Confidencialidade: impede o acesso indevido.
- Integridade: impede alterações indevidas.
- Disponibilidade: garante o acesso quando necessário.

## 3. Boas práticas de segurança

### 3.1 Senhas e autenticação
- Criar senhas longas, fortes e exclusivas.
- Evitar reutilizar senhas em diferentes serviços.
- Utilizar gerenciadores de senhas.
- Ativar autenticação multifator (MFA).
- Nunca compartilhar senhas ou códigos de autenticação.

### 3.2 Atualizações e correções
- Manter sistemas operacionais atualizados.
- Instalar atualizações de segurança.
- Atualizar aplicativos e ferramentas.
- Remover programas desnecessários.
- Corrigir vulnerabilidades conhecidas.

### 3.3 Controle de acesso
- Aplicar o princípio do menor privilégio.
- Utilizar contas individuais.
- Evitar utilizar contas administrativas em tarefas comuns.
- Revisar permissões periodicamente.
- Remover acessos que não são mais necessários.

### 3.4 Proteção de dados
- Realizar backups periódicos.
- Criptografar informações sensíveis.
- Proteger arquivos e documentos.
- Utilizar armazenamento confiável.
- Evitar compartilhar informações confidenciais em ambientes não confiáveis.

### 3.5 Navegação e engenharia social
- Verificar remetentes de e-mails.
- Desconfiar de links suspeitos.
- Não abrir anexos desconhecidos.
- Identificar tentativas de phishing.
- Confirmar solicitações sensíveis por canais confiáveis.

### 3.6 Segurança de dispositivos e redes
- Utilizar firewall.
- Manter proteção antimalware.
- Proteger redes Wi-Fi.
- Bloquear dispositivos quando não estiverem em uso.
- Evitar conectar dispositivos USB desconhecidos.
- Utilizar conexões seguras.

### 3.7 Monitoramento e resposta a incidentes
- Monitorar atividades suspeitas.
- Analisar registros de eventos (logs).
- Identificar comportamentos anormais.
- Registrar incidentes de segurança.
- Preservar evidências.
- Comunicar incidentes aos responsáveis.

## 4. Princípios complementares

### Menor privilégio
Cada usuário deve possuir somente as permissões necessárias para executar suas atividades.

### Defesa em profundidade
Utilizar diferentes camadas de segurança para evitar que uma única falha comprometa todo o ambiente.

### Gestão de riscos
Identificar ameaças, vulnerabilidades, impactos e medidas de proteção.

### Segurança desde o início
Considerar segurança durante o planejamento, desenvolvimento e configuração de sistemas.

### Autorização
Realizar testes de segurança somente em sistemas próprios ou com autorização explícita e dentro do escopo permitido.

## 5. Checklist básico de segurança

- [ ] Utilizar senhas fortes e exclusivas.
- [ ] Ativar autenticação multifator.
- [ ] Manter sistemas atualizados.
- [ ] Configurar firewall.
- [ ] Realizar backups.
- [ ] Revisar permissões de acesso.
- [ ] Proteger informações confidenciais.
- [ ] Verificar links e anexos suspeitos.
- [ ] Monitorar atividades suspeitas.
- [ ] Conhecer os procedimentos de resposta a incidentes.

## 6. Referências para aprofundamento

- NIST Cybersecurity Framework (CSF).
- NIST SP 800-12 — An Introduction to Information Security.
- ISO/IEC 27001 — Sistema de Gestão de Segurança da Informação.
- CIS Critical Security Controls.
- OWASP — Open Worldwide Application Security Project.

---

**Observação:** material introdutório para estudos e atividades de segurança em ambientes autorizados.
