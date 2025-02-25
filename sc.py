import requests

def check_urls(input_file, output_file):
    with open(input_file, 'r') as file:
        urls = file.readlines()

    with open(output_file, 'w') as output:
        for url in urls:
            url = url.strip()  # Supprime les espaces ou les nouvelles lignes
            try:
                # Envoie une requête HEAD pour ne pas télécharger tout le contenu
                response = requests.head(url)
                if response.status_code == 200:
                    output.write(f"{url}\n")  # Enregistre uniquement l'URL
                    print(f"{url} - Status Code: 200 (saved)")  # Optionnel, si vous voulez afficher dans le terminal
            except requests.RequestException as e:
                print(f"Error with {url}: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to the file containing the links: ")
    output_file = input("Enter the name of the output file for 200 status codes: ")
    check_urls(input_file, output_file)
