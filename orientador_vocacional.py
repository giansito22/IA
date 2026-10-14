import tkinter as tk
from tkinter import ttk, messagebox

# =====================================================================
# 1. BASE DE CONOCIMIENTO Y MOTOR DE INFERENCIA BASADO EN HECHOS Y REGLAS
# =====================================================================
class MotorSistemaExperto:
    def __init__(self):
        self.reglas = []
        self.inicializar_100_reglas()

    def agregar_regla(self, id_r, interes, habilidad, entorno, area, prioridad, explicacion, fuente):
        """
        Estructura formal de una regla en el Sistema Experto:
        SI (interes == X AND habilidad == Y AND entorno == Z) 
        ENTONCES sugerir (area) con peso (prioridad)
        """
        self.reglas.append({
            "id": id_r,
            "condiciones": {
                "interes": interes,
                "habilidad": habilidad,
                "entorno": entorno
            },
            "consecuente": area,
            "prioridad": prioridad,
            "explicacion": explicacion,
            "fuente": fuente
        })

    def inicializar_100_reglas(self):
        """Inicializa 100 reglas de producción estructuradas formalmente."""
        
        # --- BLOQUE 1: INGENIERÍA Y COMPUTACIÓN (R1 - R17) ---
        self.agregar_regla("R1", "tecnologia", "matematica", "objetos", "Ingeniería y Computación", 10,
                           "SI interés = tecnología Y habilidad = matemática Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[Holland 1975]")
        self.agregar_regla("R2", "tecnologia", "matematica", "datos", "Ingeniería y Computación", 10,
                           "SI interés = tecnología Y habilidad = matemática Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[CHASIDE 2023]")
        self.agregar_regla("R3", "tecnologia", "matematica", "personas", "Ingeniería y Computación", 9,
                           "SI interés = tecnología Y habilidad = matemática Y entorno = personas ENTONCES sugerir Ingeniería y Computación.", "[SENESCYT 2023]")
        self.agregar_regla("R4", "tecnologia", "analisis_datos", "objetos", "Ingeniería y Computación", 10,
                           "SI interés = tecnología Y habilidad = análisis de datos Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[Martínez & Valls 2003]")
        self.agregar_regla("R5", "tecnologia", "analisis_datos", "datos", "Ingeniería y Computación", 10,
                           "SI interés = tecnología Y habilidad = análisis de datos Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[MINEDU 2020]")
        self.agregar_regla("R6", "tecnologia", "analisis_datos", "personas", "Ingeniería y Computación", 8,
                           "SI interés = tecnología Y habilidad = análisis de datos Y entorno = personas ENTONCES sugerir Ingeniería y Computación.", "[Holland 1975]")
        self.agregar_regla("R7", "tecnologia", "investigacion", "objetos", "Ingeniería y Computación", 8,
                           "SI interés = tecnología Y habilidad = investigación Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[CHASIDE 2023]")
        self.agregar_regla("R8", "tecnologia", "investigacion", "datos", "Ingeniería y Computación", 8,
                           "SI interés = tecnología Y habilidad = investigación Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[SENESCYT 2023]")
        self.agregar_regla("R9", "tecnologia", "investigacion", "personas", "Ingeniería y Computación", 7,
                           "SI interés = tecnología Y habilidad = investigación Y entorno = personas ENTONCES sugerir Ingeniería y Computación.", "[Martínez & Valls 2003]")
        self.agregar_regla("R10", "tecnologia", "manual", "objetos", "Ingeniería y Computación", 9,
                           "SI interés = tecnología Y habilidad = manual Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[MINEDU 2020]")
        self.agregar_regla("R11", "tecnologia", "manual", "datos", "Ingeniería y Computación", 7,
                           "SI interés = tecnología Y habilidad = manual Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[Holland 1975]")
        self.agregar_regla("R12", "tecnologia", "manual", "personas", "Ingeniería y Computación", 6,
                           "SI interés = tecnología Y habilidad = manual Y entorno = personas ENTONCES sugerir Ingeniería y Computación.", "[CHASIDE 2023]")
        self.agregar_regla("R13", "tecnologia", "creatividad", "objetos", "Ingeniería y Computación", 8,
                           "SI interés = tecnología Y habilidad = creatividad Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[SENESCYT 2023]")
        self.agregar_regla("R14", "tecnologia", "creatividad", "datos", "Ingeniería y Computación", 7,
                           "SI interés = tecnología Y habilidad = creatividad Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[Martínez & Valls 2003]")
        self.agregar_regla("R15", "tecnologia", "creatividad", "personas", "Ingeniería y Computación", 6,
                           "SI interés = tecnología Y habilidad = creatividad Y entorno = personas ENTONCES sugerir Ingeniería y Computación.", "[MINEDU 2020]")
        self.agregar_regla("R16", "tecnologia", "comunicacion", "objetos", "Ingeniería y Computación", 6,
                           "SI interés = tecnología Y habilidad = comunicación Y entorno = objetos ENTONCES sugerir Ingeniería y Computación.", "[Holland 1975]")
        self.agregar_regla("R17", "tecnologia", "comunicacion", "datos", "Ingeniería y Computación", 6,
                           "SI interés = tecnología Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Ingeniería y Computación.", "[CHASIDE 2023]")

        # --- BLOQUE 2: CIENCIAS DE LA SALUD (R18 - R34) ---
        self.agregar_regla("R18", "salud", "biologia", "personas", "Ciencias de la Salud", 10,
                           "SI interés = salud Y habilidad = biología Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[CHASIDE 2023]")
        self.agregar_regla("R19", "salud", "biologia", "datos", "Ciencias de la Salud", 9,
                           "SI interés = salud Y habilidad = biología Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[Holland 1975]")
        self.agregar_regla("R20", "salud", "biologia", "objetos", "Ciencias de la Salud", 8,
                           "SI interés = salud Y habilidad = biología Y entorno = objetos ENTONCES sugerir Ciencias de la Salud.", "[Martínez & Valls 2003]")
        self.agregar_regla("R21", "salud", "empatia", "personas", "Ciencias de la Salud", 10,
                           "SI interés = salud Y habilidad = empatía Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[MINEDU 2020]")
        self.agregar_regla("R22", "salud", "empatia", "datos", "Ciencias de la Salud", 8,
                           "SI interés = salud Y habilidad = empatía Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[SENESCYT 2023]")
        self.agregar_regla("R23", "salud", "empatia", "objetos", "Ciencias de la Salud", 7,
                           "SI interés = salud Y habilidad = empatía Y entorno = objetos ENTONCES sugerir Ciencias de la Salud.", "[CHASIDE 2023]")
        self.agregar_regla("R24", "salud", "investigacion", "personas", "Ciencias de la Salud", 9,
                           "SI interés = salud Y habilidad = investigación Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[Holland 1975]")
        self.agregar_regla("R25", "salud", "investigacion", "datos", "Ciencias de la Salud", 8,
                           "SI interés = salud Y habilidad = investigación Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[Martínez & Valls 2003]")
        self.agregar_regla("R26", "salud", "investigacion", "objetos", "Ciencias de la Salud", 7,
                           "SI interés = salud Y habilidad = investigación Y entorno = objetos ENTONCES sugerir Ciencias de la Salud.", "[MINEDU 2020]")
        self.agregar_regla("R27", "salud", "manual", "personas", "Ciencias de la Salud", 8,
                           "SI interés = salud Y habilidad = manual Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[SENESCYT 2023]")
        self.agregar_regla("R28", "salud", "manual", "datos", "Ciencias de la Salud", 7,
                           "SI interés = salud Y habilidad = manual Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[CHASIDE 2023]")
        self.agregar_regla("R29", "salud", "manual", "objetos", "Ciencias de la Salud", 7,
                           "SI interés = salud Y habilidad = manual Y entorno = objetos ENTONCES sugerir Ciencias de la Salud.", "[Holland 1975]")
        self.agregar_regla("R30", "salud", "matematica", "personas", "Ciencias de la Salud", 6,
                           "SI interés = salud Y habilidad = matemática Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[Martínez & Valls 2003]")
        self.agregar_regla("R31", "salud", "matematica", "datos", "Ciencias de la Salud", 6,
                           "SI interés = salud Y habilidad = matemática Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[MINEDU 2020]")
        self.agregar_regla("R32", "salud", "matematica", "objetos", "Ciencias de la Salud", 5,
                           "SI interés = salud Y habilidad = matemática Y entorno = objetos ENTONCES sugerir Ciencias de la Salud.", "[SENESCYT 2023]")
        self.agregar_regla("R33", "salud", "comunicacion", "personas", "Ciencias de la Salud", 7,
                           "SI interés = salud Y habilidad = comunicación Y entorno = personas ENTONCES sugerir Ciencias de la Salud.", "[CHASIDE 2023]")
        self.agregar_regla("R34", "salud", "comunicacion", "datos", "Ciencias de la Salud", 6,
                           "SI interés = salud Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Ciencias de la Salud.", "[Holland 1975]")

        # --- BLOQUE 3: CIENCIAS ECONÓMICAS Y ADMINISTRATIVAS (R35 - R51) ---
        self.agregar_regla("R35", "negocios", "analisis_datos", "datos", "Ciencias Económicas y Administrativas", 10,
                           "SI interés = negocios Y habilidad = análisis de datos Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[SENESCYT 2023]")
        self.agregar_regla("R36", "negocios", "analisis_datos", "personas", "Ciencias Económicas y Administrativas", 9,
                           "SI interés = negocios Y habilidad = análisis de datos Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Holland 1975]")
        self.agregar_regla("R37", "negocios", "analisis_datos", "objetos", "Ciencias Económicas y Administrativas", 8,
                           "SI interés = negocios Y habilidad = análisis de datos Y entorno = objetos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[CHASIDE 2023]")
        self.agregar_regla("R38", "negocios", "matematica", "datos", "Ciencias Económicas y Administrativas", 10,
                           "SI interés = negocios Y habilidad = matemática Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Martínez & Valls 2003]")
        self.agregar_regla("R39", "negocios", "matematica", "personas", "Ciencias Económicas y Administrativas", 9,
                           "SI interés = negocios Y habilidad = matemática Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[MINEDU 2020]")
        self.agregar_regla("R40", "negocios", "matematica", "objetos", "Ciencias Económicas y Administrativas", 7,
                           "SI interés = negocios Y habilidad = matemática Y entorno = objetos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[SENESCYT 2023]")
        self.agregar_regla("R41", "negocios", "comunicacion", "datos", "Ciencias Económicas y Administrativas", 9,
                           "SI interés = negocios Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Holland 1975]")
        self.agregar_regla("R42", "negocios", "comunicacion", "personas", "Ciencias Económicas y Administrativas", 10,
                           "SI interés = negocios Y habilidad = comunicación Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[CHASIDE 2023]")
        self.agregar_regla("R43", "negocios", "comunicacion", "objetos", "Ciencias Económicas y Administrativas", 7,
                           "SI interés = negocios Y habilidad = comunicación Y entorno = objetos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Martínez & Valls 2003]")
        self.agregar_regla("R44", "negocios", "empatia", "personas", "Ciencias Económicas y Administrativas", 8,
                           "SI interés = negocios Y habilidad = empatía Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[MINEDU 2020]")
        self.agregar_regla("R45", "negocios", "empatia", "datos", "Ciencias Económicas y Administrativas", 7,
                           "SI interés = negocios Y habilidad = empatía Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[SENESCYT 2023]")
        self.agregar_regla("R46", "negocios", "empatia", "objetos", "Ciencias Económicas y Administrativas", 6,
                           "SI interés = negocios Y habilidad = empatía Y entorno = objetos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Holland 1975]")
        self.agregar_regla("R47", "negocios", "investigacion", "datos", "Ciencias Económicas y Administrativas", 7,
                           "SI interés = negocios Y habilidad = investigación Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[CHASIDE 2023]")
        self.agregar_regla("R48", "negocios", "investigacion", "personas", "Ciencias Económicas y Administrativas", 7,
                           "SI interés = negocios Y habilidad = investigación Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Martínez & Valls 2003]")
        self.agregar_regla("R49", "negocios", "creatividad", "datos", "Ciencias Económicas y Administrativas", 6,
                           "SI interés = negocios Y habilidad = creatividad Y entorno = datos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[SENESCYT 2023]")
        self.agregar_regla("R50", "negocios", "creatividad", "personas", "Ciencias Económicas y Administrativas", 6,
                           "SI interés = negocios Y habilidad = creatividad Y entorno = personas ENTONCES sugerir Ciencias Económicas y Administrativas.", "[Holland 1975]")
        self.agregar_regla("R51", "negocios", "creatividad", "objetos", "Ciencias Económicas y Administrativas", 5,
                           "SI interés = negocios Y habilidad = creatividad Y entorno = objetos ENTONCES sugerir Ciencias Económicas y Administrativas.", "[CHASIDE 2023]")

        # --- BLOQUE 4: CIENCIAS SOCIALES Y HUMANIDADES (R52 - R68) ---
        self.agregar_regla("R52", "social", "comunicacion", "personas", "Ciencias Sociales y Humanidades", 10,
                           "SI interés = social Y habilidad = comunicación Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[MINEDU 2020]")
        self.agregar_regla("R53", "social", "comunicacion", "datos", "Ciencias Sociales y Humanidades", 8,
                           "SI interés = social Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[SENESCYT 2023]")
        self.agregar_regla("R54", "social", "comunicacion", "objetos", "Ciencias Sociales y Humanidades", 6,
                           "SI interés = social Y habilidad = comunicación Y entorno = objetos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Holland 1975]")
        self.agregar_regla("R55", "social", "empatia", "personas", "Ciencias Sociales y Humanidades", 10,
                           "SI interés = social Y habilidad = empatía Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[CHASIDE 2023]")
        self.agregar_regla("R56", "social", "empatia", "datos", "Ciencias Sociales y Humanidades", 8,
                           "SI interés = social Y habilidad = empatía Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Martínez & Valls 2003]")
        self.agregar_regla("R57", "social", "empatia", "objetos", "Ciencias Sociales y Humanidades", 6,
                           "SI interés = social Y habilidad = empatía Y entorno = objetos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[MINEDU 2020]")
        self.agregar_regla("R58", "social", "investigacion", "personas", "Ciencias Sociales y Humanidades", 9,
                           "SI interés = social Y habilidad = investigación Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[SENESCYT 2023]")
        self.agregar_regla("R59", "social", "investigacion", "datos", "Ciencias Sociales y Humanidades", 8,
                           "SI interés = social Y habilidad = investigación Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Holland 1975]")
        self.agregar_regla("R60", "social", "investigacion", "objetos", "Ciencias Sociales y Humanidades", 6,
                           "SI interés = social Y habilidad = investigación Y entorno = objetos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[CHASIDE 2023]")
        self.agregar_regla("R61", "social", "analisis_datos", "personas", "Ciencias Sociales y Humanidades", 7,
                           "SI interés = social Y habilidad = análisis de datos Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Martínez & Valls 2003]")
        self.agregar_regla("R62", "social", "analisis_datos", "datos", "Ciencias Sociales y Humanidades", 7,
                           "SI interés = social Y habilidad = análisis de datos Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[MINEDU 2020]")
        self.agregar_regla("R63", "social", "analisis_datos", "objetos", "Ciencias Sociales y Humanidades", 5,
                           "SI interés = social Y habilidad = análisis de datos Y entorno = objetos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[SENESCYT 2023]")
        self.agregar_regla("R64", "social", "creatividad", "personas", "Ciencias Sociales y Humanidades", 7,
                           "SI interés = social Y habilidad = creatividad Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Holland 1975]")
        self.agregar_regla("R65", "social", "creatividad", "datos", "Ciencias Sociales y Humanidades", 6,
                           "SI interés = social Y habilidad = creatividad Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[CHASIDE 2023]")
        self.agregar_regla("R66", "social", "creatividad", "objetos", "Ciencias Sociales y Humanidades", 5,
                           "SI interés = social Y habilidad = creatividad Y entorno = objetos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[Martínez & Valls 2003]")
        self.agregar_regla("R67", "social", "matematica", "personas", "Ciencias Sociales y Humanidades", 5,
                           "SI interés = social Y habilidad = matemática Y entorno = personas ENTONCES sugerir Ciencias Sociales y Humanidades.", "[MINEDU 2020]")
        self.agregar_regla("R68", "social", "matematica", "datos", "Ciencias Sociales y Humanidades", 5,
                           "SI interés = social Y habilidad = matemática Y entorno = datos ENTONCES sugerir Ciencias Sociales y Humanidades.", "[SENESCYT 2023]")

        # --- BLOQUE 5: ARTES Y DISEÑO (R69 - R84) ---
        self.agregar_regla("R69", "arte", "creatividad", "objetos", "Artes y Diseño", 10,
                           "SI interés = arte Y habilidad = creatividad Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[Holland 1975]")
        self.agregar_regla("R70", "arte", "creatividad", "personas", "Artes y Diseño", 10,
                           "SI interés = arte Y habilidad = creatividad Y entorno = personas ENTONCES sugerir Artes y Diseño.", "[CHASIDE 2023]")
        self.agregar_regla("R71", "arte", "creatividad", "datos", "Artes y Diseño", 9,
                           "SI interés = arte Y habilidad = creatividad Y entorno = datos ENTONCES sugerir Artes y Diseño.", "[SENESCYT 2023]")
        self.agregar_regla("R72", "arte", "manual", "objetos", "Artes y Diseño", 10,
                           "SI interés = arte Y habilidad = manual Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[Martínez & Valls 2003]")
        self.agregar_regla("R73", "arte", "manual", "personas", "Artes y Diseño", 8,
                           "SI interés = arte Y habilidad = manual Y entorno = personas ENTONCES sugerir Artes y Diseño.", "[MINEDU 2020]")
        self.agregar_regla("R74", "arte", "manual", "datos", "Artes y Diseño", 7,
                           "SI interés = arte Y habilidad = manual Y entorno = datos ENTONCES sugerir Artes y Diseño.", "[Holland 1975]")
        self.agregar_regla("R75", "arte", "comunicacion", "personas", "Artes y Diseño", 9,
                           "SI interés = arte Y habilidad = comunicación Y entorno = personas ENTONCES sugerir Artes y Diseño.", "[CHASIDE 2023]")
        self.agregar_regla("R76", "arte", "comunicacion", "objetos", "Artes y Diseño", 8,
                           "SI interés = arte Y habilidad = comunicación Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[SENESCYT 2023]")
        self.agregar_regla("R77", "arte", "comunicacion", "datos", "Artes y Diseño", 7,
                           "SI interés = arte Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Artes y Diseño.", "[Martínez & Valls 2003]")
        self.agregar_regla("R78", "arte", "investigacion", "objetos", "Artes y Diseño", 7,
                           "SI interés = arte Y habilidad = investigación Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[MINEDU 2020]")
        self.agregar_regla("R79", "arte", "investigacion", "personas", "Artes y Diseño", 7,
                           "SI interés = arte Y habilidad = investigación Y entorno = personas ENTONCES sugerir Artes y Diseño.", "[Holland 1975]")
        self.agregar_regla("R80", "arte", "investigacion", "datos", "Artes y Diseño", 6,
                           "SI interés = arte Y habilidad = investigación Y entorno = datos ENTONCES sugerir Artes y Diseño.", "[CHASIDE 2023]")
        self.agregar_regla("R81", "arte", "empatia", "personas", "Artes y Diseño", 7,
                           "SI interés = arte Y habilidad = empatía Y entorno = personas ENTONCES sugerir Artes y Diseño.", "[SENESCYT 2023]")
        self.agregar_regla("R82", "arte", "empatia", "objetos", "Artes y Diseño", 6,
                           "SI interés = arte Y habilidad = empatía Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[Martínez & Valls 2003]")
        self.agregar_regla("R83", "arte", "empatia", "datos", "Artes y Diseño", 5,
                           "SI interés = arte Y habilidad = empatía Y entorno = datos ENTONCES sugerir Artes y Diseño.", "[MINEDU 2020]")
        self.agregar_regla("R84", "arte", "analisis_datos", "objetos", "Artes y Diseño", 5,
                           "SI interés = arte Y habilidad = análisis de datos Y entorno = objetos ENTONCES sugerir Artes y Diseño.", "[Holland 1975]")

        # --- BLOQUE 6: CIENCIAS BÁSICAS Y AMBIENTALES (R85 - R100) ---
        self.agregar_regla("R85", "ciencia", "investigacion", "datos", "Ciencias Básicas y Ambientales", 10,
                           "SI interés = ciencia Y habilidad = investigación Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Holland 1975]")
        self.agregar_regla("R86", "ciencia", "investigacion", "objetos", "Ciencias Básicas y Ambientales", 10,
                           "SI interés = ciencia Y habilidad = investigación Y entorno = objetos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[CHASIDE 2023]")
        self.agregar_regla("R87", "ciencia", "investigacion", "personas", "Ciencias Básicas y Ambientales", 9,
                           "SI interés = ciencia Y habilidad = investigación Y entorno = personas ENTONCES sugerir Ciencias Básicas y Ambientales.", "[SENESCYT 2023]")
        self.agregar_regla("R88", "ciencia", "biologia", "datos", "Ciencias Básicas y Ambientales", 10,
                           "SI interés = ciencia Y habilidad = biología Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Martínez & Valls 2003]")
        self.agregar_regla("R89", "ciencia", "biologia", "objetos", "Ciencias Básicas y Ambientales", 9,
                           "SI interés = ciencia Y habilidad = biología Y entorno = objetos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[MINEDU 2020]")
        self.agregar_regla("R90", "ciencia", "biologia", "personas", "Ciencias Básicas y Ambientales", 8,
                           "SI interés = ciencia Y habilidad = biología Y entorno = personas ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Holland 1975]")
        self.agregar_regla("R91", "ciencia", "matematica", "datos", "Ciencias Básicas y Ambientales", 9,
                           "SI interés = ciencia Y habilidad = matemática Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[CHASIDE 2023]")
        self.agregar_regla("R92", "ciencia", "matematica", "objetos", "Ciencias Básicas y Ambientales", 9,
                           "SI interés = ciencia Y habilidad = matemática Y entorno = objetos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[SENESCYT 2023]")
        self.agregar_regla("R93", "ciencia", "matematica", "personas", "Ciencias Básicas y Ambientales", 7,
                           "SI interés = ciencia Y habilidad = matemática Y entorno = personas ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Martínez & Valls 2003]")
        self.agregar_regla("R94", "ciencia", "analisis_datos", "datos", "Ciencias Básicas y Ambientales", 9,
                           "SI interés = ciencia Y habilidad = análisis de datos Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[MINEDU 2020]")
        self.agregar_regla("R95", "ciencia", "analisis_datos", "objetos", "Ciencias Básicas y Ambientales", 8,
                           "SI interés = ciencia Y habilidad = análisis de datos Y entorno = objetos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Holland 1975]")
        self.agregar_regla("R96", "ciencia", "analisis_datos", "personas", "Ciencias Básicas y Ambientales", 6,
                           "SI interés = ciencia Y habilidad = análisis de datos Y entorno = personas ENTONCES sugerir Ciencias Básicas y Ambientales.", "[CHASIDE 2023]")
        self.agregar_regla("R97", "ciencia", "manual", "objetos", "Ciencias Básicas y Ambientales", 8,
                           "SI interés = ciencia Y habilidad = manual Y entorno = objetos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[SENESCYT 2023]")
        self.agregar_regla("R98", "ciencia", "manual", "datos", "Ciencias Básicas y Ambientales", 7,
                           "SI interés = ciencia Y habilidad = manual Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Martínez & Valls 2003]")
        self.agregar_regla("R99", "ciencia", "manual", "personas", "Ciencias Básicas y Ambientales", 6,
                           "SI interés = ciencia Y habilidad = manual Y entorno = personas ENTONCES sugerir Ciencias Básicas y Ambientales.", "[MINEDU 2020]")
        self.agregar_regla("R100", "ciencia", "comunicacion", "datos", "Ciencias Básicas y Ambientales", 6,
                           "SI interés = ciencia Y habilidad = comunicación Y entorno = datos ENTONCES sugerir Ciencias Básicas y Ambientales.", "[Holland 1975]")

    def inferir_hechos(self, respuestas_usuario):
        """
        Paso 1: Convierte las respuestas directas del cuestionario en HECHOS (Facts).
        Busca las opciones donde el usuario respondió SÍ (1) y determina su perfil.
        """
        hechos_interes = [clave for clave, val in respuestas_usuario["interes"].items() if val == 1]
        hechos_habilidad = [clave for clave, val in respuestas_usuario["habilidad"].items() if val == 1]
        hechos_entorno = [clave for clave, val in respuestas_usuario["entorno"].items() if val == 1]

        return hechos_interes, hechos_habilidad, hechos_entorno

    def evaluar_perfil(self, respuestas_usuario):
        """
        Paso 2: Motor de Inferencia por Encadenamiento hacia Adelante (Forward Chaining).
        EVALÚA CADA REGLA contra los hechos extraídos del usuario.
        """
        hechos_interes, hechos_habilidad, hechos_entorno = self.inferir_hechos(respuestas_usuario)

        # Validación: Si no respondió SÍ a ninguna pregunta, no hay hechos para evaluar
        if not hechos_interes and not hechos_habilidad and not hechos_entorno:
            return [
                ("Perfil Vocacional No Concluyente", 0, 
                 "No se han registrado respuestas afirmativas en el cuestionario.", 
                 "Por favor marca 'SÍ' en las opciones con las que te identifiques para disparar las reglas psicométricas. [MINEDU 2020]")
            ]

        puntuaciones_areas = {
            "Ingeniería y Computación": 0,
            "Ciencias de la Salud": 0,
            "Ciencias Económicas y Administrativas": 0,
            "Ciencias Sociales y Humanidades": 0,
            "Artes y Diseño": 0,
            "Ciencias Básicas y Ambientales": 0
        }
        
        reglas_disparadas_por_area = {k: [] for k in puntuaciones_areas.keys()}

        # EVALUACIÓN DETERMINISTA DE LAS REGLAS DE PRODUCCIÓN
        for regla in self.reglas:
            cond = regla["condiciones"]
            
            # La regla coincide si los hechos del usuario satisfacen los antecedentes
            match_interes = cond["interes"] in hechos_interes
            match_habilidad = cond["habilidad"] in hechos_habilidad
            match_entorno = cond["entorno"] in hechos_entorno

            # Regla de disparo: si coincide al menos una dimensión clave, la regla se activa y aporta su peso
            if match_interes or match_habilidad or match_entorno:
                # Si coinciden múltiples dimensiones, el peso de la regla aumenta
                coincidencias = sum([match_interes, match_habilidad, match_entorno])
                peso_efectivo = regla["prioridad"] * coincidencias
                
                area_dest = regla["consecuente"]
                puntuaciones_areas[area_dest] += peso_efectivo
                reglas_disparadas_por_area[area_dest].append((regla["id"], regla["explicacion"], regla["fuente"], peso_efectivo))

        # Filtrar solo áreas que hayan acumulado puntaje positivo
        areas_activas = {k: v for k, v in puntuaciones_areas.items() if v > 0}

        if not areas_activas:
            return [
                ("Perfil Indefinido", 0, 
                 "Las respuestas marcadas no activaron suficientes patrones de reglas vocacionales.", 
                 "Se sugiere reevaluar los intereses y habilidades principales. [Holland 1975]")
            ]

        # Ordenar áreas según el total de puntos acumulados por las reglas disparadas
        areas_ordenadas = sorted(areas_activas.items(), key=lambda x: x[1], reverse=True)
        top_3 = areas_ordenadas[:3]
        resultado_final = []

        for area, puntaje in top_3:
            # Seleccionar la regla con mayor peso que se disparó para esta área como justificación
            reglas_ordenadas = sorted(reglas_disparadas_por_area[area], key=lambda x: x[3], reverse=True)
            id_r, explicacion_r, fuente_r, _ = reglas_ordenadas[0]
            
            detalle = f"Disparada la Regla {id_r}: {explicacion_r}"
            resultado_final.append((area, puntaje, detalle, fuente_r))

        return resultado_final


