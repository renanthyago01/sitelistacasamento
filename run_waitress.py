from waitress import serve
from meu_site import app  # Certifique-se de que 'app' é o nome da sua variável Flask

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
