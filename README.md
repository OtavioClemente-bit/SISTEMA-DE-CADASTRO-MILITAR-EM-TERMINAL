# Sistema de Cadastro Militar (Terminal)

Este é um sistema de terminal desenvolvido em Python para cadastro, consulta, edição e exclusão de militares, com persistência em arquivo JSON.

## Funcionalidades
- Cadastro completo de militares (nome, CPF, IDT, PREC-CP, banco, conta, etc)
- Ordenação por posto/graduação
- Busca por nome (com ou sem acento)
- Edição de qualquer campo do militar
- Exclusão com confirmação
- Cadastro dinâmico de postos e bancos
- Dados salvos localmente em `militares.json`

## Tecnologias
- Python 3
- JSON para persistência
- Interface em terminal

## Como executar

1. Clone o repositório ou baixe os arquivos:
```bash
git clone https://github.com/SeuUsuario/sistema-cadastro-militar.git
cd sistema-cadastro-militar
```

2. Execute o programa:
```bash
python main.py
```

> O arquivo `militares.json` será criado automaticamente se não existir.

## Desenvolvido por
[Otavio Clemente](https://github.com/OtavioClemente-bit)
