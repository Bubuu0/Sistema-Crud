## Sistema de Cadastro de Livros (Biblioteca CRUD)

> **Projeto Final:** Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade.
> **Instituição:** UniFECAF
> **Disciplina:** Engenharia de Software

##  Descrição do Projeto
Este projeto consiste em um sistema web para o gerenciamento do acervo de uma biblioteca, operando sob a arquitetura de um CRUD (Create, Read, Update, Delete). Desenvolvido em Python, o software utiliza a biblioteca **Streamlit** para fornecer uma interface gráfica interativa e responsiva, e o **SQLite3** como banco de dados relacional embutido para a persistência das informações.

##  Escopo Inicial
O escopo inicial do sistema contemplava a criação de uma entidade principal (`Livro`) com as funcionalidades básicas de gerenciamento:
- **Create:** Cadastro de novos livros contendo Título, Autor e Ano de Publicação.
- **Read:** Visualização dinâmica de todo o acervo cadastrado em formato de tabela (utilizando Pandas).
- **Update:** Atualização dos dados de um livro existente utilizando seu ID.
- **Delete:** Remoção permanente de registros do banco de dados.

##  Metodologia Ágil Adotada
A metodologia ágil escolhida para o gerenciamento e desenvolvimento deste projeto foi o **Kanban**.
A gestão visual do fluxo de trabalho foi implementada através da aba **Projects do GitHub**, dividindo as tarefas do ciclo de vida do software em três colunas estruturais:
- `To Do` (A Fazer): Backlog de funcionalidades, documentações e correções.
- `In Progress` (Em Progresso): Tarefas em desenvolvimento ativo.
- `Done` (Concluído): Entregas finalizadas, testadas e integradas ao repositório via *commits* semânticos.

## Gestão de Mudanças e Alteração de Escopo
Durante o desenvolvimento iterativo e as validações iniciais, identificou-se uma oportunidade de melhoria crítica para a experiência do usuário (o bibliotecário). O cadastro restrito a "Título" e "Autor" tornava a catalogação limitante. 

**A Mudança:** Foi solicitada uma mudança de escopo ágil para a inclusão do campo obrigatório **"Gênero Literário"** na estrutura do banco de dados e na interface de usuário. 
Essa adaptação foi rapidamente absorvida pela metodologia Kanban, sendo documentada em um novo *card* e implementada no fluxo contínuo de desenvolvimento sem comprometer a estabilidade das entregas anteriores, demonstrando a flexibilidade e resiliência da engenharia de software ágil.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Front-end:** Streamlit
- **Back-end/Banco de Dados:** SQLite3
- **Manipulação de Dados:** Pandas
- **Controle de Qualidade / CI:** Pytest e GitHub Actions

---

## Como Executar o Sistema Localmente

Siga os passos abaixo para rodar a aplicação em sua máquina:

**1. Clone o repositório:**
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO
