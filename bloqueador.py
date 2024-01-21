import tkinter as tk
import re  # Libreria que funciona para buscar cadenas

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

def study_mode(bool):

    with open("paginas.txt", 'r+') as paginas:
        if bool:
            for pagina in paginas:
                bloquear_sitio(pagina.strip())
        else:
            for pagina in paginas:
                desbloquear_sitio(pagina.strip())           


ventana = tk.Tk()
ventana.title('Bloqueador de Sitios')
ventana.geometry('400x200')  # Ancho x Alto

sitio_entry = tk.Entry(ventana, width=50)
sitio_entry.pack(pady=10)

bloquear_button = tk.Button(ventana, text='Bloquear Sitio', command=lambda: bloquear_sitio(sitio_entry.get()))
bloquear_button.pack(pady=5)

desbloquear_button = tk.Button(ventana, text='Desbloquear Sitio', command=lambda: desbloquear_sitio(sitio_entry.get()))
desbloquear_button.pack(pady=5)

study_button_on = tk.Button(ventana , text='Activar modo estudio' , command=lambda : study_mode(True))
study_button_on.pack(pady=5)

study_button_off = tk.Button(ventana , text='Desactivar modo estudio' , command=lambda : study_mode(False))
study_button_off.pack(pady=5)

ventana.mainloop()
