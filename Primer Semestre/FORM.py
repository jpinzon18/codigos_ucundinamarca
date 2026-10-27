
"""
Rellenador de datos FICTICIOS para Microsoft Forms.
Procesa un registro por ejecución y se detiene antes de enviar.

Instalación:
    py -m pip install playwright
    py -m playwright install chromium

Ejemplos:
    py FORM.py --index 1
    py FORM.py --index 11
    py FORM.py --index 21

El programa no pulsa automáticamente el botón Enviar.
Usar únicamente en un formulario de prueba autorizado.
"""

import argparse
import re
import unicodedata
from difflib import SequenceMatcher
from playwright.sync_api import sync_playwright

FORM_URL = (
    "https://forms.cloud.microsoft/Pages/ResponsePage.aspx"
    "?id=oGfaB0MfjE6Xf1-ItkcO5tSiPFBRepRLmwNEiA_ps99UN0cyQUJYRzJCVE9KTDJaV1JTQ0k3SlpNQi4u"
)

ENTRADAS = [
    {
        "nombre": "Sebastián Andrés Pardo Beltrán",
        "edad": "23", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida típica colombiana",
        "saludable": "SI",
        "opciones": "Arepas de choclo, empanadas y jugos naturales",
        "franja": "11 a. m. – 2 p. m.",
        "justificacion": "Es una hora práctica para almorzar y probar platos diferentes.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Isabella Juliana Peña Salazar",
        "edad": "25", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Comida internacional",
        "saludable": "SI",
        "opciones": "Tacos, sushi y pasta",
        "franja": "12 p. m. – 4 p. m.",
        "justificacion": "Tendría tiempo de recorrer los puestos con calma.",
        "asistencia": "Sí, definitivamente"
    },
    {
        "nombre": "Mateo Alejandro Cifuentes Lara",
        "edad": "20", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida rápida",
        "saludable": "NO",
        "opciones": "Hamburguesas, perros calientes y papas",
        "franja": "2 p. m. – 5 p. m.",
        "justificacion": "En la tarde podría asistir después de terminar sus actividades.",
        "asistencia": "Tal vez"
    },
    {
        "nombre": "Gabriela Fernanda Ospina Cruz",
        "edad": "28", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Postres y bebidas",
        "saludable": "SI",
        "opciones": "Obleas, waffles, helados y limonadas",
        "franja": "3 p. m. – 6 p. m.",
        "justificacion": "Es un buen horario para comer algo dulce y compartir.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Tomás Enrique Beltrán Rincón",
        "edad": "32", "genero": "Masculino",
        "rol": "Externo",
        "tipo": "Comida tradicional de distintas regiones",
        "saludable": "SI",
        "opciones": "Ajiaco, tamales, arepas y envueltos",
        "franja": "10 a. m. – 2 p. m.",
        "justificacion": "Me interesa conocer platos regionales y aprovechar el horario del almuerzo.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Manuela Isabel Quintero Acosta",
        "edad": "22", "genero": "Femenino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida vegetariana y saludable",
        "saludable": "SI",
        "opciones": "Ensaladas, wraps y bowls de frutas",
        "franja": "11 a. m. – 1 p. m.",
        "justificacion": "Me gustaría encontrar opciones frescas y saludables.",
        "asistencia": "Sí, definitivamente"
    },
    {
        "nombre": "Samuel David Niño Cárdenas",
        "edad": "27", "genero": "Masculino",
        "rol": "Externo",
        "tipo": "Comida callejera",
        "saludable": "NO",
        "opciones": "Salchipapas, empanadas y choripanes",
        "franja": "12 p. m. – 3 p. m.",
        "justificacion": "Coincide con la hora de almuerzo y sería fácil pasar un rato.",
        "asistencia": "Tal vez"
    },
    {
        "nombre": "Daniela Alejandra Buitrago Mesa",
        "edad": "24", "genero": "Femenino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida colombiana casera",
        "saludable": "SI",
        "opciones": "Arroz con pollo, patacones y jugos naturales",
        "franja": "11 a. m. – 3 p. m.",
        "justificacion": "Es un horario amplio para almorzar y visitar varios puestos.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Esteban Mauricio Rincón Patiño",
        "edad": "30", "genero": "Masculino",
        "rol": "Externo",
        "tipo": "Comida mexicana e italiana",
        "saludable": "SI",
        "opciones": "Tacos, pizza y lasaña",
        "franja": "1 p. m. – 5 p. m.",
        "justificacion": "En la tarde tendría más disponibilidad para ir al evento.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Sara Milena Villamil Torres",
        "edad": "26", "genero": "Femenino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida variada y económica",
        "saludable": "SI",
        "opciones": "Sándwiches, arepas rellenas y ensalada de frutas",
        "franja": "9 a. m. – 12 p. m.",
        "justificacion": "La mañana es conveniente para quienes tienen compromisos por la tarde.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Nicolás Felipe Arévalo Méndez",
        "edad": "24", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida típica colombiana",
        "saludable": "SI",
        "opciones": "Bandeja paisa, arepas y jugos naturales",
        "franja": "11 a. m. – 2 p. m.",
        "justificacion": "El horario permite almorzar y conocer las propuestas gastronómicas.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Valentina María Duarte Rojas",
        "edad": "22", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Comida internacional",
        "saludable": "SI",
        "opciones": "Sushi, tacos y crepes",
        "franja": "12 p. m. – 4 p. m.",
        "justificacion": "Podría asistir después de sus actividades de la mañana.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Juan Sebastián Molina Vargas",
        "edad": "29", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida rápida",
        "saludable": "NO",
        "opciones": "Hamburguesas, perros calientes y papas",
        "franja": "2 p. m. – 5 p. m.",
        "justificacion": "La tarde es conveniente para recorrer los diferentes puestos.",
        "asistencia": "Tal vez"
    },
    {
        "nombre": "Laura Camila Sánchez Prieto",
        "edad": "26", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Postres y bebidas",
        "saludable": "SI",
        "opciones": "Obleas, brownies y limonadas",
        "franja": "3 p. m. – 6 p. m.",
        "justificacion": "Es una buena hora para compartir algo de comer con amigos.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Andrés Mauricio Cárdenas Gil",
        "edad": "31", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida tradicional de distintas regiones",
        "saludable": "SI",
        "opciones": "Ajiaco, tamales y empanadas",
        "franja": "10 a. m. – 2 p. m.",
        "justificacion": "Me interesa probar platos regionales durante el almuerzo.",
        "asistencia": "Sí, definitivamente"
    },
    {
        "nombre": "Mariana Lucía Torres Benítez",
        "edad": "21", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Comida vegetariana y saludable",
        "saludable": "SI",
        "opciones": "Ensaladas, wraps y bowls de frutas",
        "franja": "11 a. m. – 1 p. m.",
        "justificacion": "Prefiero encontrar alternativas frescas y saludables.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Felipe Santiago Rojas Cabrera",
        "edad": "27", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida callejera",
        "saludable": "NO",
        "opciones": "Empanadas, salchipapas y choripanes",
        "franja": "12 p. m. – 3 p. m.",
        "justificacion": "Coincide con el almuerzo y permite probar diferentes comidas.",
        "asistencia": "Tal vez"
    },
    {
        "nombre": "Natalia Andrea Castro Méndez",
        "edad": "25", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Comida colombiana casera",
        "saludable": "SI",
        "opciones": "Arroz con pollo, patacones y jugos naturales",
        "franja": "11 a. m. – 3 p. m.",
        "justificacion": "El horario es amplio y facilita visitar varios puestos.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Daniel Eduardo Acosta Rincón",
        "edad": "23", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida mexicana e italiana",
        "saludable": "SI",
        "opciones": "Tacos, pizza y lasaña",
        "franja": "1 p. m. – 5 p. m.",
        "justificacion": "La tarde me permitiría organizar el tiempo para asistir.",
        "asistencia": "Sí"
    },
    {
        "nombre": "Paula Andrea Lozano Silva",
        "edad": "28", "genero": "Femenino",
        "rol": "Externo",
        "tipo": "Comida variada y económica",
        "saludable": "SI",
        "opciones": "Sándwiches, arepas rellenas y ensalada de frutas",
        "franja": "9 a. m. – 12 p. m.",
        "justificacion": "La mañana me parece adecuada para aprovechar el evento.",
        "asistencia": "Sí, probablemente"
    },
    {
        "nombre": "Miguel Ángel Vargas Prieto",
        "edad": "30", "genero": "Masculino",
        "rol": "Creador de oportunidades",
        "tipo": "Comida típica colombiana",
        "saludable": "SI",
        "opciones": "Arepas, tamales y jugos naturales",
        "franja": "11 a. m. – 2 p. m.",
        "justificacion": "Es un horario práctico para almorzar y conocer la oferta gastronómica.",
        "asistencia": "Sí"
    },
]


