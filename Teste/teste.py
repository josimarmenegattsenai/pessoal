import webbrowser

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo Simples</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Este HTML foi gerado por Python.</p>
</body>
</html>
"""

with open("pagina.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html_content)

webbrowser.open("pagina.html")
