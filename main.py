import PyPDF2
from tkinter import filedialog
from tkinter import Tk

def selecionar_arquivos_pdf():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    file_paths = filedialog.askopenfilenames(title="Selecione os arquivos PDF", filetypes=[("PDF files", "*.pdf")])
    return root.tk.splitlist(file_paths)

def juntar_pdfs(output_path, pdf_paths):
    pdf_writer = PyPDF2.PdfMerger()

    for pdf in pdf_paths:
        with open(pdf, 'rb') as f:
            pdf_writer.append(f)
    
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    arquivos_pdf = selecionar_arquivos_pdf()
    if arquivos_pdf:
        caminho_saida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], title="Salvar arquivo PDF combinado")
        if caminho_saida:
            juntar_pdfs(caminho_saida, arquivos_pdf)
            print(f"PDFs combinados com sucesso em {caminho_saida}")
