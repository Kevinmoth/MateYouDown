from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import ttk

def descargar_audio():
    url = url_entry.get()

    try:
        video = YouTube(url)
        titulo_video = video.title
        audio = video.streams.filter(only_audio=True).first()

        # Barra de carga ez (en realidad no indica nada, pero queda bien op)
        progress_bar['value'] = 20
        root.update_idletasks()

        audio.download(filename=f"{titulo_video}.mp3")
a
        progress_bar['value'] = 100
        messagebox.showinfo("Descarga completada!", "El audio descargo correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error!: {e}")

def descargar_video():
    url = url_entry.get()

    try:
        video = YouTube(url)
        titulo_video = video.title
        video.streams.get_highest_resolution().download(filename=f"{titulo_video}.mp4")
        progress_bar['value'] = 100
        messagebox.showinfo("Descarga completada", "El video se descargo correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = Tk()
root.title("MateYouDown 😀🎵🎥")
root.geometry("420x180") 
root.resizable(False, False)

url_label = Label(root, text="Ingresa la URL del video:", anchor="center")
url_label.grid(row=0, column=0, padx=(10, 5), pady=(15, 5), columnspan=2, sticky=W + E)

url_entry = Entry(root, width=40)
url_entry.grid(row=1, column=0, padx=(10, 5), pady=5, columnspan=2, sticky=W + E)

audio_button = Button(root, text="Descargar Audio 🎵", command=descargar_audio)
audio_button.grid(row=2, column=0, padx=10, pady=10, sticky=W + E)

video_button = Button(root, text="Descargar Video 🎥", command=descargar_video)
video_button.grid(row=2, column=1, padx=(5, 10), pady=10, sticky=W + E)

style = ttk.Style()
style.theme_use('clam')
style.configure("Horizontal.TProgressbar", thickness=3)
progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, length=380, mode='determinate', style="Horizontal.TProgressbar")
progress_bar.grid(row=3, columnspan=2, padx=10, pady=10)


root.mainloop()
