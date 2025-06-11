import os
import datetime
import sys
from typing import Optional, Set

# Carpetas a excluir
EXCLUDE_DIRS = {
    # Directorios comunes
    ".git",
    ".cache",

    # Directorios de Structurizr
    ".structurizr",
    "images",
    "workspace.json",
    
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
    ".testmondata",
    
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


def path_in_whitelist(file_path: str, whitelist: Set[str]) -> bool:
    """
    Verifica si la ruta del fichero coincide o está dentro de alguna ruta de la whitelist.
    Se hace una comparación simple si la ruta contiene alguno de los caminos whitelist.
    """
    normalized_path = os.path.normpath(file_path)
    for allowed_path in whitelist:
        # Normalizar y comprobar si allowed_path es substring en ruta
        if allowed_path in normalized_path:
            return True
    return False


def snapshot_project_content(
    project_path: str, 
    only_paths: bool = False, 
    whitelist: Optional[Set[str]] = None
) -> None:
    """
    Lee todos los archivos de un proyecto y guarda su contenido en un archivo txt.
    El nombre del archivo incluye la última parte de la ruta, la fecha actual y la hora.
    whitelist: conjunto de rutas permitidas para mostrar contenido aunque only_paths sea True.
    """
    if whitelist is None:
        whitelist = set()

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
                    mostrar = False
                    mostrar_contenido = False

                    if only_paths:
                        # Mostrar todas las rutas, contenido solo para whitelist
                        mostrar = True
                        mostrar_contenido = path_in_whitelist(file_path, whitelist)
                    elif whitelist:
                        # Solo mostrar archivos de whitelist con contenido
                        mostrar = path_in_whitelist(file_path, whitelist)
                        mostrar_contenido = mostrar
                    else:
                        # Mostrar todo con contenido
                        mostrar = True
                        mostrar_contenido = True

                    if not mostrar:
                        continue  # No escribir nada para esta ruta

                    out_file.write(f"# Ruta: {file_path}\n")

                    if mostrar_contenido:
                        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                        out_file.write(f"#{'-' * 80}\n")
                        out_file.write(content + "\n\n")
                    else:
                        out_file.write("\n")

                    # Imprime la ruta del fichero guardado o registrado en el archivo
                    print(f"Fichero registrado: {file_path}")
                except Exception as e:
                    print(f"Error al leer {file_path}: {e}")
    print(f"\nArchivo guardado: {output_file}")


if __name__ == "__main__":
    # Uso:
    # python main.py <ruta_del_proyecto> [--only-paths] [--whitelist=ruta1,ruta2,...]
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Uso: python main.py <ruta_del_proyecto> [--only-paths] [--whitelist=ruta1,ruta2,...]")
        sys.exit(1)
    
    PROJECT_PATH = sys.argv[1]
    only_paths = False
    whitelist: Set[str] = set()

    for arg in sys.argv[2:]:
        if arg == "--only-paths":
            only_paths = True
        elif arg.startswith("--whitelist="):
            paths_str = arg[len("--whitelist="):]
            new_paths = set(os.path.normpath(p.strip()) for p in paths_str.split(",") if p.strip())
            whitelist.update(new_paths)
        else:
            print(f"Argumento desconocido: {arg}")
            sys.exit(1)

    if not os.path.isdir(PROJECT_PATH):
        print("Error: La ruta especificada no es un directorio válido.")
        sys.exit(1)

    snapshot_project_content(PROJECT_PATH, only_paths=only_paths, whitelist=whitelist)
