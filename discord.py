from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# GitHub details
GITHUB_REPO_OWNER = "SamiaAlshehri"
GITHUB_REPO_NAME = "health_down_syndrome_chatbot"
GITHUB_ACCESS_TOKEN = "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"

@app.route('/discord-webhook', methods=['POST'])
def discord_webhook():
    data = request.json

    # Extract relevant information from the Discord message
    author = data['author']['username']
    message = data['content']
    
    # Create a GitHub issue
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues"
    headers = {
        "Authorization": f"token {GITHUB_ACCESS_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": f"Message from {author}",
        "body": f"**Author**: {author}\n**Message**: {message}"
    }
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 201:
        return jsonify({"message": "Issue created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create issue", "status_code": response.status_code}), 500

if __name__ == '__main__':
    app.run(debug=True)
