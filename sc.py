import subprocess

def get_status_code(url):
    # Utilisation de subprocess pour exécuter la commande curl et récupérer le code de statut
    result = subprocess.run(
        ['curl', '-I', '-s', url],  # -I : pour les en-têtes, -s : pour silence
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    
    # Extraire le code de statut HTTP à partir de la réponse
    for line in result.stdout.decode().splitlines():
        if line.startswith('HTTP/'):
            # Récupère et retourne le code de statut HTTP
            return line.split()[1]

def check_urls_from_file(file_path, output_file):
    # Ouvre le fichier contenant les liens
    with open(file_path, 'r') as file:
        # Lire chaque ligne du fichier et récupérer l'URL
        urls = file.readlines()
    
    with open(output_file, 'w') as output:
        for url in urls:
            url = url.strip()  # Enlever les espaces ou sauts de ligne inutiles
            if url:
                status_code = get_status_code(url)
                if status_code == "200":
                    # Écrire l'URL dans le fichier si le statut est 200
                    output.write(f'{url} - Status Code: {status_code}\n')
                    print(f'{url} - Status Code: {status_code} (saved)')

def main():
    # Demande à l'utilisateur de fournir le chemin du fichier et du fichier de sortie
    file_path = input("Entrez le chemin du fichier contenant les liens : ")
    output_file = input("Entrez le nom du fichier de sortie pour les codes 200 : ")
    check_urls_from_file(file_path, output_file)

if __name__ == '__main__':
    main()
