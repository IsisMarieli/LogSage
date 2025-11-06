# 📋 Residência Tecnológica - GrowUp 2025.2 | SQUAD 48 | Projeto Banco do Brasil - LogSage

## 🚀 Preparação do Ambiente: Clonagem e Instalação de Dependências

Este guia foca nos passos iniciais para configurar o ambiente de desenvolvimento do **LogSage**, incluindo a clonagem do repositório e a instalação das bibliotecas Python necessárias.

### 1. ⚙️ Pré-requisitos

Certifique-se de que os seguintes softwares estão instalados e configurados em sua máquina:

* **Python 3** (Recomendado versão 3.8+)
* **Git**

### 2. 🎣 Clonagem do Repositório

O primeiro passo é obter o código-fonte do projeto.

1.  **Abra o terminal** (ou prompt de comando) na pasta onde deseja armazenar o projeto.
2.  **Execute o comando** de clonagem:

    ```bash
    git clone https://github.com/IsisMarieli/LogSage
    ```

3.  **Acesse a pasta** do projeto:

    ```bash
    cd LogSage
    ```

### 3. 🐍 Criação e Ativação do Ambiente Virtual (venv)

É **crucial** utilizar um ambiente virtual para isolar as dependências do projeto, evitando conflitos com outras instalações Python.

1.  **Crie o ambiente virtual** na pasta raiz do projeto:

    ```bash
    python -m venv venv
    ```

2.  **Ative o ambiente virtual**:

    * **No Windows (PowerShell/CMD):**
        ```bash
        .\venv\Scripts\activate
        ```
    * **No Linux/macOS (ou WSL):**
        ```bash
        source venv/bin/activate
        ```

    > 💡 **Nota:** Após a ativação, você verá `(venv)` no início da linha de comando, indicando que o ambiente está ativo.

### 4. 📦 Instalação das Dependências

Com o ambiente virtual ativo, instale todas as bibliotecas Python listadas no arquivo `requirements.txt`.

1.  **Execute o comando** de instalação:

    ```bash
    pip install -r requirements.txt
    ```

---

✅ O ambiente de desenvolvimento está agora configurado e pronto para a próxima fase.

* ***Próximo Passo:*** Inicializar a infraestrutura de Backend com o Docker.