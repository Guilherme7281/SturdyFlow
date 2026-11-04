
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os


# ==========================================
# CONFIGURAÇÕES INICIAIS
# ==========================================

janela = tk.Tk()
janela.title("SturdyFlow - Organizador de Estudos")
janela.geometry("1000x650")
janela.minsize(850, 550)
janela.configure(bg="#F4F1FA")

COR_ROXA = "#6C4AB6"
COR_ROXA_ESCURO = "#50358F"
COR_FUNDO = "#F4F1FA"
COR_BRANCO = "#FFFFFF"
COR_TEXTO = "#29243A"
COR_CINZA = "#77717F"
COR_VERDE = "#3A9D72"

materias = []
tarefas = []
sessoes = []

ARQUIVO_DADOS = "dados.json"

# ==========================================
# ESTRUTURA PRINCIPAL
# ==========================================

menu_lateral = tk.Frame(
    janela,
    bg=COR_ROXA_ESCURO,
    width=220
)
menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

area_principal = tk.Frame(
    janela,
    bg=COR_FUNDO
)
area_principal.pack(
    side="right",
    fill="both",
    expand=True
)


# ==========================================
# FUNÇÕES GERAIS
# ==========================================

def limpar_tela():
    for widget in area_principal.winfo_children():
        widget.destroy()


def carregar_dados():
    global materias, tarefas, sessoes

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            materias = dados.get("materias", [])
            tarefas = dados.get("tarefas", [])
            sessoes = dados.get("sessoes", [])

        except (json.JSONDecodeError, OSError):
            messagebox.showwarning(
                "Atenção",
                "Não foi possível carregar os dados salvos."
            )


def salvar_dados():
    global materias, tarefas, sessoes

    
    dados = {
        "materias": materias,
        "tarefas": tarefas,
        "sessoes": sessoes
    }

    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    except OSError:
        messagebox.showerror(
            "Erro",
            "Não foi possível salvar os dados."
        )

    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            materias = dados.get("materias", [])
            tarefas = dados.get("tarefas", [])
            sessoes = dados.get("sessoes", [])

        except (json.JSONDecodeError, OSError):
            messagebox.showwarning(
                "Atenção",
                "Não foi possível carregar os dados salvos."
            )


