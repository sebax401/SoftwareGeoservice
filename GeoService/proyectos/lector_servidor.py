import os


def leer_servidor(ruta_servidor):

    if not os.path.exists(ruta_servidor):
        print("❌ La ruta no existe")
        return

    nombre_salida = "estructura_servidor.txt"

    with open(nombre_salida, "w", encoding="utf-8") as archivo_txt:

        archivo_txt.write(
            f"CARPETA PRINCIPAL: {os.path.basename(ruta_servidor)}\n"
        )

        archivo_txt.write("=" * 60 + "\n\n")

        for ruta_actual, carpetas, archivos in os.walk(ruta_servidor):

            nivel = ruta_actual.replace(ruta_servidor, "").count(os.sep)

            espacios = "    " * nivel

            # Mostrar carpeta
            if ruta_actual == ruta_servidor:
                archivo_txt.write(
                    f"{espacios}📁 {os.path.basename(ruta_actual)}\n"
                )
            else:
                archivo_txt.write(
                    f"{espacios}📁 {os.path.basename(ruta_actual)}\n"
                )

            # Mostrar archivos
            for nombre_archivo in archivos:

                archivo_txt.write(
                    f"{espacios}    📄 {nombre_archivo}\n"
                )

    print(f"✅ Estructura guardada en: {nombre_salida}")