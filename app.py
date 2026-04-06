from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "videos"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
    <h2>Descargador de Videos</h2>
    <form action="/download" method="post">
        URL del video: <input type="text" name="url">
        <button type="submit">Descargar</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)