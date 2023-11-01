# IAdvogado 

## Aplicativo de Transformação de Texto em Petições Jurídicas

Este aplicativo foi desenvolvido com o propósito de facilitar a transformação de textos coloquiais em petições jurídicas utilizando a API da OpenAI. Ele utiliza Python com o framework Flask para a lógica do lado do servidor e páginas HTML e CSS para a interface do usuário.

## Funcionalidades

- **Conversão de Texto:** Aceita textos coloquiais como entrada e os transforma em linguagem jurídica adequada para petições.
- **Integração com a API da OpenAI:** Utiliza a API da OpenAI para processar os textos e gerar o conteúdo jurídico.
- **Interface Web Simples:** Páginas HTML e estilização com CSS para uma experiência de usuário amigável.

## Tecnologias Utilizadas

- **Python:** Utilizado para a lógica de servidor e integração com a API da OpenAI.
- **Flask:** Framework de Python para construção de aplicativos web.
- **HTML e CSS:** Páginas e estilização para a interface do usuário.

## Execução do Aplicativo

Para executar este aplicativo:

1. Certifique-se de ter Python instalado.
2. Instale as dependências do projeto listadas no arquivo `requirements.txt`.
3. Execute o servidor Flask com o comando `python app.py`.
4. Acesse a aplicação através do navegador no endereço `http://localhost:5000`.

Certifique-se de ter as chaves de API da OpenAI configuradas corretamente no aplicativo para o funcionamento adequado da integração.

## Estrutura de Diretórios

- **app.py:** Arquivo principal que inicia o servidor Flask.
- **templates/:** Diretório contendo os arquivos HTML para as páginas do aplicativo.
- **css/:** Diretório com arquivo CSS para a estilização.
