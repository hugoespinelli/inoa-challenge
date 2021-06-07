## Desafio Inoa

Para iniciar o projeto, você precisará do ``docker`` instalado em sua máquina local.
Na pasta raiz do seu projeto, execute:

    docker-compose --env-file ./.env up

Isso inicializará o projeto com suas devidas dependencias.
Seu projeto poderá ser acessado em

    http://localhost


### Primeiro carregamento
Você precisará ativar a migração para construir as tabelas necessárias ao projeto.
Entre na pasta ``back`` e execute:
    python manage.py migrate


### Inicialize as variáveis locais
Na pasta raiz, crie um arquivo ``.env`` com as variáveis de ambiente requeridas ao projeto.
Siga o ``.env.example`` para preenche-lo corretamente.



