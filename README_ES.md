# 🗺️ Project Context Mapper

¿Te gustaría que tu IA favorita (ChatGPT, Gemini, Claude, etc.) entienda tu proyecto **como un humano** antes de programar, depurar o agregar nuevas features?  
¡Este proyecto es la solución definitiva para mapear el contenido de cualquier proyecto de desarrollo, fichero por fichero, y proporcionar a las IAs **el contexto real que necesitan** para ayudarte de verdad!

---

## 🚀 ¿Qué es Project Context Mapper?

Project Context Mapper es una herramienta pensada para desarrolladores, equipos y comunidades que quieren dar a las IAs el **máximo contexto posible** sobre el estado, la estructura y el contenido de sus proyectos, pero con un **control total** sobre qué compartir y cómo.  
La herramienta genera un snapshot de tu código fuente en un único archivo de texto, con diferentes niveles de profundidad y personalización.

---

## 🎯 Objetivos del proyecto

* **Facilitar la colaboración** entre humanos e IAs en tareas de desarrollo.
* Permitir que las IAs puedan entender mejor el contexto, dependencias y organización real de cualquier código.
* Proveer snapshots rápidos y controlados para tareas como:

  * Desarrollo asistido por IA.
  * Debugging y troubleshooting avanzado.
  * Refactorización con contexto global.
  * Onboarding rápido de nuevos miembros (humanos o bots).
  * Documentación y análisis de seguridad.

---

## 🧩 Modalidades de captura

Puedes elegir entre **4 modalidades** según el objetivo y el tamaño de tu proyecto:

1. **Capturar TODO el proyecto**  
   Ideal para proyectos pequeños o cuando necesitas que la IA conozca absolutamente todo (estructura + contenido).

2. **Capturar solo las rutas**  
   Perfecto para proyectos grandes o cuando solo necesitas que la IA entienda la **estructura** (árbol de ficheros y directorios), sin mostrar el contenido interno de cada archivo.

3. **Capturar solo ciertos ficheros**  
   Útil cuando la IA ya conoce la estructura, pero necesita ver el contenido de archivos **clave** para una feature o bug específico, sin sobrecargar el contexto con info innecesaria.

4. **Combinación de rutas + algunos ficheros completos**  
   ¡El modo avanzado!  

   * Proporciona la estructura completa del proyecto.
   * Añade el contenido de solo **algunos archivos relevantes** (definidos por una whitelist).
   * Utilidad: Proporcionar contexto específico y eficiente para debugging o desarrollo incremental sin perder la visión global.

---

## 🆕 Sobre la opción `--whitelist`

La opción `--whitelist` acepta **tanto archivos individuales como rutas de carpetas/directorios** (relativas a la raíz del proyecto o absolutas).
Si incluyes una **carpeta**, el snapshot incluirá el **contenido completo de todos los ficheros dentro de esa carpeta** (de forma recursiva).

**Ejemplos:**

```bash
# Incluir un archivo específico y todos los archivos dentro de una carpeta
python snapshot_project.py /ruta/a/proyecto --only-paths --whitelist=app/main.py,app/services

# Con espacios (usa comillas)
python snapshot_project.py /ruta/a/proyecto --only-paths "--whitelist=app/main.py, app/services"
```

* Si pasas un archivo: se incluye solo el contenido de ese archivo.
* Si pasas una carpeta: se incluyen todos los archivos dentro de esa carpeta y sus subcarpetas con contenido completo.

> Si alguna ruta de la whitelist no existe, el script abortará y te notificará las rutas inválidas.

---

## 🧠 Estrategia recomendada para interacción con IA

Para sacar el máximo provecho a Project Context Mapper y mejorar la colaboración con la IA, te recomendamos esta estrategia:

1. Primero, proporciona a la IA la estructura completa del proyecto, ya sea sin contenido o con contenido básico de archivos clave como el arranque de la aplicación, la estructura global y la navegación. Esto le da una visión general sólida sin saturarla con detalles innecesarios.

2. Segundo, permite que la IA identifique qué ficheros específicos necesita revisar para atender la petición o resolver el problema planteado.

3. Tercero, tras esa identificación, solicita a la IA que te devuelva una lista de los archivos requeridos, separados por coma.

4. Finalmente, utiliza esa lista para generar un segundo snapshot con Project Context Mapper, incluyendo solo el contenido de esos ficheros específicos. Esto garantiza que la IA trabaje con la información relevante y actualizada, optimizando tiempos y precisión.

---

