import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLlchemy

# ---Confuguracion Inicial ---
app = Flask(__name__)
#Configuracion de la base de daatos (usando SQLlite para este inicio rapido)
# En profuccion (Render/Heroku), cambiaras esto por la URL de PostgreeSQL
basedor = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' + os.path.join(basedir. 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- Modelos de Base de Datos (Sprint 1) ---
# (Estos son nuestros "Contenedores" de datos)

class User(db.Model):
  """Modelo paara los Estudiantes"""
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  name = db.Column(db.String(80), nullable=True)

class Topic(db.Model):
  """Modelo para los tems de matematicas"""
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullble=True)
  description = db.Column(dbString(500), nullable=True)
  
  exercises = db.relationship('Exercise', backref='topic', lazy=True)

class Exercise(db.Model):
  """MOdelo para los ejercicios"""
  id = db.Column(db.Integer, primary_key=True)
  question = db.Column(db.String(500), nullble=False)
  correct_answer = db.column(db.String(100), nullble=False)
  topic_id = db.Column(db.Integer, db.ForeingKey('topic.id), nullable=False)

# ---Rutas de la API (Endpoints) ---

@app.route('/')
def home():
  return jsonify({"mesage": "¡El servidor de la App de  Matemticas esta funcionando!"}]

@app.route('login', methods=['POST'])
def login():
  data = request.json
  print(f"Token recibido (simulado)): {data.get('token')}")
  user = User.query.first()
  if user:
    return jsonify({"mesage": "Login exitoso (simuldo)", "user_id": user.id})
  return jsonify({"mesgaae", "Login exitoso (simulaado)", "user_id":1})

@app.route('/topics', methods=['GET'])
def get_topics():
    """Obtiene la lista de todos los temas de matemáticas"""
    topics = Topic.query.all()
    # Convertimos los objetos de la DB a un formato JSON
    topic_list = [{"id": topic.id, "title": topic.title, "description": topic.description} for topic in topics]
    return jsonify(topic_list)

@app.route('/topics/<int:topic_id>/exercises', methods=['GET'])
def get_exercises_for_topic(topic_id):
    """Obtiene todos los ejercicios de un tema específico"""
    exercises = Exercise.query.filter_by(topic_id=topic_id).all()
    if not exercises:
        return jsonify({"message": "No hay ejercicios para este tema"}), 404
    
    exercise_list = [{"id": ex.id, "question": ex.question} for ex in exercises]
    return jsonify(exercise_list)

@app.route('/evaluate', methods=['POST'])
def evaluate_answer():
    """
    Placeholder (Sprint 2): Este es el endpoint clave.
    Aquí es donde llamaremos a nuestro "Motor de Evaluación".
    """
    data = request.json
    exercise_id = data.get('exercise_id')
    user_answer = data.get('user_answer')

    # --- INICIO DEL MOTOR DE EVALUACIÓN (Simulación Sprint 1) ---
    # (En Sprint 2, esta lógica será mucho más compleja)
    
    # 1. Buscamos la respuesta correcta en la DB
    exercise = Exercise.query.get(exercise_id)
    if not exercise:
        return jsonify({"message": "Ejercicio no encontrado"}), 404
    
    is_correct = False
    if exercise.correct_answer == user_answer:
        is_correct = True
    
    # 2. (Simulación) El motor genera la explicación
    steps = [
        f"Paso 1: Recibiste la pregunta '{exercise.question}'",
        f"Paso 2: Tu respuesta fue '{user_answer}'.",
        f"Paso 3: La respuesta correcta es '{exercise.correct_answer}'.",
        f"Paso 4: Por lo tanto, tu respuesta es {'CORRECTA' if is_correct else 'INCORRECTA'}."
    ]
    # --- FIN DEL MOTOR DE EVALUACIÓN ---

    return jsonify({
        "is_correct": is_correct,
        "explanation_steps": steps
    })


# --- Función para crear la DB y datos de prueba ---
def setup_database(app):
    with app.app_context():
        db.create_all() # Crea las tablas si no existen
        
        # Insertamos datos de prueba solo si no existen
        if not Topic.query.first():
            print("Base de datos vacía. Creando datos de prueba...")
            # Tema 1: Ecuaciones
            topic1 = Topic(title="Ecuaciones Lineales", description="Aprende a resolver para x.")
            db.session.add(topic1)
            
            # Ejercicios para Ecuaciones
            ex1 = Exercise(question="2x + 5 = 15", correct_answer="x=5", topic=topic1)
            ex2 = Exercise(question="3x - 1 = 8", correct_answer="x=3", topic=topic1)
            db.session.add(ex1)
            db.session.add(ex2)

            # Tema 2: Fracciones
            topic2 = Topic(title="Suma de Fracciones", description="Suma fracciones con diferente denominador.")
            db.session.add(topic2)
            
            # Ejercicios para Fracciones
            ex3 = Exercise(question="1/2 + 1/4", correct_answer="3/4", topic=topic2)
            db.session.add(ex3)

            # Usuario de prueba
            user1 = User(email="estudiante@prueba.com", name="Estudiante de Prueba")
            db.session.add(user1)

            db.session.commit() # Guarda los cambios
            print("Datos de prueba creados.")

# --- Ejecución de la App ---
if __name__ == '__main__':
    setup_database(app) # Prepara la base de datos antes de iniciar
    app.run(debug=True) # Inicia el servidor


  
                                                 

  
