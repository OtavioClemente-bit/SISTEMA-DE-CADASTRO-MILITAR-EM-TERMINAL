# main.py
# SISTEMA DE CADASTRO MILITAR EM TERMINAL
# Desenvolvido por: Otavio Clemente

import json, os, time, unicodedata

dados_arquivos = "militares.json"
militares = []
posto_graduação = ["Capitão", "1º Tenente", "2º Tenente", "Subtenente", "1º Sargento", "2º Sargento", "3º Sargento", "Cabo Efetivo Profissional", "Soldado Efetivo Profissional", "Soldado Efetivo Variável"]
bancos = ["001 - Banco do Brasil S.A", "341 - Itaú Unibanco S.A", "033 - Banco Santander (Brasil) S.A", "237 - Banco Bradesco S.A", "237 - Banco Santander (Brasil) S.A", "104 - Caixa Econômica Federal"]

def salvar_dados():
    with open(dados_arquivos, "w") as f:
        json.dump(militares, f, indent=4, ensure_ascii=False)

def carregar_dados():
    global militares
    try:
        with open(dados_arquivos, "r") as f:
            militares = json.load(f)
    except FileNotFoundError:
        pass

carregar_dados()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro_militares_posto_e_graduação():
    limpar_tela()
    incluir_PG = input("Digite o nome do POSTO/GRADUAÇÃO para incluir: ").capitalize()
    posto_graduação.append(incluir_PG)
    salvar_dados()
    return posto_graduação

def prioridade_posto(posto):
    try:
        return posto_graduação.index(posto)
    except ValueError:
        return len(posto_graduação) 

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()
    
def cadastrar_incluir_bancos():
    limpar_tela()
    incluir_bancos = input("Digite o nome do BANCO para incluir: ").capitalize()
    bancos.append(incluir_bancos)
    salvar_dados()

def cadastro_militares_CPF():
    while True:
        limpar_tela()
        cpf = input("Digite o CPF (somente número): ")
        if cpf.isdigit() and len(cpf) == 11:
            formato_cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"CPF - {formato_cpf} - cadastrador.")
            salvar_dados()
            return formato_cpf
        else:
            limpar_tela()
            print("CPF inválido.")
            time.sleep(1)

def cadastro_militares_PREC():
    while True:
        prec = input("Digite o PREC-CP (somente número): ")
        if prec.isdigit() and len(prec) == 9:
            formato_prec= f"{prec[:2]} {prec[2:9]}"
            print(f"PREC-CP - {formato_prec} - cadastrador.")
            salvar_dados()
            return formato_prec
        else:
            limpar_tela()
            print("PREC-CP inválido.")
            time.sleep(1)

def cadastro_militares_IDT():
    while True:
        IDT = input("Digite o IDT MILITAR (somente número): ")
        if IDT.isdigit() and len(IDT) == 10:
            formato_IDT= f"{IDT[:3]}.{IDT[3:6]}.{IDT[6:9]}-{IDT[9:]}"
            print(f"IDT MILITAR - {formato_IDT} - cadastrador.")
            salvar_dados()
            return formato_IDT
        else:
            limpar_tela()
            print("IDT MILITAR inválido.")
            time.sleep(1)

def cadastrar_banco_escolha():
    while True:
        limpar_tela()
        for i, banco in enumerate(bancos, start=1):
            print(f"{i} - {banco}")
        try:
            escolha_banco = int(input("\nEscolha o Posto/Graduação: "))
            if 1 <= escolha_banco <= len(bancos):
                escolha_bk = bancos[escolha_banco - 1]
                salvar_dados()
                return escolha_bk
            else:
                limpar_tela()
                print("Entrada inválida.")
                time.sleep(1)   
        except ValueError:
            limpar_tela()
            print("Entrada inválida.")
            time.sleep(1)  

def cadastrar_dados_bancarios():
    while True:
        limpar_tela()
        agencia_incluir = input("Digite a agência bancaria: ")
        if agencia_incluir.isdigit():
            print(f"AG {agencia_incluir} cadastrada com sucesso.")
            salvar_dados()
        else:
            limpar_tela()
            print("Agencia incorreta.")
            time.sleep(1)
        limpar_tela()
        conta_corrente = input("Digite o número da conta: ")
        if conta_corrente.isdigit():
            print(f"Conta {conta_corrente} cadastrada com sucesso.")
            salvar_dados()
            return agencia_incluir, conta_corrente
        else:
            limpar_tela()
            print("Conta incorreta.")
            time.sleep(1)