## ✂️ Exclusión inteligente de archivos y carpetas

Project Context Mapper permite **ignorar** automáticamente archivos y directorios que no son relevantes para el análisis de IA, como:

* Carpetas: .git, .cache, node\_modules, dist, build, .venv, **pycache**, etc.
* Archivos: .DS\_Store, yarn.lock, thumbs.db, etc.
* Extensiones: .log, .tmp, .png, .svg, .xlsx, .csv, y otros binarios o temporales.

¿Necesitas excluir más? Solo edita las listas EXCLUDE\_DIRS, EXCLUDE\_FILES y ADDITIONAL\_EXCLUDES.

---

## ⚡ ¿Cómo funciona?

Solo necesitas Python 3.  
Ejecuta el script indicando la ruta del proyecto y las opciones deseadas.

**Uso básico:**

```bash
python snapshot_project.py <ruta_del_proyecto> [--only-paths] [--whitelist=ruta1,ruta2,...]
```

**Nota importante sobre el uso de `--whitelist`:**
Si tu whitelist contiene espacios después de las comas, **debes poner todo el argumento entre comillas** para evitar que el shell lo divida en múltiples argumentos. Por ejemplo:

```bash
python snapshot_project.py /ruta/a/proyecto --only-paths "--whitelist=app/main.py, app/database.py, app/core/security.py"
```

Alternativamente, puedes omitir los espacios después de las comas:

```bash
python snapshot_project.py /ruta/a/proyecto --only-paths --whitelist=app/main.py,app/database.py,app/core/security.py
```

---

**Sin parámetros extra:**
  Captura el contenido completo de todos los archivos relevantes.

**Con --only-paths:**
  Solo muestra la estructura de carpetas y archivos (sin contenido).

**Con --whitelist:**
Muestra solo el contenido de rutas/ficheros específicos (o carpetas como se explicó arriba).

**Combinado --only-paths + --whitelist:**
Muestra la estructura completa del proyecto y, además, el contenido **solo** de los archivos que incluyas en la whitelist.
Ideal para darle a la IA la visión global del proyecto, pero solo el detalle completo de ciertos ficheros relevantes.

---

**Ejemplos de uso:**

Capturar todo el proyecto (estructura y contenido):

```bash
python snapshot_project.py /ruta/a/tu/proyecto
```

Solo estructura (nombres de carpetas y archivos):

```bash
python snapshot_project.py /ruta/a/tu/proyecto --only-paths
```

Solo algunos archivos concretos (estructura + esos ficheros completos):

```bash
python snapshot_project.py /ruta/a/tu/proyecto --only-paths --whitelist=src/app.py,README.md,requirements.txt
```

O con espacios en whitelist (usa comillas):

```bash
python snapshot_project.py /ruta/a/tu/proyecto --only-paths "--whitelist=src/app.py, README.md, requirements.txt"
```

---

**¿Qué resultado obtienes?**
Un archivo TXT con toda la información estructurada y lista para subir a ChatGPT, Gemini, Claude o cualquier IA para trabajar con contexto real y preciso.

---

## 💡 ¿Por qué es útil para la IA y la comunidad?

* **Evita el ruido**: la IA trabaja solo con la información relevante y actualizada.
* **Máximo contexto, mínimo esfuerzo**: comparte solo lo necesario, ajusta la granularidad.
* **Auditoría y trazabilidad**: snapshot textual y portable, ideal para adjuntar a issues, PRs o consultas con IA.

---

## 🔒 Seguridad y privacidad

* ¡Tú decides qué se comparte!
* Excluye binarios, passwords, dependencias, archivos grandes o sensibles por defecto.
* Personaliza fácilmente la lista de exclusiones según las necesidades de tu proyecto.

---

## 👨‍💻 Fragmento principal (main.py)

El núcleo de la herramienta es un script Python (main.py) fácil de extender. Aquí se definen los filtros de exclusión, la lógica de whitelist y el formato de salida, para que puedas adaptarlo a cualquier flujo de trabajo.

---

## 🙌 Contribuye

¿Tienes ideas, necesitas más modalidades o filtros?
¿Quieres soporte para otro lenguaje o integración con más IAs?
¡Pull requests, issues y forks son más que bienvenidos!

---

## ⭐ Dale una estrella si te ayuda, y comparte tu experiencia usando la herramienta con tu IA favorita.

---

¡Haz que tu IA realmente entienda tu proyecto, **no solo lea líneas sueltas**!
Project Context Mapper – *Llevar el contexto al siguiente nivel.*

---