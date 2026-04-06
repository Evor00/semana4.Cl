from flask import Flask, request, send_file, render_template_string
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "videos"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Descargador de Videos</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: white;
            text-align: center;
            padding: 50px;
        }

        .container {
            background: rgba(0,0,0,0.4);
            padding: 30px;
            border-radius: 15px;
            width: 400px;
            margin: auto;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        }

        h1 {
            margin-bottom: 20px;
        }

        input {
            width: 90%;
            padding: 10px;
            border-radius: 10px;
            border: none;
            margin-bottom: 15px;
        }

        button {
            background: #00c9a7;
            border: none;
            padding: 10px 20px;
            color: white;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
        }

        button:hover {
            background: #00a78e;
        }

        .error {
            margin-top: 15px;
            color: #ff6b6b;
        }

        .footer {
            margin-top: 20px;
            font-size: 12px;
            opacity: 0.7;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>📥 Video Downloader</h1>

    <form action="/download" method="post">
        <input type="text" name="url" placeholder="Pega aquí el link del video..." required>
        <br>
        <button type="submit">Descargar</button>
    </form>

    {% if error %}
        <div class="error">
            <strong>Error:</strong> {{ error }}
        </div>
    {% endif %}

    <div class="footer">
        Soporta YouTube, TikTok, Instagram, Facebook
    </div>
</div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return send_file(filename, as_attachment=True)

    except Exception as e:
        return render_template_string(HTML, error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)