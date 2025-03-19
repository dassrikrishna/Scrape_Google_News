import base64
import requests

# base64 encode image data
def encode_base64(url):
    return base64.b64encode(requests.get(url).content)

# decode image data
def decode_base64(encoded_string):
    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.decodebytes(encoded_string))