def normalizar(texto):
    texto = unicodedata.normalize("NFKD", texto or "")
    texto = "".join(
        c for c in texto if not unicodedata.combining(c)
    )
    return re.sub(r"\s+", " ", texto.lower()).strip(" ¿?¡!:.")


def similitud(a, b):
    return SequenceMatcher(
        None, normalizar(a), normalizar(b)
    ).ratio()


def localizar_pregunta(page, pregunta):
    """
    Busca el contenedor de pregunta.
    Devuelve None si no puede identificarlo de forma fiable.
    """
    selectores = [
        '[data-automation-id="questionItem"]',
        '[data-automation-id="question-item"]',
    ]

    for selector in selectores:
        elementos = page.locator(selector)

        for i in range(elementos.count()):
            elemento = elementos.nth(i)

            try:
                if not elemento.is_visible():
                    continue

                texto = elemento.inner_text(timeout=1000)

                if normalizar(pregunta) in normalizar(texto):
                    return elemento
            except Exception:
                continue

    print(f"[AVISO] No se encontró la pregunta: {pregunta}")
    return None


def rellenar_texto(page, pregunta, respuesta):
    contenedor = localizar_pregunta(page, pregunta)

    if contenedor is None:
        return False

    selectores = [
        "textarea",
        'input[type="text"]',
        'input:not([type])',
        '[contenteditable="true"]',
    ]

    for selector in selectores:
        campos = contenedor.locator(selector)

        for i in range(campos.count()):
            campo = campos.nth(i)

            try:
                if not campo.is_visible() or not campo.is_enabled():
                    continue

                campo.fill(respuesta, timeout=2000)
                return True
            except Exception:
                continue

    return False


