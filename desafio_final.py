import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='GaliBank',layout='centered')

#CRIANDO CLASSE CONTA, CLASSE CONTACORRENTE, CLASSE CONTAESTUDANTE
class Conta:
    def __init__ (self, titular: str, saldo: float = 0.0):
        self.titular = " ".join([p.capitalize() for p in titular.strip().split()])
        self.saldo = float(saldo)
        self.historico = [] #lista de transações

    def descricao(self):
        return f'Conta do titular {self.titular} - Saldo em R$: {self.saldo:.2f}'
    
    def depositar (self, valor):
        try:
            v = float(valor)
            if v <= 0:
                raise ValueError("ERRO - Valor deve ser positivo!")
        except Exception as e:
            raise

        self.saldo += v
        self.historico.append({"Tipo" : "Depósito", "Valor" : v, "Data" : datetime.now()})

    def sacar (self, valor):
        try:
            v = float(valor)
            if v <= 0:
                raise ValueError("ERRO - Valor deve ser positivo!")
        except Exception:
            raise

        #CONFIGURANDO A TAXA DE 1.50
        taxa = self.taxa_operacao()
        total_debito = v + taxa
        if total_debito >= self.saldo:
            raise ValueError("ERRO - Saldo insufieciente na conta!")
        self.saldo -= total_debito
        self.historico.append({"Tipo" : "Saque", "Valor" : total_debito, "Data" : datetime.now()})

    def taxa_operacao(self):
        return 1.50
    
    def extrato_df(self):
        #RETORNAR UM DF DO HISTÓRICO DE OPERAÇÕES
        if not self.historico:
            return pd.DataFrame(columns=["Tipo", "Valor", "Taxa", "Data"])
        df = pd.DataFrame(self.historico)
        return df
    
class ContaCorrente(Conta):
    def descricao (self):
        return f'Conta Corrente {self.titular} - Saldo em R$: {self.saldo:.2f}'
    
class ContaEstudante(Conta):
    def descricao (self):
        return f'Conta Estudante {self.titular} - Saldo em R$: {self.saldo:.2f}'
    
    def taxa_operacao(self):
        return 0.0 #estudante não paga taxa de saque

#CONFIGURANDO INTERFACE COM STREAMLIT
if "conta" not in st.session_state:
    st.session_state.conta = None

st.title("GALIBANK - SEJA MUITO BEM-VINDO!")

nome = st.text_input("Nome do titular: ")
tipo_conta = st.radio("Tipo de Conta", ["Corrente", "Estudante"])
saldo_inicial = st.text_input("Saldo Inicial: ")

if st.button("Criar Conta"):
    try:
        saldo_val = float(saldo_inicial) if saldo_inicial.strip() else 0.0
    except Exception:
        st.error("Saldo Inicial deve ser um número!")
    else:
        if tipo_conta == "Corrente":
            st.session_state.conta = ContaCorrente(nome, saldo_val)
        else:
            st.session_state.conta = ContaEstudante(nome, saldo_val)
        st.success("Conta criada com sucesso!")

if st.session_state.conta:
    conta = st.session_state.conta
    st.subheader(conta.descricao())

    col1, col2 = st.columns(2)

    with col1:
        valor_deposito = st.text_input("Valor Depositado")
        if st.button("Depositar"):
            try:
                conta.depositar(valor_deposito)
                st.success(f"Depósito de {float(valor_deposito):.2f} foi realizado com sucesso!")
            except Exception as e:
                st.error(f"Erro - {e}")
    
    with col2:
        valor_saque = st.text_input("Valor Sacado")
        if st.button("Sacar"):
            try:
                conta.sacar(valor_saque)
                st.success(f"Saque de {float(valor_saque):.2f} foi realizado com sucesso!")
            except Exception as e:
                st.error(f"Erro - {e}")

    #CONFIGURAÇÃO DO EXTRATO UTILIZANDO A BIBLIOTECA PANDAS
    st.header("HISTÓRICO DE TRANSAÇÕES")
    df_extrato = conta.extrato_df()
    if not df_extrato.empty:
        #formatar as colunas e datas
        df_extrato = df_extrato.copy()
        df_extrato['Data'] = df_extrato['Data'].dt.strftime("%Y-%m-%d %H:%M:%S")
        st.dataframe(df_extrato)
    else:
        st.info("NENHUMA MOVIMENTAÇÃO FOI REGISTRADA AINDA!")
    
    st.markdown(f"O saldo atual: {conta.saldo:.2f}")

    if st.button("RESETAR CONTA (APAGAR HISTÓRICO)"):
        st.session_state.conta = None
        st.success("AS INFOS FORAM APAGADAS")

else:
    st.info(f"CRIE UMA CONTA PARA COMEÇAR!")


