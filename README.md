# BruteForce_Http

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Uma ferramenta de força bruta para autenticação HTTP, desenvolvida em Python. Este projeto permite testar combinações de usuários e senhas em formulários de login HTTP.

## Funcionalidades

- **Força Bruta Automatizada**: Realiza tentativas automáticas de login utilizando listas de usuários e senhas.
- **Suporte a Formulários com CSRF Token**: Detecta e lida com tokens CSRF presentes nos formulários de login.
- **Execução Multithread**: Utiliza múltiplas threads para acelerar o processo de brute force.
- **Personalização**: Permite o uso de listas personalizadas de usuários e senhas.

## Instalação

### Requisitos

- Python 3.x
- Bibliotecas:
  - `requests`
  - `colorama`

### Passos para Instalação

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/LightProgrammer000/BruteForce_Http.git
   cd BruteForce_Http
