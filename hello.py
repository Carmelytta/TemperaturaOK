from flask import Flask, send_from_directory, render_template, jsonify, request

app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

#Estructura y visualizacion de la pagina web principal
@app.route('/') 
def root():
    return render_template('float_capas.html')

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
    import sqlite3
    #Obtenemos datos de la bd
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

@app.route("/api/humedadS") #URL de humedad de suelo
def humedadS():
    samples = request.args.get('samples', 288)
    data = []
    import sqlite3
    #Obtenemos datos de la bd
    conn = sqlite3.connect('a.db')
    c = conn.cursor()
    #Recorremos la base de datos haciendo una consulta 
    #El numero de consultas seran las muestras que tome para la representacion
    for row in c.execute('SELECT * FROM humedadS ORDER BY fecha,hora LIMIT {}'.format(samples)):
        data.append({'humedadS': row[2], 'tiempo': '{} {}'.format(row[0], row[1])})
    #Adjuntamos los datos de la humedad y la fecha
    
    #Creamos lista con esos datos en json
    return jsonify({
	"data": data
}) 
	
@app.route("/api/humedadT") #URL de humedad del ambiente
def humedadT():
    samples = request.args.get('samples', 288)
    data = []
    import sqlite3
    #Obtenemos datos de la bd
    conn = sqlite3.connect('riego.db')
    c = conn.cursor()
    #Recorremos la base de datos haciendo una consulta 
    #El numero de consultas seran las muestras que tome para la representacion
    for row in c.execute('SELECT * FROM humedadT ORDER BY fecha,hora LIMIT {}'.format(samples)):
        data.append({'humedadT': row[2], 'tiempo': '{} {}'.format(row[0], row[1])})
    #Adjuntamos los datos de la humedad del ambiente y la fecha
    
    #Creamos lista con esos datos en json
    return jsonify({
	"data": data
}) 	

#Visualizacion de las distintas graficas del TFG

@app.route("/api/gTemperatura") #Estructura y visualizacion de la pagina web
def gTemp():
    return render_template('temperatura.html')

@app.route("/api/gHumedadS") #Estructura y visualizacion de la pagina web
def gHumS():
    return render_template('humedadS.html')

@app.route("/api/gHumedadT") #Estructura y visualizacion de la pagina web
def gHumT():
    return render_template('humedadT.html')


