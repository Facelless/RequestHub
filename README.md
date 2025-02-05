# 🌍 Servidor de API Simples em Python

Este é um script leve em Python que utiliza `http.server` para roteamento e `urllib` para lidar com requisições. Ele permite a criação de APIs básicas e é perfeito para testes locais e aprendizado sobre servidores web.

## 📌 Recursos

- 🚀 **Roteamento Simples** – Manipule vários endpoints com facilidade.
- 🌐 **Leve** – Nenhuma dependência externa necessária.
- 🛠️ **Fácil de Expandir** – Modifique e expanda funcionalidades rapidamente.
- 🔄 **Testes Locais** – Ideal para prototipagem rápida de APIs.

## 🛠 Instalação e Uso

### 🔹 Requisitos

- 🐍 **Python 3.6+**

### 🚀 Executando o Servidor

Clone o repositório e execute o script:

```bash
git clone https://github.com/Facelless/RequestHub.git
cd SimplePythonAPIServer
python server.py
```

### 📝 Exemplo de Requisição

```bash
curl http://localhost:8000/api/example
```

## 📖 Como Funciona

- O script usa `http.server` para escutar requisições recebidas.
- Os endpoints são definidos no próprio script para manipular diferentes requisições.
- `urllib` processa os parâmetros da requisição e gera respostas.


Aproveite para construir sua API simples! 🚀

