# Buscar Usuários no GitHub 💥🔙

Este é um projeto desenvolvido em **Flask** que permite ao usuário buscar informações de um perfil do GitHub. O aplicativo recebe o nome de usuário e exibe dados como nome, bio, localização, repositórios públicos e um link para o perfil do GitHub.

## Funcionalidades 🚀

- **Busca de usuário**: Ao inserir o nome de um usuário do GitHub, o sistema busca e exibe informações do perfil.
- **Exibição de informações**:
  - **Nome** 📝
  - **Bio** ✍️
  - **Localização** 🌍
  - **Repositórios Públicos** 📂
  - **Link para o perfil no GitHub** 🔗

## Tecnologias Utilizadas ⚙️

- **Flask**: Framework Python para desenvolvimento web. 🌐
- **Jinja2**: Motor de templates utilizado pelo Flask. 🔧
- **Requests**: Biblioteca para realizar requisições HTTP. 🌐
- **HTML/CSS**: Para a estruturação e estilização da interface. 🎨

## Como Rodar o Projeto 🚦

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/mateuslucianoo/BuscarusuriosGithub.git
   ```

2. **Navegue até o diretório do projeto**:
   ```bash
   cd BuscarusuriosGithub
   ```

3. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   ```

4. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Rode o servidor Flask**:
   ```bash
   python app.py
   ```

7. **Acesse o aplicativo no navegador**:
   Abra seu navegador e vá para: `http://127.0.0.1:5000/` 🌍

---

## Estrutura do Projeto 📂

```bash
├── .venv/                  # Ambiente virtual
├── app.py                  # Código principal do Flask
├── templates/              # Arquivos HTML
│   └── index.html          # Template HTML principal
├── static/                 # Arquivos estáticos (CSS, JS, etc.)
│   └── css/
│       └── styles.css      # Estilo personalizado
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

📝 **Desenvolvedor**: [Mateus Luciano](https://github.com/mateuslucianoo)

