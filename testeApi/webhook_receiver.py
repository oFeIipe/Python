from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

# O segredo compartilhado para verificar a assinatura do webhook
WEBHOOK_SECRET = 'meu_segredo'  # Substitua isso pelo segredo gerado no GitHub

def verify_signature(payload, signature):
    # Calcula a assinatura HMAC SHA1
    hash_digest = hmac.new(WEBHOOK_SECRET.encode(), payload, hashlib.sha1).hexdigest()
    # Compara a assinatura calculada com a recebida do GitHub
    return hmac.compare_digest(f"sha1={hash_digest}", signature)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Verifica a assinatura enviada pelo GitHub
    signature = request.headers.get('X-Hub-Signature')
    payload = request.data

    if not verify_signature(payload, signature):
        return jsonify({'message': 'Invalid signature'}), 403

    # Converte o payload recebido para JSON
    event_data = request.json

    # Verifica o tipo de evento
    event_type = request.headers.get('X-GitHub-Event')
    print(f"Recebi um evento do tipo: {event_type}")

    # Processa o evento conforme necessário
    if event_type == 'push':
        print(f"Push recebido de: {event_data['pusher']['name']}")
        # Faça algo com o evento push, como disparar um build ou enviar uma notificação
    elif event_type == 'pull_request':
        print(f"Pull request {event_data['action']} de: {event_data['pull_request']['user']['login']}")

    # Responde com sucesso
    return jsonify({'message': 'Webhook recebido!'}), 200

if __name__ == '__main__':
    app.run(port=5000)
