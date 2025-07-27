# Analisador de Currículos com IA

Este é um projeto de análise de currículos que utiliza a API da Groq para gerar **resumos críticos**, **pontuações personalizadas** e **comparações entre candidatos**, com base nos requisitos de uma vaga específica. O projeto é desenvolvido em **Python**, utilizando **Streamlit** como interface web interativa.

---

## 🔍 Funcionalidades

* **📤 Upload em Lote de Currículos**
  Permite o envio de múltiplos arquivos `.pdf` de uma só vez.

* **📊 Análise e Pontuação Automatizada**
  Cada currículo é avaliado com base nos critérios da vaga, e recebe uma pontuação entre 0 e 100.

* **📈 Comparação Lado a Lado**
  Interface para comparar os candidatos mais bem pontuados com análises detalhadas.

* **🧠 Resumo Crítico via IA**
  Geração de um resumo textual com os pontos fortes e fracos de cada currículo, segundo a vaga.

---

## 🛠 Tecnologias Utilizadas

* **Python**: Linguagem principal do projeto.
* **Streamlit**: Framework para criação de dashboards interativos.
* **Groq (modelo Llama 3.1)**: Modelo de linguagem usado para resumir e pontuar os currículos.
* **TinyDB**: Banco de dados leve, utilizado para armazenar dados locais.
* **Poetry**: Ferramenta de gerenciamento de dependências e ambientes virtuais.

---

## ✅ Pré-requisitos

* Python 3.10 ou superior
* Poetry instalado globalmente
* Chave de API da Groq válida


## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
