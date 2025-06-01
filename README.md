
-----

#  API de Streaming e Busca do YouTube

Uma API simples desenvolvida com Flask para buscar e reproduzir v�deos do YouTube em formato de �udio.

##  Instala��o

1. **Clone o reposit�rio:**

   ```bash
   git clone https://github.com/El-SpaceX/youtube-stream-api.git
   cd youtube-stream-api
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as depend�ncias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplica��o:**

   ```bash
   flask run
   ```

   A aplica��o estar� dispon�vel em `http://localhost:5000`.

## Endpoints

### `/play`

Reproduz o �udio de um v�deo do YouTube a partir de uma URL fornecida.

* **M�todo:** `GET`
* **Par�metros de Consulta:**

  * `url` (obrigat�rio): URL do v�deo do YouTube.

**Exemplo de Requisi��o:**

```http
GET /play?url=https://www.youtube.com/watch?v=abc123
```

**Resposta:**

* Retorna o �udio do v�deo em formato `audio/mpeg`.

### `/search`

Realiza uma busca por v�deos no YouTube com base em uma query.

* **M�todo:** `GET`
* **Par�metros de Consulta:**

  * `query` (obrigat�rio): Termo de busca.
  * `max_result` (opcional): N�mero m�ximo de resultados a serem retornados (padr�o: 5).

**Exemplo de Requisi��o:**

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

Combina a funcionalidade de busca e reprodu��o. Realiza uma busca no YouTube e reproduz o �udio do primeiro v�deo encontrado.

* **M�todo:** `GET`
* **Par�metros de Consulta:**

  * `query` (obrigat�rio): Termo de busca.

**Exemplo de Requisi��o:**

```http
GET /search-and-play?query=lofi+hip+hop
```

**Resposta:**

* Retorna o �udio do primeiro v�deo encontrado em formato `audio/mpeg`.

## Tecnologias Utilizadas

* [Flask](https://flask.palletsprojects.com/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)

## Licen�a

Este projeto est� licenciado sob a [MIT License](LICENSE).

---