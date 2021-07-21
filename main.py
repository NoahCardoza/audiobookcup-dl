import sys
import shutil

from urllib.request import Request, urlopen
from urllib.parse import urlparse
from base64 import b64decode
from os import path


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
url = sys.argv[1]

print('Fetching audio book information...')

req = Request(url)
req.add_header('user-agent', user_agent)
res = urlopen(req)

html = res.read()

print('Decoding download link...')

encrypted_url = html.split(b'encrypt:')[1].split(b"',")[0]
decoded_url = b64decode(encrypted_url).decode()
parsed_url = urlparse(decoded_url)


req = Request(decoded_url)
req.add_header('user-agent', user_agent)
req.add_header('referer', 'https://www.audiobookcup.com/')

output_path = path.join('.', path.basename(parsed_url.path))

print('Starting download...')

with urlopen(req) as in_stream, open(output_path, 'wb') as out_file:
    shutil.copyfileobj(in_stream, out_file)

print('Success! File saved to', output_path)