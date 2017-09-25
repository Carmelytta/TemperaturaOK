from flask import Flask, send_from_directory, render_template, jsonify, request
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/') #Estructura y visualizacion de la pagina web
def root():
    return render_template('temperatura.html')

@app.route("/api/temperaturaEjemplo") #URL de ejemplo
def ejemplo():
    return jsonify({
	"data": [{
		"tiempo": 0,
		"temperatura": 25
	}, {
		"tiempo": 5,
		"temperatura": 30
	}]
}) 

@app.route("/api/temperatura") #URL de temperatura
def temperatura():
    samples = request.args.get('samples', 288)
    data = []
    #Obtenemos datos de la bd
    import sqlite3
    conn = sqlite3.connect('riego.db')
    c = conn.cursor()
    #Recorremos la base de datos haciendo una consulta 
    #El numero de consultas seran las muestras que tome para la representacion
    for row in c.execute('SELECT * FROM temperatura ORDER BY fecha,hora LIMIT {}'.format(samples)):
        data.append({'temperatura': row[2], 'tiempo': '{} {}'.format(row[0], row[1])})
    #Adjuntamos los datos de temperatura y la fecha
    
    #Creamos lista con esos datos en json
    return jsonify({
	"data": data
}) 
	