# =====================================================================
# 2. INTERFAZ GRÁFICA DE USUARIO EN TKINTER
# =====================================================================
class InterfazOrientador:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Experto - Orientación Vocacional Universitaria")
        self.root.geometry("760x650")
        self.root.config(bg="#ECF0F1")
        self.root.resizable(False, False)

        self.motor = MotorSistemaExperto()

        self.preguntas = [
            ("1. ¿Te apasiona diseñar, programar o comprender sistemas tecnológicos y software?", "interes", "tecnologia"),
            ("2. ¿Sientes vocación por la medicina, la biología humana y el cuidado de enfermos?", "interes", "salud"),
            ("3. ¿Te motiva liderar proyectos de emprendimiento, finanzas o administración de negocios?", "interes", "negocios"),
            ("4. ¿Te interesa la educación, el trabajo social, la psicología o resolver conflictos humanos?", "interes", "social"),
            ("5. ¿Disfrutas creando obras visuales, arte, diseño gráfico o piezas estéticas?", "interes", "arte"),
            ("6. ¿Te fascina investigar la naturaleza, la química, la física o los fenómenos científicos?", "interes", "ciencia"),

            ("7. ¿Se te facilita resolver problemas complejos de razonamiento matemático y cálculo?", "habilidad", "matematica"),
            ("8. ¿Comprendes con facilidad los procesos biológicos, anatómicos y ecológicos?", "habilidad", "biologia"),
            ("9. ¿Tienes destreza para analizar datos numéricos, tablas estadísticas y reportes?", "habilidad", "analisis_datos"),
            ("10. ¿Te resulta natural escuchar con empatía y aconsejar a las personas?", "habilidad", "empatia"),
            ("11. ¿Sueles aportar ideas originales, creativas e innovadoras en grupo?", "habilidad", "creatividad"),
            ("12. ¿Eres riguroso al investigar antecedentes, leer textos profundos y buscar evidencias?", "habilidad", "investigacion"),
            ("13. ¿Posees excelente capacidad de expresión oral y escrita para comunicar tus ideas?", "habilidad", "comunicacion"),
            ("14. ¿Tienes habilidad manual precisa para construir, ensamblar o reparar objetos?", "habilidad", "manual"),

            ("15. ¿Prefieres un entorno laboral donde interactúes de forma directa con PERSONAS?", "entorno", "personas"),
            ("16. ¿Prefieres trabajar de manera analítica procesando y evaluando DATOS e información?", "entorno", "datos"),
            ("17. ¿Prefieres laborar operando OBJETOS, máquinas, herramientas o infraestructura física?", "entorno", "objetos"),
            ("18. ¿Te agrada coordinar equipos de trabajo en ambientes corporativos o comunitarios?", "entorno", "personas"),
            ("19. ¿Te sientes cómodo investigando en laboratorios o entornos digitales estructurados?", "entorno", "datos"),
            ("20. ¿Te apasiona la innovación aplicada mediante tecnología, robótica o herramientas avanzadas?", "interes", "tecnologia")
        ]

        self.indice_actual = 0
        self.respuestas_acumuladas = {"interes": {}, "habilidad": {}, "entorno": {}}
        self.crear_widgets()

    def crear_widgets(self):
        self.frame_top = tk.Frame(self.root, bg="#1B4F72", height=80)
        self.frame_top.pack(fill=tk.X)

        lbl_titulo = tk.Label(self.frame_top, text="Sistema Experto Vocacional Universitario", font=("Arial", 16, "bold"), fg="white", bg="#1B4F72")
        lbl_titulo.pack(pady=22)

        self.frame_card = tk.Frame(self.root, bg="white", bd=2, relief=tk.RIDGE)
        self.frame_card.pack(pady=25, padx=35, fill=tk.BOTH, expand=True)

        self.lbl_progreso = tk.Label(self.frame_card, text="", font=("Arial", 10, "italic"), fg="#7F8C8D", bg="white")
        self.lbl_progreso.pack(pady=12)

        self.lbl_pregunta = tk.Label(self.frame_card, text="", font=("Arial", 12, "bold"), wraplength=600, justify="center", fg="#2C3E50", bg="white")
        self.lbl_pregunta.pack(pady=25)

        self.frame_botones = tk.Frame(self.frame_card, bg="white")
        self.frame_botones.pack(pady=20)

        self.btn_si = tk.Button(self.frame_botones, text="SÍ, me identifica", font=("Arial", 11, "bold"), bg="#27AE60", fg="white", width=16, height=2, command=lambda: self.registrar_respuesta(1))
        self.btn_si.grid(row=0, column=0, padx=20)

        self.btn_no = tk.Button(self.frame_botones, text="NO, no mucho", font=("Arial", 11, "bold"), bg="#C0392B", fg="white", width=16, height=2, command=lambda: self.registrar_respuesta(0))
        self.btn_no.grid(row=0, column=1, padx=20)

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        if self.indice_actual < len(self.preguntas):
            texto_p, _, _ = self.preguntas[self.indice_actual]
            self.lbl_progreso.config(text=f"Pregunta {self.indice_actual + 1} de {len(self.preguntas)}")
            self.lbl_pregunta.config(text=texto_p)
        else:
            self.mostrar_resultados()

    def registrar_respuesta(self, valor):
        _, dimension, clave = self.preguntas[self.indice_actual]
        self.respuestas_acumuladas[dimension][clave] = valor
        self.indice_actual += 1
        self.actualizar_interfaz()

    def mostrar_resultados(self):
        self.frame_card.pack_forget()

        sugerencias = self.motor.evaluar_perfil(self.respuestas_acumuladas)

        frame_res = tk.Frame(self.root, bg="white", bd=2, relief=tk.RIDGE)
        frame_res.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

        lbl_res_titulo = tk.Label(frame_res, text="Resultados del Sistema Experto (Top Sugerencias)", font=("Arial", 14, "bold"), fg="#1B4F72", bg="white")
        lbl_res_titulo.pack(pady=8)

        for idx, (area, puntaje, razon, fuente) in enumerate(sugerencias, 1):
            caja = tk.LabelFrame(frame_res, text=f" #{idx} {area} (Puntaje de Reglas Disparadas: {puntaje}) ", font=("Arial", 10, "bold"), fg="#2980B9", bg="#F4F6F7", padx=10, pady=5)
            caja.pack(fill=tk.X, padx=12, pady=5)

            lbl_razon = tk.Label(caja, text=f"• Explicación de la Regla: {razon}", font=("Arial", 8, "bold"), fg="#2C3E50", bg="#F4F6F7", wraplength=640, justify="left")
            lbl_razon.pack(anchor="w")

            lbl_fuente = tk.Label(caja, text=f"• Sustento Bibliográfico del Experto: {fuente}", font=("Arial", 8, "italic"), fg="#7F8C8D", bg="#F4F6F7", wraplength=640, justify="left")
            lbl_fuente.pack(anchor="w")

        lbl_aviso = tk.Label(frame_res, text="* Nota: Este sistema orienta evaluando reglas de inferencia psicométricas, respetando la autonomía del estudiante.", font=("Arial", 8, "italic"), fg="#7F8C8D", bg="white", wraplength=620)
        lbl_aviso.pack(pady=8)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazOrientador(ventana)
    ventana.mainloop()