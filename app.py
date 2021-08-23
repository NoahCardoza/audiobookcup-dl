import traceback
from base64 import b64decode
from os import environ

import requests
from flask import Flask, Response, jsonify
from flask_cors import CORS
from requests.sessions import session

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


proxies = {
    'https': environ['HTTPS_PROXY']
} if 'HTTPS_PROXY' in environ else None

@app.route('/<path:audiobook_page_url>', )
def catch_all(audiobook_page_url):
    try:
        if '://www.audiobookcup.com/' not in audiobook_page_url:
            return jsonify({
                'message': 'Invalid Audiobook Cup URL'
            }), 400

        s = requests.Session()
        s.headers.update({
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
        })

        audiobook_page_res = s.get(audiobook_page_url, proxies=proxies)
        
        html = audiobook_page_res.text
        
        book_title = html.split('<title>')[1].split('</title>')[0]
        
        encrypted_url = html.split('encrypt:')[1].split("',")[0]
        decoded_url = b64decode(encrypted_url).decode()

        audiobook_file_res = s.get(decoded_url, headers={
            'referer': 'https://www.audiobookcup.com/'
        }, stream=True)

        file_postfix = decoded_url.rsplit('.', maxsplit=1)[1]
        
        def generate():
            for chunk in audiobook_file_res.iter_content(chunk_size=1024): 
                    if chunk:
                        yield chunk
        
        return Response(generate(), headers={
            'x-filename': f'{book_title}.{file_postfix}',
            'Content-Length': audiobook_file_res.headers['Content-Length'],
            'Access-Control-Expose-Headers': 'x-filename'
        }, mimetype=audiobook_file_res.headers['content-type'])
    except Exception:
        traceback.print_exc()
        return jsonify({
            'message': 'An unknown error has occured. Contact MacHacker#8396 on Discord.'
        }), 500

if __name__ == "__main__":
    app.run(debug=True)

