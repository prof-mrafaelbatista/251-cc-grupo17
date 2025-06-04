
Plataforma de Aprendizado de Programação com Flask e Gemini AI

Este projeto é uma aplicação web desenvolvida em Flask que oferece uma plataforma de aprendizado de programação. Conta com um glossário interativo, informações sobre conceitos de programação, além de integração com a API Gemini da Google para geração de respostas inteligentes.

Funcionalidades

- Página inicial e navegação por níveis de conhecimento (iniciante, intermediário, programador, etc.).
- Glossário colaborativo, onde é possível adicionar, remover e alterar termos.
- Sistema de busca por termos do glossário e também por páginas do site.
- Integração com a IA Gemini para responder perguntas dos usuários.
- Página de cadastro de informações pessoais simples (sobre você).

Tecnologias Utilizadas

- Python
- Flask
- HTML e Jinja (templates)
- CSV para armazenamento de dados
- API Google Gemini AI

Estrutura de Pastas

/templates -> Arquivos HTML (páginas do site)
bd_glossario.csv -> Banco de dados do glossário
bd_sobre_mim.csv -> Banco de dados de textos dos usuários
app.py -> Código principal da aplicação

Instalação

1. Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

2. Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  (Linux/Mac)
venv\Scripts\activate     (Windows)

3. Instale as dependências:

pip install flask google-generativeai requests

4. Configure sua API Key da Google Gemini:

No arquivo app.py, substitua:

python
gemini_api_key = api_key

Por sua chave real da API.

Como Executar

Execute o arquivo app.py:

python app.py

Acesse no navegador:

http://127.0.0.1:5000/


Funcionalidades das Rotas

- `/` - Página inicial
- `/sobre-equipe` - Sobre a equipe
- `/10anos` - Conteúdo para crianças
- `/iniciante` - Conteúdo para iniciantes
- `/intermediario` - Conteúdo intermediário
- `/programador` - Conteúdo avançado
- `/basico` - Conteúdos básicos
- `/selecao` - Estruturas de seleção
- `/vetmat` - Vetores e matrizes
- `/repeticao` - Estruturas de repetição
- `/funepro` - Funções e procedimentos
- `/traexc` - Tratamento de exceções
- `/bibliotecas` - Bibliotecas em Python
- `/datanalise` - Análise de dados
- `/glossario` - Glossário de termos
- `/conta` - Página para escrever informações pessoais
- `/ia` - Página com interação via IA Gemini

Contribuição

Contribuições são bem-vindas. Sinta-se livre para abrir uma issue ou enviar um pull request.

Licença

Este projeto está licenciado sob a licença MIT.
