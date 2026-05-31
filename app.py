import streamlit as st
import pandas as pd
import backend

# Inicializa o banco de dados e cria a tabela se não existir
backend.criar_tabela()

# Configuração da página
st.set_page_config(page_title="Biblioteca CRUD", page_icon="📚", layout="centered")

st.title("📚 Sistema de Cadastro de Livros")

# Menu lateral para navegação
st.sidebar.title("Navegação")
menu = st.sidebar.radio(
    "Escolha uma ação:", 
    ["➕ Adicionar Livro", "📖 Visualizar Livros", "✏️ Atualizar Livro", "❌ Deletar Livro"]
)

st.write("---")

# ----------------- CREATE -----------------
if menu == "➕ Adicionar Livro":
    st.subheader("Adicionar um Novo Livro")
    
    with st.form(key="add_form"):
        categoria = st.selectbox(
    "Categoria",
    [
        "Romance",
        "Fantasia",
        "Ficção Científica",
        "Tecnologia",
        "História",
        "Biografia",
        "Outros"
    ]
)
        submit = st.form_submit_button("Salvar Livro")
        
        if submit:
            if titulo.strip() and autor.strip():
               backend.adicionar_livro(
    titulo,
    autor,
    ano,
    categoria
)
                st.success(f"O livro '{titulo}' foi adicionado com sucesso!")
            else:
                st.warning("⚠️ Por favor, preencha os campos obrigatórios (Título e Autor).")

# ----------------- READ -----------------
elif menu == "📖 Visualizar Livros":
    st.subheader("Acervo Atual")

    busca = st.text_input("🔍 Buscar livro por título ou autor")

    if busca:
        livros = backend.buscar_livros(busca)
    else:
        livros = backend.listar_livros()
    
    if livros:
        # Transforma os dados em um DataFrame para uma tabela mais bonita
       df = pd.DataFrame(
    livros,
    columns=[
        "ID",
        "Título",
        "Autor",
        "Ano",
        "Categoria"
    ]
)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("A biblioteca está vazia no momento.")

# ----------------- UPDATE -----------------
elif menu == "✏️ Atualizar Livro":
    st.subheader("Atualizar Dados de um Livro")
    livros = backend.listar_livros()
    
    if livros:
        df = pd.DataFrame(livros, columns=["ID", "Título", "Autor", "Ano"])
        
        # Seleciona o livro pelo ID
        livro_id = st.selectbox("Selecione o ID do Livro que deseja alterar", df["ID"])
        
        st.write("Insira os novos dados abaixo:")
        with st.form(key="update_form"):
    novo_titulo = st.text_input("Novo Título")
    novo_autor = st.text_input("Novo Autor")
    novo_ano = st.number_input("Novo Ano", min_value=1000, max_value=2100, step=1)

    nova_categoria = st.selectbox(
        "Nova Categoria",
        [
            "Romance",
            "Fantasia",
            "Ficção Científica",
            "Tecnologia",
            "História",
            "Biografia",
            "Outros"
        ]
    )

    submit = st.form_submit_button("Atualizar Livro")
            
            if submit:
                if novo_titulo.strip() and novo_autor.strip():
                    backend.atualizar_livro(
    livro_id,
    novo_titulo,
    novo_autor,
    novo_ano,
    nova_categoria
)
                    st.success("Livro atualizado com sucesso!")
                else:
                    st.warning("⚠️ Por favor, preencha todos os campos para atualizar.")
    else:
        st.info("Não há livros cadastrados para atualizar.")

# ----------------- DELETE -----------------
elif menu == "❌ Deletar Livro":
    st.subheader("Remover Livro do Acervo")
    livros = backend.listar_livros()
    
    if livros:
        df = pd.DataFrame(livros, columns=["ID", "Título", "Autor", "Ano"])
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        livro_id = st.selectbox("Selecione o ID do Livro que deseja deletar", df["ID"])
        
        if st.button("Deletar Livro Permanente"):
            backend.deletar_livro(livro_id)
            st.error("Livro deletado do sistema.")
            st.rerun() # Atualiza a tela automaticamente
    else:
        st.info("Não há livros cadastrados para deletar.")
