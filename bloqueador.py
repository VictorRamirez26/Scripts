import tkinter as tk
import re  # Libreria que funciona para buscar cadenas
from tkinter import filedialog

def bloquear_sitio(sitio):
    variantes_sitio = [sitio, 'https://' + sitio, 'www.' + sitio]
    with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as archivo_hosts:
        contenido = archivo_hosts.read()
        for variante in variantes_sitio:
            if not re.search(rf'\b{variante}\b', contenido):
                archivo_hosts.write('127.0.0.1 ' + variante + '\n')

def desbloquear_sitio(sitio):
    variantes_sitio = [sitio, 'https://' + sitio, 'www.' + sitio]
    with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+') as archivo_hosts:
        lineas = archivo_hosts.readlines()
        archivo_hosts.seek(0)
        archivo_hosts.truncate()
        for linea in lineas:
            if not any(variante in linea for variante in variantes_sitio):
                archivo_hosts.write(linea)
 

def abrir_archivo(bool):
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo",filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as archivo:
            for pagina in archivo:
                if bool:
                    bloquear_sitio(pagina.strip())
                else:
                    desbloquear_sitio(pagina.strip())


ventana = tk.Tk()
ventana.title('Bloqueador de Sitios')
ventana.geometry('600x400')  # Ancho x Alto

sitio_entry = tk.Entry(ventana, width=50)
sitio_entry.pack(pady=10)

bloquear_button = tk.Button(ventana, text='Bloquear Sitio', command=lambda: bloquear_sitio(sitio_entry.get()))
bloquear_button.pack(pady=5)

desbloquear_button = tk.Button(ventana, text='Desbloquear Sitio', command=lambda: desbloquear_sitio(sitio_entry.get()))
desbloquear_button.pack(pady=5)


bloquear_archivo = tk.Button(ventana, text='Importar paginas (Para Bloquear)', command=lambda : abrir_archivo(True))
bloquear_archivo.pack(pady=5)

desbloquear_archivo = tk.Button(ventana, text='Importar paginas (Para Desbloquear)', command=lambda : abrir_archivo(False))
desbloquear_archivo.pack(pady=5)

ventana.mainloop()