def seleccionar_opcion(page, pregunta, respuesta):
    contenedor = localizar_pregunta(page, pregunta)

    if contenedor is None:
        return False

    # Busca las opciones de radio, casillas y elementos accesibles.
    selectores = [
        '[role="radio"]',
        '[role="checkbox"]',
        'input[type="radio"]',
        'input[type="checkbox"]',
        'label',
        '[role="option"]',
    ]

    for selector in selectores:
        elementos = contenedor.locator(selector)

        for i in range(elementos.count()):
            elemento = elementos.nth(i)

            try:
                if not elemento.is_visible():
                    continue

                texto = (
                    elemento.get_attribute("aria-label")
                    or elemento.inner_text(timeout=700)
                    or elemento.get_attribute("value")
                    or ""
                )

                if normalizar(texto) == normalizar(respuesta):
                    elemento.click(timeout=2000)
                    return True
            except Exception:
                continue

    # Alternativa: texto exacto dentro del contenedor.
    textos = contenedor.get_by_text(respuesta, exact=True)

    for i in range(textos.count()):
        elemento = textos.nth(i)

        try:
            if elemento.is_visible():
                elemento.click(timeout=1500)
                return True
        except Exception:
            continue

    print(
        f"[AVISO] No se encontró la opción '{respuesta}' "
        f"en la pregunta: {pregunta}"
    )
    return False


def responder_auto(page, pregunta, respuesta):
    """
    Intenta rellenar texto. Si no hay un campo de texto,
    intenta seleccionar una opción existente.
    """
    if rellenar_texto(page, pregunta, respuesta):
        return True

    return seleccionar_opcion(page, pregunta, respuesta)


def main():
    parser = argparse.ArgumentParser(
        description="Preparar una respuesta ficticia para revisión."
    )
    parser.add_argument(
        "--index",
        type=int,
        default=1,
        help="Número de registro, del 1 al 21.",
    )
    args = parser.parse_args()

    if not 1 <= args.index <= len(ENTRADAS):
        parser.error(
            f"--index debe estar entre 1 y {len(ENTRADAS)}."
        )

    registro = ENTRADAS[args.index - 1]

    print(
        f"Registro {args.index}/{len(ENTRADAS)}: "
        f"{registro['nombre']} — {registro['rol']}"
    )

    # Los enunciados deben coincidir con los de tu formulario.
    preguntas_texto = [
        ("Por favor digite su nombre", "nombre"),
        ("Por favor digite su edad", "edad"),
        (
            "¿Qué tipo de comida desearía ver en una feria de gastronomía?",
            "tipo",
        ),
        (
            "¿Qué opciones de comida le gustaría ver en el evento?",
            "opciones",
        ),
        (
            "¿En qué franja horaria le gustaría que se realizara el evento?",
            "franja",
        ),
        (
            "Justifique su elección de franja horaria",
            "justificacion",
        ),
    ]

    preguntas_opciones = [
        ("Seleccione su género", "genero"),
        ("Escoja su rol", "rol"),
        (
            "¿Considera que los productos deberían promover comida saludable?",
            "saludable",
        ),
        (
            "¿Está considerando seriamente asistir al evento?",
            "asistencia",
        ),
    ]

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto(FORM_URL, wait_until="domcontentloaded")
        pagina.wait_for_timeout(3000)

        resultados = {}

        for pregunta, clave in preguntas_texto:
            resultados[pregunta] = responder_auto(
                pagina, pregunta, registro[clave]
            )

        for pregunta, clave in preguntas_opciones:
            resultados[pregunta] = seleccionar_opcion(
                pagina, pregunta, registro[clave]
            )

        captura = f"FORM_prueba_{args.index:02d}.png"
        pagina.screenshot(path=captura, full_page=True)

        print("\n--- RESULTADO ---")
        for pregunta, correcto in resultados.items():
            print(
                f"[{'OK' if correcto else 'REVISAR'}] {pregunta}"
            )

        print(f"\nCaptura guardada: {captura}")
        print("El programa NO ha pulsado Enviar.")
        print("Comprueba los campos y las opciones en Chromium.")

        input(
            "Pulsa Enter aquí cuando termines de revisar "
            "para cerrar el navegador..."
        )
        navegador.close()


if __name__ == "__main__":
    main()
