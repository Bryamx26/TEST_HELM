from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Cette page est maintenant la porte d'entrée avec le bouton vers ArgoCD
    return render_template_string('''
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project ArgoCD 1</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f0f2f5;
            text-align: center;
        }
        .card {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        h1 { color: #2c3e50; margin-bottom: 20px; }
        .btn {
            display: inline-block;
            padding: 15px 30px;
            background: #e8590c;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            transition: background 0.3s;
        }
        .btn:hover { background: #fc8621; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Project ArgoCD 1</h1>
        <p>Hello, World! updated 3</p>
        <br>
        <a href="/argocd" class="btn">Voir le guide ArgoCD</a>
    </div>
</body>
</html>
:::::::::
                                  


''')

if __name__ == '__main__':
    app.run(debug=True)