# IAdvogado 

## Aplicativo de Transformação de Texto em Petições Jurídicas

Este aplicativo foi desenvolvido com o propósito de facilitar a transformação de textos coloquiais em petições jurídicas utilizando a API da OpenAI. Ele utiliza Python com o framework Flask para a lógica do lado do servidor e páginas HTML e CSS para a interface do usuário.

![image](https://i.imgur.com/UqQIeVW.png)
![video](https://i.imgur.com/8VlZ66G.mp4)

## Integrantes

### Gabriel Menezes Cabral
- **Matrícula:** 119110372

### Paulo Henrique Ribeiro Medeiros Cruz
- **Matrícula:** 118210460

## Funcionalidades

- **Conversão de Texto:** Aceita textos coloquiais como entrada e os transforma em linguagem jurídica adequada para petições.
- **Integração com a API da OpenAI:** Utiliza a API da OpenAI para processar os textos e gerar o conteúdo jurídico.
- **Interface Web Simples:** Páginas HTML e estilização com CSS para uma experiência de usuário amigável.

## Tecnologias Utilizadas

- **Python:** Utilizado para a lógica de servidor e integração com a API da OpenAI.
- **Flask:** Framework de Python para construção de aplicativos web.
- **HTML e CSS:** Páginas e estilização para a interface do usuário.

## Explicação do Código

Neste projeto, O foi feita uma API em python utilizando Flask, que por sua vez utiliza a API da OpenAI para criar petições jurídicas a partir de um texto fornecido. Ele carrega chaves de API e utiliza funções para enviar um texto base à API da OpenAI, que gera uma petição jurídica com base nesse texto. Depois, com esse texto como resposta, é gerado um arquivo .docx, ou seja Word, com as informações do documento. E fica disponível para dowload.

## Execução do Aplicativo

Para executar este aplicativo:

1. Certifique-se de ter Python instalado.
2. Instale as dependências do projeto com o comando `pip install -r requirements.txt`.
3. Crie um arquivo .env e adicione a  uma variável de ambiente com a sua chave da OpenAI `OPENAI_API_KEY=sua_chave_aqui`.
4. Execute o servidor Flask com o comando `python app.py`.
5. Acesse a aplicação através do navegador no endereço.

Certifique-se de ter as chaves de API da OpenAI configuradas corretamente no aplicativo para o funcionamento adequado da integração.

## Estrutura de Diretórios

- **app.py:** Arquivo principal que inicia o servidor Flask.
- **templates/:** Diretório contendo os arquivos HTML para as páginas do aplicativo.
- **css/:** Diretório com arquivo CSS para a estilização.