def cadastrar_militar_posto_graduaçao():
    while True:
        limpar_tela()
        for i, PG in enumerate(posto_graduação, start=1):
            print(f"{i} - {PG}")
        try:
            escolha_PG = int(input("\nEscolha o Posto/Graduação: "))
            if 1 <= escolha_PG <= len(posto_graduação):
                escolha_posto_graduaçao = posto_graduação[escolha_PG - 1]
                salvar_dados()
                return escolha_posto_graduaçao
            else:
                limpar_tela()
                print("Entrada inválida.")
                time.sleep(1)
        except ValueError:
            limpar_tela()
            print("Entrada inválida.")
            time.sleep(1)

def cadastrar_militar():
    while True:
        limpar_tela()
        nome_completo = input("Digite o nome completo: ").title()
        if nome_completo.replace(" ","").isalpha() and not any(nome_completo == m['nome completo'] for m in militares):
            nome_guerra = input("Digite o nome de guerra: ").capitalize()
            if nome_guerra.isalpha() and nome_guerra in nome_completo:
                print(f"{nome_guerra} cadastrado com sucesso.")
                salvar_dados()
                return nome_completo, nome_guerra
            else:
                limpar_tela()
                print("Nome de guerra incorreto.")
                time.sleep(1)
        else:
            limpar_tela()
            print("Nome incorreto.")
            time.sleep(1)

def listar_militares():
    limpar_tela()
    for i, nome in enumerate(sorted(militares, key=lambda x: prioridade_posto(x['PG'])), start=1):
        print(f"{i}: {nome['PG']} - {nome['nome completo']}")
    input()

def pesquisar_militar():
    limpar_tela()
    resultados = []
    nome_pesquisa = remover_acentos(input("Digite o nome para procurar: ").strip())
    for nome in sorted(militares, key=lambda x: prioridade_posto(x['PG'])):
        nome_normal = remover_acentos(nome['nome completo']).strip()
        if nome_pesquisa in nome_normal:
            resultados.append(nome)
    if not resultados:
        print("\nNenhum militar encontrado.")
        input("\nPressione qualquer tecla para retornar ...")
        return
    print("\n=== RESULTADOS ENCONTRADOS ===")
    for i, militar in enumerate(resultados, start=1):
        print(f"{i}. {militar['PG']} - {militar['nome completo']} ({militar['nome de guerra']})")
    try:
        escolha = int(input("\nDigite o número do militar para ver os detalhes: "))
        if 1 <= escolha <= len(resultados):
            militar = resultados[escolha - 1]
            limpar_tela()
            print(f"Posto e Graduação: {militar['PG']}")
            print(f"Nome completo: {militar['nome completo']}")
            print(f"CPF: {militar['cpf']}")
            print(f"PREC-CP: {militar['prec']}")
            print(f"Identidade militar: {militar['idt']}")
            print(f"Banco: {militar['banco']}")
            print(f"Agência: {militar['AGENCIA']}")
            print(f"Conta Corrente: {militar['CC']}")
        else:
            print("\nNúmero inválido.")
    except ValueError:
        print("\nEntrada inválida.")

    input("\nPressione qualquer tecla para retornar ...")

def editar_militar():
    limpar_tela()
    resultados = []
    nome_pesquisa = remover_acentos(input("Digite o nome para procurar: ").strip())
    for nome in sorted(militares, key=lambda x: prioridade_posto(x['PG'])):
        nome_normal = remover_acentos(nome['nome completo']).strip()
        if nome_pesquisa in nome_normal:
            resultados.append(nome)
    if not resultados:
        print("\nNenhum militar encontrado.")
        input("\nPressione qualquer tecla para retornar ...")
        return
    print("\n=== RESULTADOS ENCONTRADOS ===")
    for i, militar in enumerate(resultados, start=1):
        print(f"{i}. {militar['PG']} - {militar['nome completo']} ({militar['nome de guerra']})")
    try:
        escolha = int(input("\nDigite o número do militar para ver os detalhes: "))
        if 1 <= escolha <= len(resultados):
            militar = resultados[escolha - 1]
            limpar_tela()
            campos = {
                1: "PG",
                2: "nome completo",
                3: "nome de guerra",
                4: "cpf",
                5: "prec",
                6: "idt",
                7: "banco",
                8: "AGENCIA",
                9: "CC"
            }
            for k, v in campos.items():
                print(f"{k} - {v.title()}: {militar[v]}")
            escolha_editar = int(input("\nDigite o número do campo que deseja editar: "))
            if escolha_editar in campos:
                chave = campos[escolha_editar]
                if chave == "PG":
                    novo_valor = cadastrar_militar_posto_graduaçao()
                elif chave == "cpf":
                    novo_valor = cadastro_militares_CPF()
                elif chave == "prec":
                    novo_valor = cadastro_militares_PREC()
                elif chave == "idt":
                    novo_valor = cadastro_militares_IDT()
                elif chave == "banco":
                    novo_valor = cadastrar_banco_escolha()
                elif chave == "AGENCIA" or chave == "CC":
                    cadastrar_dados_bancarios()
                else:
                    novo_valor = input(f"Digite o novo valor para {chave.title()}: ").strip().title()
                militar[chave] = novo_valor
                salvar_dados()
                print("\nDado atualizado com sucesso!")
            else:
                limpar_tela()
                print("\nEntrada inválida.")
                time.sleep(1)
        else:
            limpar_tela()
            print("\nNúmero inválido.")
            time.sleep(1)
    except ValueError:
        limpar_tela()
        print("\nEntrada inválida.")
        time.sleep(1)

    input("\nPressione qualquer tecla para retornar ...")

