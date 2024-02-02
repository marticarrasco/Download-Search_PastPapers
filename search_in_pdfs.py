import os
import PyPDF2

def buscar_en_pdfs(texto_a_buscar, directorio_base="Download PP/IB_Papers"):
    encontrados = []
    print(f"Buscando en el directorio: {directorio_base}")

    for root, dirs, files in os.walk(directorio_base):
        for file in files:
            if file.endswith(".pdf"):
                archivo_completo = os.path.join(root, file)
                #print(f"Accediendo al archivo: {archivo_completo}")
                try:
                    with open(archivo_completo, "rb") as f:
                        pdf_reader = PyPDF2.PdfReader(f)
                        for page in pdf_reader.pages:
                            contenido = page.extract_text()
                            if contenido and texto_a_buscar in contenido:
                                encontrados.append(archivo_completo)
                                print(f"Texto encontrado en: {archivo_completo}")
                                break
                except Exception as e:
                    print(f"Error al leer el archivo {archivo_completo}: {e}")

    return encontrados

def main():
    texto_a_buscar = input("Introduce el texto a buscar: ")
    resultados = buscar_en_pdfs(texto_a_buscar)
    if resultados:
        print("Exámenes encontrados que contienen el texto:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron exámenes con el texto especificado.")

if __name__ == "__main__":
    main()
