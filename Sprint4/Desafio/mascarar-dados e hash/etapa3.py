import hashlib

def gerar_hash_sha1():
    while True:
        entrada = input("Digite uma string para gerar o hash (ou 'exit' para sair): ")
        
        if entrada.lower() == 'exit':
            print("Encerrando o programa...")
            break
        
        # Gerar o hash SHA-1 da string
        hsh = hashlib.sha1(entrada.encode())
        
        # Imprimir o hash usando o método hexdigest
        print("Hash SHA-1:", hsh.hexdigest())

if __name__ == "__main__":
    gerar_hash_sha1()
