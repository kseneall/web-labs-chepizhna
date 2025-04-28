from flask import Flask
import ssl
import generate_cert

app = Flask(__name__)

@app.route("/api/message")
def get_message():
    return "Це захищений запит через TLS 1.2! Chepizhna Oksana"

if __name__ == "__main__":
    generate_cert.generate_cert()

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("cert.pem", "key.pem")


    context.set_ciphers('RSA')


    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_2

    app.run(host="0.0.0.0", port=8443, ssl_context=context)
