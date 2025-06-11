# 🗺️ Project Context Mapper

Would you like your favorite AI (ChatGPT, Gemini, Claude, etc.) to understand your project **like a human** before programming, debugging, or adding new features?
This project is the ultimate solution to map the contents of any development project, file by file, and provide AIs with **the real context they need** to truly help you!

---

## 🚀 What is Project Context Mapper?

Project Context Mapper is a tool designed for developers, teams, and communities who want to give AIs the **maximum possible context** about the state, structure, and content of their projects, but with **total control** over what to share and how.
The tool generates a snapshot of your source code into a single text file, with different levels of depth and customization.

---

## 🎯 Project Goals

* **Facilitate collaboration** between humans and AIs in development tasks.
* Enable AIs to better understand the context, dependencies, and real organization of any code.
* Provide fast and controlled snapshots for tasks such as:

  * AI-assisted development.
  * Advanced debugging and troubleshooting.
  * Refactoring with global context.
  * Fast onboarding of new members (humans or bots).
  * Documentation and security analysis.

---

## 🧩 Capture Modes

You can choose among **4 modes** depending on the goal and size of your project:

1. **Capture the ENTIRE project**
   Ideal for small projects or when you want the AI to know absolutely everything (structure + content).

2. **Capture only paths**
   Perfect for large projects or when you only want the AI to understand the **structure** (file and directory tree), without showing the internal content of each file.

3. **Capture only certain files**
   Useful when the AI already knows the structure, but needs to see the contents of **key** files for a specific feature or bug, without overloading the context with unnecessary info.

4. **Combination of paths + some full files**
   The advanced mode!

   * Provides the complete project structure.
   * Adds the content of only **some relevant files** (defined by a whitelist).
   * Utility: Provide specific and efficient context for debugging or incremental development without losing the global view.

---

## 🧠 Recommended AI Interaction Strategy

To get the most out of Project Context Mapper and improve collaboration with the AI, we recommend this strategy:

1. First, provide the AI with the complete project structure, either without content or with basic content of key files like application startup, global structure, and navigation. This gives a solid overview without overwhelming it with unnecessary details.

2. Second, allow the AI to identify which specific files it needs to review to address the request or solve the problem.

3. Third, after that identification, ask the AI to give you a list of the required files, separated by commas.

4. Finally, use that list to generate a second snapshot with Project Context Mapper, including only the content of those specific files. This ensures the AI works with relevant, up-to-date information, optimizing time and accuracy.

---

## ✂️ Smart Exclusion of Files and Folders

Project Context Mapper automatically **ignores** files and directories that are not relevant for AI analysis, such as:

* Folders: .git, .cache, node\_modules, dist, build, .venv, **pycache**, etc.
* Files: .DS\_Store, yarn.lock, thumbs.db, etc.
* Extensions: .log, .tmp, .png, .svg, .xlsx, .csv, and other binaries or temporary files.

Need to exclude more? Just edit the EXCLUDE\_DIRS, EXCLUDE\_FILES, and ADDITIONAL\_EXCLUDES lists.

---

## ⚡ How does it work?

You only need Python 3.
Run the script indicating the project path and the desired options.

**Basic usage:**

```bash
python snapshot_project.py <project_path> [--only-paths] [--whitelist=path1,path2,...]
```

**Important note about `--whitelist` usage:**
If your whitelist contains spaces after commas, **you must enclose the entire argument in quotes** to prevent the shell from splitting it into multiple arguments. For example:

```bash
python snapshot_project.py /path/to/project --only-paths "--whitelist=app/main.py, app/database.py, app/core/security.py"
```

Alternatively, you can omit spaces after commas:

```bash
python snapshot_project.py /path/to/project --only-paths --whitelist=app/main.py,app/database.py,app/core/security.py
```

---

**Without extra parameters:**
Captures the complete content of all relevant files.

**With --only-paths:**
Only shows the folder and file structure (no content).

**With --whitelist:**
Shows only the content of specific paths/files.

**Combined --only-paths + --whitelist:**
Shows the complete project structure and also the content **only** of files included in the whitelist.
Ideal to give the AI a global vision of the project, but only detailed content of certain relevant files.

---

**Usage examples:**

Capture entire project (structure and content):

```bash
python snapshot_project.py /path/to/your/project
```

Only structure (folder and file names):

```bash
python snapshot_project.py /path/to/your/project --only-paths
```

Only some specific files (structure + those full files):

```bash
python snapshot_project.py /path/to/your/project --only-paths --whitelist=src/app.py,README.md,requirements.txt
```

Or with spaces in whitelist (use quotes):

```bash
python snapshot_project.py /path/to/your/project --only-paths "--whitelist=src/app.py, README.md, requirements.txt"
```

---

**What result do you get?**
A TXT file with all structured information, ready to upload to ChatGPT, Gemini, Claude or any AI to work with real and precise context.

---

## 💡 Why is it useful for AI and the community?

* **Avoids noise**: AI works only with relevant and updated information.
* **Maximum context, minimum effort**: share only what is needed, adjust granularity.
* **Audit and traceability**: textual snapshot, portable and ideal to attach to issues, PRs or AI queries.

---

## 🔒 Security and Privacy

* You decide what to share!
* Excludes binaries, passwords, dependencies, large or sensitive files by default.
* Easily customize exclusion lists according to your project needs.

---

## 👨‍💻 Main script (main.py)

The core of the tool is an easy-to-extend Python script (main.py). Here the exclusion filters, whitelist logic and output formatting are defined, so you can adapt it to any workflow.

---

## 🙌 Contribute

Got ideas, need more modes or filters?
Want support for another language or AI integration?
Pull requests, issues, and forks are more than welcome!

---

## ⭐ Give it a star if it helps you, and share your experience using the tool with your favorite AI.

---

Make your AI really understand your project, **not just read loose lines!**
Project Context Mapper – *Taking context to the next level.*

---

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
Muestra solo el contenido de rutas/ficheros específicos.

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
