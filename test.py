from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html>
            <head>
                <title>Мой сайт</title>
            </head>
            <body>
                <button onclick="startPythonScript()">Запустить программу на Python</button>
                <script>
                    function startPythonScript() {
                        fetch('/run-python-script')
                            .then(response => response.text())
                            .then(data => console.log(data))
                    }
                </script>
            </body>
        </html>
    """

@app.route('/run-python-script')
def run_python_script():
    print('Функция на Python была вызвана!')
    return 'Функция на Python была вызвана!'

if __name__ == '__main__':
    app.run()