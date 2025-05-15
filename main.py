import streamlit as st

def tela_principal():
    st.title("Tabela de Contas")
    num_contas = st.number_input("Quantas contas (1-10)?", min_value=1, max_value=10, step=1)
    dados = []

    st.write("Preencha as quantidades para cada conta e item (níveis 10 a 19):")
    for conta in range(num_contas):
        cols = st.columns(10)
        linha = []
        for item in range(10, 20):
            valor = cols[item - 10].number_input(
                f"Conta {conta+1} - Nível {item}",
                min_value=0,
                value=0,
                key=f"{conta}_{item}"
            )
            linha.append(valor)
        dados.append(linha)

    if st.button("Somar Itens"):
        totais = {i: 0 for i in range(10, 21)}
        for linha in dados:
            for i, val in enumerate(linha):
                totais[10 + i] += val

        for lvl in range(10, 20):
            if totais[lvl] >= 2:
                totais[lvl + 1] += totais[lvl] // 2
                totais[lvl] = totais[lvl] % 2

        st.write("**Totais:**")
        for lvl in range(10, 21):
            st.write(f"Nível {lvl}: {totais[lvl]}")

# Executa o app
tela_principal()
