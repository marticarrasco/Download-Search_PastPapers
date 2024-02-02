import requests
import os

def download_ib_papers(start_year=2000, end_year=2021):
    base_url = "https://gateway.tor2web.ibhaven.st/resources/ibdocuments-original/IB%20PAST%20PAPERS%20-%20SUBJECT/Group%204%20-%20Sciences/Computer_science_SL/"
    sessions = ["May", "November"]
    error_log = []

    for year in range(start_year, end_year + 1):
        for session in sessions:
            # Crear la carpeta para cada año y sesión
            folder_path = f"IB_Papers/{year}_{session}"
            os.makedirs(folder_path, exist_ok=True)

            # Descargar el examen y su corrección
            exam_url = f"{base_url}{year}%20{session}%20Examination%20Session/Computer_science_paper_1__SL_Spanish.pdf"
            markscheme_url = f"{base_url}{year}%20{session}%20Examination%20Session/Computer_science_paper_1__SL_markscheme.pdf"

            try:
                # Descargar el examen
                exam_response = requests.get(exam_url)
                if exam_response.status_code == 200:
                    with open(f"{folder_path}/Examen.pdf", "wb") as file:
                        file.write(exam_response.content)
                else:
                    error_log.append(f"Error al descargar el examen de {year} {session}: Código de estado {exam_response.status_code}")

                # Descargar la corrección
                markscheme_response = requests.get(markscheme_url)
                if markscheme_response.status_code == 200:
                    with open(f"{folder_path}/Correccion.pdf", "wb") as file:
                        file.write(markscheme_response.content)
                else:
                    error_log.append(f"Error al descargar la corrección de {year} {session}: Código de estado {markscheme_response.status_code}")

            except Exception as e:
                error_log.append(f"Error al procesar {year} {session}: {e}")

    # Escribir el log de errores si hay errores
    if error_log:
        with open("IB_Papers/error_log.txt", "w") as log_file:
            for error in error_log:
                log_file.write(error + "\n")

    return "Descarga completada con errores registrados en 'error_log.txt'" if error_log else "Descarga completada sin errores"

download_ib_papers()