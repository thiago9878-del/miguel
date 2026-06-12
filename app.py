from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Datos de Thiago para la plantilla
    profile_data = {
        "name": "Thiago",
        "age": 17,
        "school": "Colegio Sarmiento",
        "location": "Recoleta, CABA, Buenos Aires",
        "experience": [
            {
                "role": "Vendedor / Atención al cliente",
                "place": "Local de ropa",
                "description": "Desarrollo de habilidades de comunicación, responsabilidad y gestión de ventas."
            },
            {
                "role": "Técnico Informático",
                "place": "Freelance / Independiente",
                "description": "Mantenimiento preventivo, reparación de hardware y optimización de sistemas operativos."
            },
            {
                "role": "Operador / Soporte",
                "place": "Centro de Simulación",
                "description": "Asistencia técnica en entornos de simulación y manejo de equipos especializados."
            }
        ],
        "skills": [
            {"name": "Python", "level": "Intermedio", "description": "Lenguaje versátil para automatización, análisis de datos y desarrollo web con Flask."},
            {"name": "Excel", "level": "Intermedio", "description": "Manejo de tablas dinámicas, funciones avanzadas y organización de datos complejos."},
            {"name": "HTML", "level": "Intermedio", "description": "Estructuración de contenido web moderno utilizando etiquetas semánticas."},
            {"name": "CSS", "level": "Intermedio", "description": "Diseño visual de páginas web, uso de Flexbox, Grid y personalización de estilos."}
        ],
        "interests": [
            {"name": "Deportes", "icon": "fas fa-futbol", "description": "Me encanta jugar a la pelota con mis amigos."},
            {"name": "Lectura", "icon": "fas fa-book-open", "description": "Disfruto de un buen libro para aprender y relajarme."},
            {"name": "Familia", "icon": "fas fa-walking", "description": "Pasear y compartir momentos especiales con mi familia."},
            {"name": "Tecnología", "icon": "fas fa-laptop-code", "description": "Explorar nuevas herramientas y lenguajes de programación."}
        ],
        "about_me": "Soy una persona muy sociable y familiera. En mis tiempos libres disfruto mucho de jugar a la pelota, leer y pasear con mi familia. Me considero alguien que valora mucho los vínculos personales y el trabajo en equipo.",
        "goal": "Expandir mis conocimientos en informática y desarrollarme profesionalmente en el sector IT.",
        "why_me": "Soy una persona altamente responsable, con una gran capacidad para adaptarme a diversos entornos de trabajo. Mi versatilidad me permite enfrentar nuevos desafíos con eficacia, asegurando siempre un compromiso total con los objetivos del equipo.",
        "contact": {
            "instagram": "thiago_rojas90",
            "gmail": "thiagorojas9878@gmail.com"
        }
    }
    return render_template('index.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True)
