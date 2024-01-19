import PyPDF2
import sys
import os
import shutil

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

    return output

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pdf_files = sys.argv[1:]
        output_path = 'merged_output.pdf'
        merged_pdf = merge_pdfs(pdf_files, output_path)

        # Mover el archivo PDF fusionado al directorio del primer archivo PDF
        first_pdf_directory = os.path.dirname(pdf_files[0])
        shutil.move(merged_pdf, os.path.join(first_pdf_directory, output_path))
    else:
        print("No se han proporcionado archivos PDF para fusionar.")