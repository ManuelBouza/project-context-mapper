import os
import datetime
import sys

# Carpetas a excluir
EXCLUDE_DIRS = {
    # Directorios comunes
    ".git",
    "coverage",
    ".cache",
    
    # Directorios backend
    "__pycache__",
    ".idea",
    ".pytest_cache",
    ".coverage",
    ".mypy_cache",
    ".venv", 
    "venv",
    "playwright-report",
    "test-results",
    ".ruff_cache",
    
    # Directorios frontend
    "node_modules",
    "dist", 
    "build",
    ".next"
}

# Ficheros a excluir
EXCLUDE_FILES = {
    ".DS_Store", 
    "thumbs.db", 
    "desktop.ini",
    "yarn.lock"
}

# Extensiones adicionales a excluir
ADDITIONAL_EXCLUDES = {".log", ".tmp", ".png", ".svg", ".ico", ".xlsx", ".csv"}  

def is_excluded(path: str) -> bool:
    """
    Verifica si una ruta o fichero debe ser excluido.
    """
    # Verifica si alguna carpeta en la ruta es excluida
    for exclude_dir in EXCLUDE_DIRS:
        if exclude_dir in path.split(os.sep):
            return True
    # Verifica si el fichero tiene un nombre o extensión excluida
    if os.path.basename(path) in EXCLUDE_FILES:
        return True
    for ext in ADDITIONAL_EXCLUDES:
        if path.endswith(ext):
            return True
    return False


def snapshot_project_content(project_path: str) -> None:
    """
    Lee todos los archivos de un proyecto y guarda su contenido en un archivo txt.
    El nombre del archivo incluye la última parte de la ruta, la fecha actual y la hora.
    """
    # Obtiene el nombre de la última carpeta de la ruta
    project_name = os.path.basename(os.path.normpath(project_path))
    # Genera el nombre de salida con fecha y hora actual
    date_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file = f"{project_name}_snapshot_{date_str}.txt"

    with open(output_file, "w", encoding="utf-8") as out_file:
        for root, dirs, files in os.walk(project_path):
            # Elimina carpetas excluidas de la lista dirs (modifica dirs in-place)
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                file_path = os.path.join(root, file)

                # Verifica si el archivo debe ser excluido
                if is_excluded(file_path):
                    continue
                try:
                    # Lee el contenido del archivo
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    # Guarda el contenido en el archivo de salida
                    out_file.write(f"# Ruta: {file_path}\n")
                    out_file.write(f"#{'-' * 80}\n")
                    out_file.write(content + "\n\n")
                    # Imprime la ruta del fichero guardado en el archivo
                    print(f"Fichero guardado: {file_path}")
                except Exception as e:
                    print(f"Error al leer {file_path}: {e}")
    print(f"\n Archivo guardado: {output_file}")


if __name__ == "__main__":
    # Configura la ruta del proyecto desde un parámetro de entrada
    if len(sys.argv) != 2:
        print("Uso: python main.py <ruta_del_proyecto>")
        sys.exit(1)
    
    PROJECT_PATH = sys.argv[1]
    if not os.path.isdir(PROJECT_PATH):
        print("Error: La ruta especificada no es un directorio válido.")
    else:
        snapshot_project_content(PROJECT_PATH)
