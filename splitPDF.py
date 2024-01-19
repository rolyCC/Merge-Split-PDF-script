import PyPDF2
import sys
import os
import shutil

def split_pdf(path, output_folder):
    pdf_reader = PyPDF2.PdfReader(path)
    for page in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page])

        output_filename = os.path.join(output_folder, f'page_{page + 1}.pdf')

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        pdf_file = sys.argv[1]
        output_folder = os.path.dirname(pdf_file)
        split_pdf(pdf_file, output_folder)
    else:
        print("Por favor, proporciona un archivo PDF para dividir.")