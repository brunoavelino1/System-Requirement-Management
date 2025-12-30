<p align="center">
  <img src="https://img.shields.io/github/languages/top/brunoavelino1/System-Requirement-Management?style=for-the-badge&color=blue" alt="Python">
  <img src="https://img.shields.io/github/repo-size/brunoavelino1/System-Requirement-Management?style=for-the-badge" alt="Repo Size">
  <img src="https://img.shields.io/github/license/brunoavelino1/System-Requirement-Management?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/ISO-29148-orange?style=for-the-badge" alt="ISO 29148">
</p>

# 🛠️ System Requirement Management

<img width="1335" height="561" alt="image" src="https://github.com/user-attachments/assets/493774f0-484f-4702-9007-51c7dde7360c" />


**System Requirement Manager** é uma ferramenta leve e robusta para Gestão de Requisitos, projetada para transformar Backlogs genéricos em Especificações de Requisitos de Software (SRS) profissionais, seguindo as diretrizes da norma **ISO/IEC/IEEE 29148**.

O diferencial desta ferramenta não é apenas armazenar texto, mas garantir a **qualidade semântica** dos requisitos através de validações automáticas de atomicidade e unicidade.


## 🚀 Funcionalidades Principais

-   **Validador de Atomicidade:** Algoritmo que impede a criação de requisitos compostos (uso de conjunções como "e", "ou"), forçando a quebra em unidades menores.
-   **Serialização Inteligente:** Geração automática de identificadores únicos por categoria (ex: `RF-001`, `RNF-001`, `RN-001`).
-   **Categorização ISO:** Organização nativa entre Requisitos de Negócio, Funcionais e Não Funcionais (Atributos de Qualidade).
-   **Exportação Profissional:** Gerador de documentos `.docx` (Microsoft Word) formatado para entrega técnica.
-   **Interface Clean:** Dashboards simples baseados em Bootstrap 5 para rápida gestão de backlog.

## 📐 Conformidade Técnica

O sistema aplica os princípios de:
1. **Unicidade:** Cada requisito possui um identificador único e global.
2. **Atomicidade:** Cada entrada descreve apenas uma única função ou restrição.
3. **Rastreabilidade:** Estrutura pronta para futuras implementações de matriz de rastreabilidade (RTM).

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x + Flask
- **Banco de Dados:** SQLite (leve e sem configuração necessária)
- **Frontend:** Jinja2 + Bootstrap 5 + FontAwesome
- **Documentação:** Python-Docx

## 📦 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/brunoavelino1/System-Requirement-Management.git
   cd System-Requirement-Management
   pip install -r requirements.txt
   python app.py
   ```
