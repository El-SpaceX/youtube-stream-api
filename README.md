
-----

#  API de Streaming e Busca do YouTube

Uma API simples desenvolvida com Flask para buscar e reproduzir vídeos do YouTube em formato de áudio.

##  Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/El-SpaceX/youtube-stream-api.git
   cd youtube-stream-api
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://localhost:5000`.

## Endpoints

### `/play`

Reproduz o áudio de um vídeo do YouTube a partir de uma URL fornecida.

* **Método:** `GET`
* **Parâmetros de Consulta:**

  * `url` (obrigatório): URL do vídeo do YouTube.

**Exemplo de Requisição:**

```http
GET /play?url=https://www.youtube.com/watch?v=abc123
```

**Resposta:**

* Retorna o áudio do vídeo em formato `audio/mpeg`.

### `/search`

Realiza uma busca por vídeos no YouTube com base em uma query.

* **Método:** `GET`
* **Parâmetros de Consulta:**

  * `query` (obrigatório): Termo de busca.
  * `max_result` (opcional): Número máximo de resultados a serem retornados (padrão: 5).

**Exemplo de Requisição:**

```http
GET /search?query=lofi+hip+hop&max_result=3
```

**Resposta:**

```json
[
  {
    "title": "Lofi Hip Hop Mix",
    "url": "https://www.youtube.com/watch?v=xyz456",
    "duration": "1:00:00"
  },
  {
    "title": "Chill Beats to Relax",
    "url": "https://www.youtube.com/watch?v=def789",
    "duration": "2:00:00"
  },
  {
    "title": "Study Music",
    "url": "https://www.youtube.com/watch?v=ghi012",
    "duration": "1:30:00"
  }
]
```

### `/search-and-play`

Combina a funcionalidade de busca e reprodução. Realiza uma busca no YouTube e reproduz o áudio do primeiro vídeo encontrado.

* **Método:** `GET`
* **Parâmetros de Consulta:**

  * `query` (obrigatório): Termo de busca.

**Exemplo de Requisição:**

```http
GET /search-and-play?query=lofi+hip+hop
```

**Resposta:**

* Retorna o áudio do primeiro vídeo encontrado em formato `audio/mpeg`.

## Tecnologias Utilizadas

* [Flask](https://flask.palletsprojects.com/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---