def criar_titulo(texto, descricao=None):
    titulo = tk.Label(
        area_principal,
        text=texto,
        font=("Arial", 24, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    )
    titulo.pack(anchor="w", padx=35, pady=(30, 5))

    if descricao:
        subtitulo = tk.Label(
            area_principal,
            text=descricao,
            font=("Arial", 11),
            bg=COR_FUNDO,
            fg=COR_CINZA
        )
        subtitulo.pack(anchor="w", padx=35, pady=(0, 20))


def criar_botao(pai, texto, comando):
    return tk.Button(
        pai,
        text=texto,
        command=comando,
        font=("Arial", 10, "bold"),
        bg=COR_ROXA,
        fg=COR_BRANCO,
        activebackground=COR_ROXA_ESCURO,
        activeforeground=COR_BRANCO,
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=8
    )


# ==========================================
# DASHBOARD
# ==========================================

def mostrar_dashboard():
    limpar_tela()

    criar_titulo(
        "Dashboard",
        "Acompanhe sua organização e seu progresso nos estudos."
    )

    quadro_cartoes = tk.Frame(
        area_principal,
        bg=COR_FUNDO
    )
    quadro_cartoes.pack(fill="x", padx=25, pady=20)

    concluidas = sum(
        1 for tarefa in tarefas if tarefa["concluida"]
    )

    pendentes = sum(
        1 for tarefa in tarefas if not tarefa["concluida"]
    )

    dados = [
        ("Matérias", len(materias)),
        ("Tarefas pendentes", pendentes),
        ("Tarefas concluídas", concluidas),
        ("Sessões de estudo", len(sessoes))
    ]

    for i, (nome, quantidade) in enumerate(dados):
        cartao = tk.Frame(
            quadro_cartoes,
            bg=COR_BRANCO,
            padx=20,
            pady=20,
            highlightbackground="#E2DDEC",
            highlightthickness=1
        )
        cartao.grid(
            row=0,
            column=i,
            padx=8,
            sticky="nsew"
        )

        quadro_cartoes.grid_columnconfigure(
            i,
            weight=1
        )

        tk.Label(
            cartao,
            text=str(quantidade),
            font=("Arial", 26, "bold"),
            bg=COR_BRANCO,
            fg=COR_ROXA
        ).pack(anchor="w")

        tk.Label(
            cartao,
            text=nome,
            font=("Arial", 10),
            bg=COR_BRANCO,
            fg=COR_CINZA
        ).pack(anchor="w", pady=(5, 0))

    tk.Label(
        area_principal,
        text="Bem-vindo ao SturdyFlow!",
        font=("Arial", 17, "bold"),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w", padx=35, pady=(35, 10))

    tk.Label(
        area_principal,
        text="Organize suas matérias, acompanhe suas tarefas e registre suas sessões de estudo.",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_CINZA,
        wraplength=650,
        justify="left"
    ).pack(anchor="w", padx=35)


# ==========================================
# MATÉRIAS
# ==========================================

def mostrar_materias():
    limpar_tela()

    criar_titulo(
        "Minhas Matérias",
        "Cadastre e organize as matérias que você está estudando."
    )

    quadro = tk.Frame(area_principal, bg=COR_FUNDO)
    quadro.pack(fill="x", padx=35)

    tk.Label(
        quadro,
        text="Nome da matéria:",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    entrada_materia = tk.Entry(
        quadro,
        font=("Arial", 11),
        width=40
    )
    entrada_materia.pack(anchor="w", pady=8)

    lista = tk.Listbox(
        area_principal,
        font=("Arial", 11),
        height=12,
        width=65,
        selectbackground=COR_ROXA,
        selectforeground=COR_BRANCO
    )
    lista.pack(anchor="w", padx=35, pady=15)

    def atualizar_lista():
        lista.delete(0, tk.END)

        for materia in materias:
            lista.insert(tk.END, materia)

    def adicionar_materia():
        nome = entrada_materia.get().strip()

        if not nome:
            messagebox.showwarning(
                "Atenção",
                "Digite o nome da matéria."
            )
            return

        if any(m.lower() == nome.lower() for m in materias):
            messagebox.showwarning(
                "Atenção",
                "Essa matéria já está cadastrada."
            )
            return

        materias.append(nome)
        salvar_dados()
        entrada_materia.delete(0, tk.END)
        atualizar_lista()

        messagebox.showinfo(
            "Sucesso",
            "Matéria cadastrada!"
        )

    def remover_materia():
        selecao = lista.curselection()

        if not selecao:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma matéria para remover."
            )
            return

        nome = lista.get(selecao[0])

        possui_tarefas = any(
            tarefa["materia"] == nome for tarefa in tarefas
        )

        possui_sessoes = any(
            sessao["materia"] == nome for sessao in sessoes
        )

        if possui_tarefas or possui_sessoes:
            messagebox.showwarning(
                "Atenção",
                "Não é possível remover esta matéria porque ela possui tarefas ou sessões cadastradas."
            )
            return

        materias.remove(nome)
        atualizar_lista()

        messagebox.showinfo(
            "Sucesso",
            "Matéria removida!"
        )

    quadro_botoes = tk.Frame(
        area_principal,
        bg=COR_FUNDO
    )
    quadro_botoes.pack(anchor="w", padx=35)

    criar_botao(
        quadro_botoes,
        "Adicionar matéria",
        adicionar_materia
    ).pack(side="left", padx=(0, 10))

    criar_botao(
        quadro_botoes,
        "Remover selecionada",
        remover_materia
    ).pack(side="left")

    atualizar_lista()


# ==========================================
# TAREFAS
# ==========================================

def mostrar_tarefas():
    limpar_tela()

    criar_titulo(
        "Minhas Tarefas",
        "Cadastre atividades e acompanhe seus prazos."
    )

    quadro = tk.Frame(area_principal, bg=COR_FUNDO)
    quadro.pack(fill="x", padx=35)

    tk.Label(
        quadro,
        text="Nome da tarefa:",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    entrada_nome = tk.Entry(
        quadro,
        font=("Arial", 11),
        width=40
    )
    entrada_nome.pack(anchor="w", pady=5)

    tk.Label(
        quadro,
        text="Matéria:",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    materia_escolhida = tk.StringVar()

    seletor_materia = ttk.Combobox(
        quadro,
        textvariable=materia_escolhida,
        values=materias,
        state="readonly",
        width=37,
        font=("Arial", 10)
    )
    seletor_materia.pack(anchor="w", pady=5)

    tk.Label(
        quadro,
        text="Prazo (DD/MM/AAAA):",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    entrada_data = tk.Entry(
        quadro,
        font=("Arial", 11),
        width=40
    )
    entrada_data.pack(anchor="w", pady=5)

    lista = tk.Listbox(
        area_principal,
        font=("Arial", 10),
        height=10,
        width=85,
        selectbackground=COR_ROXA,
        selectforeground=COR_BRANCO
    )
    lista.pack(anchor="w", padx=35, pady=15)

    def atualizar_tarefas():
        lista.delete(0, tk.END)

        for tarefa in tarefas:
            status = (
                "Concluída"
                if tarefa["concluida"]
                else "Pendente"
            )

            texto = (
                f'{tarefa["nome"]} | '
                f'{tarefa["materia"]} | '
                f'Prazo: {tarefa["data"]} | '
                f'{status}'
            )

            lista.insert(tk.END, texto)

    def adicionar_tarefa():
        nome = entrada_nome.get().strip()
        materia = materia_escolhida.get()
        data = entrada_data.get().strip()

        if not nome or not materia or not data:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        if materia not in materias:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma matéria válida."
            )
            return

        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Digite uma data válida no formato DD/MM/AAAA."
            )
            return

        tarefas.append({
            "nome": nome,
            "materia": materia,
            "data": data,
            "concluida": False
        })


        salvar_dados()

        entrada_nome.delete(0, tk.END)
        entrada_data.delete(0, tk.END)

        atualizar_tarefas()

        messagebox.showinfo(
            "Sucesso",
            "Tarefa cadastrada!"
        )

    def concluir_tarefa():
        selecao = lista.curselection()

        if not selecao:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma tarefa."
            )
            return

        indice = selecao[0]

        if tarefas[indice]["concluida"]:
            messagebox.showinfo(
                "Informação",
                "Essa tarefa já está concluída."
            )
            return

        tarefas[indice]["concluida"] = True
        salvar_dados()
        atualizar_tarefas()

        messagebox.showinfo(
            "Sucesso",
            "Tarefa marcada como concluída!"
        )

    quadro_botoes = tk.Frame(
        area_principal,
        bg=COR_FUNDO
    )
    quadro_botoes.pack(anchor="w", padx=35)

    criar_botao(
        quadro_botoes,
        "Adicionar tarefa",
        adicionar_tarefa
    ).pack(side="left", padx=(0, 10))

    criar_botao(
        quadro_botoes,
        "Concluir tarefa",
        concluir_tarefa
    ).pack(side="left")

    atualizar_tarefas()


# ==========================================
# SESSÕES DE ESTUDO
# ==========================================

def mostrar_sessoes():
    limpar_tela()

    criar_titulo(
        "Sessões de Estudo",
        "Registre o tempo dedicado aos seus estudos."
    )

    quadro = tk.Frame(area_principal, bg=COR_FUNDO)
    quadro.pack(fill="x", padx=35)

    tk.Label(
        quadro,
        text="Matéria:",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    materia_escolhida = tk.StringVar()

    seletor_materia = ttk.Combobox(
        quadro,
        textvariable=materia_escolhida,
        values=materias,
        state="readonly",
        width=37,
        font=("Arial", 10)
    )
    seletor_materia.pack(anchor="w", pady=5)

    tk.Label(
        quadro,
        text="Data (DD/MM/AAAA):",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    entrada_data = tk.Entry(
        quadro,
        font=("Arial", 11),
        width=40
    )
    entrada_data.pack(anchor="w", pady=5)

    tk.Label(
        quadro,
        text="Duração em minutos:",
        font=("Arial", 11),
        bg=COR_FUNDO,
        fg=COR_TEXTO
    ).pack(anchor="w")

    entrada_duracao = tk.Entry(
        quadro,
        font=("Arial", 11),
        width=40
    )
    entrada_duracao.pack(anchor="w", pady=5)

    lista = tk.Listbox(
        area_principal,
        font=("Arial", 10),
        height=10,
        width=75,
        selectbackground=COR_ROXA,
        selectforeground=COR_BRANCO
    )
    lista.pack(anchor="w", padx=35, pady=15)

    def atualizar_sessoes():
        lista.delete(0, tk.END)

        for sessao in sessoes:
            texto = (
                f'{sessao["materia"]} | '
                f'Data: {sessao["data"]} | '
                f'Duração: {sessao["duracao"]} minutos'
            )

            lista.insert(tk.END, texto)

    def adicionar_sessao():
        materia = materia_escolhida.get()
        data = entrada_data.get().strip()
        duracao = entrada_duracao.get().strip()

        if not materia or not data or not duracao:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos."
            )
            return

        if materia not in materias:
            messagebox.showwarning(
                "Atenção",
                "Selecione uma matéria válida."
            )
            return

        try:
            datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Digite uma data válida no formato DD/MM/AAAA."
            )
            return

        try:
            minutos = int(duracao)

            if minutos <= 0:
                raise ValueError

        except ValueError:
            messagebox.showwarning(
                "Atenção",
                "Digite uma duração válida em minutos, maior que zero."
            )
            return

        sessoes.append({
            "materia": materia,
            "data": data,
            "duracao": minutos
        })

        salvar_dados()

        atualizar_sessoes()

        entrada_data.delete(0, tk.END)
        entrada_duracao.delete(0, tk.END)

        messagebox.showinfo(
            "Sucesso",
            "Sessão de estudo cadastrada!"
        )

    criar_botao(
        area_principal,
        "Adicionar sessão",
        adicionar_sessao
    ).pack(anchor="w", padx=35)

    atualizar_sessoes()


# ==========================================
# MENU LATERAL
# ==========================================

tk.Label(
    menu_lateral,
    text="SturdyFlow",
    font=("Arial", 21, "bold"),
    bg=COR_ROXA_ESCURO,
    fg=COR_BRANCO
).pack(pady=(35, 45))


def criar_botao_menu(texto, comando):
    botao = tk.Button(
        menu_lateral,
        text=texto,
        command=comando,
        font=("Arial", 12),
        bg=COR_ROXA_ESCURO,
        fg=COR_BRANCO,
        activebackground=COR_ROXA,
        activeforeground=COR_BRANCO,
        relief="flat",
        anchor="w",
        padx=25,
        pady=13,
        cursor="hand2"
    )

    botao.pack(fill="x", padx=10, pady=3)


criar_botao_menu(
    "Dashboard",
    mostrar_dashboard
)

criar_botao_menu(
    "Matérias",
    mostrar_materias
)

criar_botao_menu(
    "Tarefas",
    mostrar_tarefas
)

criar_botao_menu(
    "Sessões",
    mostrar_sessoes
)


# ==========================================
# INICIALIZAÇÃO
# ==========================================

carregar_dados()

mostrar_dashboard()

janela.mainloop()