def excluir_cadastro_militar():
    limpar_tela()
    resultados = []
    nome_pesquisa = remover_acentos(input("Digite o nome para procurar: ").strip())
    for nome in sorted(militares, key=lambda x: prioridade_posto(x['PG'])):
        nome_normal = remover_acentos(nome['nome completo']).strip()
        if nome_pesquisa in nome_normal:
            resultados.append(nome)
    if not resultados:
        print("\nNenhum militar encontrado.")
        input("\nPressione qualquer tecla para retornar ...")
        return
    print("\n=== RESULTADOS ENCONTRADOS ===")
    for i, militar in enumerate(resultados, start=1):
        print(f"{i}. {militar['PG']} - {militar['nome completo']} ({militar['nome de guerra']})")
    try:
        escolha = int(input("\nDigite o número do militar para ver os detalhes: "))
        if 1 <= escolha <= len(resultados):
            militar = resultados[escolha - 1]
            confirmar = input(f"\nTem certeza que deseja excluir {militar['nome completo']}? (s/n): ").lower()
            if confirmar == "s":
                militares.remove(militar)
                salvar_dados()
                print("\nMilitar excluído com sucesso!")
            else:
                limpar_tela()
                print("\nExclusão cancelada.")
                time.sleep(1)
        else:
            limpar_tela()
            print("\nNúmero inválido.")
            time.sleep(1)
    except ValueError:
        limpar_tela()
        print("\nEntrada inválida.")
        time.sleep(1)

    input("\nPressione qualquer tecla para retornar ...")

def menu_cadastros():
    while True:
        limpar_tela()
        print("\n=== CADASTROS DADOS ===")
        print("1. Cadastrar posto e graduação.")
        print("2. Cadastrar bancos")
        print("3. Sair.")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastro_militares_posto_e_graduação()
        elif opcao == "2":
            cadastrar_incluir_bancos()
        elif opcao == "3":
            break
        else:
            limpar_tela()
            print("Opção inválida.")
            time.sleep(1)

def menu_principal():
    while True:
        limpar_tela()
        print("=== SISTEMA DE CADASTRO MILITAR ===\n")
        print("1. Cadastrar militar")
        print("2. Listar militares")
        print("3. Pesquisar.")
        print("4. Editar militar.")
        print("5. Cadastro de dados.")
        print("6. Excluir militar.")
        print("7. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            escolha_posto_graduaçao = cadastrar_militar_posto_graduaçao()
            nome_completo, nome_guerra = cadastrar_militar()
            formato_cpf = cadastro_militares_CPF()
            formato_prec = cadastro_militares_PREC()
            formato_IDT = cadastro_militares_IDT()
            escolha_bk = cadastrar_banco_escolha()
            conta_corrente, agencia_incluir = cadastrar_dados_bancarios()
            militar_cadastrado = {"PG": escolha_posto_graduaçao, "nome completo": nome_completo, "nome de guerra": nome_guerra, "cpf": formato_cpf, "prec": formato_prec, "idt": formato_IDT, "banco": escolha_bk ,"CC": conta_corrente, "AGENCIA": agencia_incluir}
            militares.append(militar_cadastrado)
            salvar_dados()
        elif opcao == "2":
            listar_militares()
        elif opcao == "3":
            pesquisar_militar()
        elif opcao == "4":
            editar_militar()
        elif opcao == "5":
            menu_cadastros()
        elif opcao == "6":
            excluir_cadastro_militar()
        elif opcao == "7":
            salvar_dados()
            limpar_tela()
            print("Saindo... até mais!")
            break
        else:
            limpar_tela()
            print("Opção inválida.")
            time.sleep(1)

militar_cadastrado = menu_principal()
