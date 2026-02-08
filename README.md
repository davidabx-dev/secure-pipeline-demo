# 🛡️ Apple DevSecOps Demo Pipeline

Este projeto demonstra um pipeline completo de **DevSecOps** (CI/CD) com verificação automática de vulnerabilidades, simulando um ambiente de produção seguro.

## 🚀 Tecnologias Utilizadas
* **Aplicação:** Python (Flask)
* **Containerização:** Docker
* **CI/CD:** GitHub Actions
* **Security (SAST/SCA):** Trivy (Aqua Security)
* **Infraestrutura:** Linux (Debian-based images)

## ⚙️ Como Funciona o Pipeline
O workflow automatizado realiza as seguintes etapas a cada `git push`:
1.  **Build:** Constrói a imagem Docker da aplicação.
2.  **Security Scan:** O scanner **Trivy** analisa a imagem em busca de vulnerabilidades (CVEs) no Sistema Operacional e nas dependências Python.
3.  **Quality Gate:** Se vulnerabilidades de nível `CRITICAL` ou `HIGH` forem encontradas, o pipeline **bloqueia** o processo (Falha intencional), impedindo o deploy de código inseguro.

## 📸 Evidências
Este repositório prova a capacidade de identificar falhas de segurança (Logs de erro no Actions) e remediar vulnerabilidades atualizando dependências e imagens base.
