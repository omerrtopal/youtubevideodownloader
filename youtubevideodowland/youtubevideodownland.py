from tkinter import *
import customtkinter
from tkinter import messagebox
from tkinter import filedialog
import threading
from pytube import YouTube

FONT = ("Corbel", 18, "bold")
FONT1 = ("Corbel", 12, "bold")
OPTIONS = ("Corbel", 15, "bold")
customtkinter.set_appearance_mode("light")

# Main
screen = customtkinter.CTk()
screen.title("YouTube Video Downloader")
screen.minsize(500, 350)


# func
def download_video(link, path, quality):
    try:
        if quality == 1080:
            yt = YouTube(link)
            stream = yt.streams.filter(file_extension="mp4", res="1080p", adaptive=True).first()
            stream.download(path)
        elif quality == 720:
            yt = YouTube(link)
            stream = yt.streams.filter(file_extension="mp4", res="720p", adaptive=True).first()
            stream.download(path)
        elif quality == 480:
            yt = YouTube(link)
            stream = yt.streams.filter(file_extension="mp4", res="480p", adaptive=True).first()
            stream.download(path)
        elif quality == 360:
            yt = YouTube(link)
            stream = yt.streams.filter(file_extension="mp4", res="360p", adaptive=True).first()
            stream.download(path)
        elif quality == 240:
            yt = YouTube(link)
            stream = yt.streams.filter(file_extension="mp4", res="240p", adaptive=True).first()
            stream.download(path)
        elif quality == 1:
            YouTube(link).streams.get_audio_only().download(output_path=path)

        messagebox.showinfo("Başarılı", "İndirme başarıyla tamamlandı.")

    except Exception as e:
        messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")


def indir_button():
    link = youtube_link_entry.get()
    path = youtube_link_entry1.get()
    quality = radio_giris.get()
    if len(link) == 0:
        messagebox.showinfo(title="Uyarı", message="Lütfen Bir Link Giriniz")
    else:
        # İndirme işlemini başka bir iş parçacığında çalıştır
        thread = threading.Thread(target=download_video, args=(link, path, quality))
        thread.start()


def open_file_dialog():
    file_path = filedialog.askdirectory()
    youtube_link_entry1.insert(0, file_path)


# Uİ

youtube_video_downlander_label = customtkinter.CTkLabel(screen, text="Youtube Video Downloader Welcome", font=FONT)
youtube_video_downlander_label.pack()

link_label = customtkinter.CTkLabel(screen, text="Video Link:", fg_color="transparent")
link_label.place(x=26, y=49)

youtube_link_entry = customtkinter.CTkEntry(screen, width=195)
youtube_link_entry.place(x=95, y=50)

youtube_downloader_button = customtkinter.CTkButton(screen, text="İndir", font=FONT1, fg_color="#FF3333",
                                                    text_color="black", command=indir_button)
youtube_downloader_button.place(x=300, y=50)

youtube_link_entry1 = customtkinter.CTkEntry(screen, width=195)
youtube_link_entry1.place(x=95, y=90)

link_label1 = customtkinter.CTkLabel(screen, text="Dosya Yolu:", fg_color="transparent")
link_label1.place(x=23, y=90)

youtube_downloader_button1 = customtkinter.CTkButton(screen, text="Gözat", font=FONT1, fg_color=("#66FF33", "#66FFFF"),
                                                     text_color="black", command=open_file_dialog)
youtube_downloader_button1.place(x=300, y=90)

youtube_video_options_label = customtkinter.CTkLabel(screen,
                                                     text="Lütfen Seçeneklerden Birini "
                                                          "Seçiniz\n"
                                                          "------------------------------------------------------",
                                                     font=OPTIONS)
youtube_video_options_label.place(x=30, y=130)

radio_giris = IntVar()
my_radiobutton = customtkinter.CTkRadioButton(screen, text="1080p", value=1080, variable=radio_giris, )
my_radiobutton1 = customtkinter.CTkRadioButton(screen, text="720p", value=720, variable=radio_giris, )
my_radiobutton2 = customtkinter.CTkRadioButton(screen, text="480p", value=480, variable=radio_giris, )
my_radiobutton3 = customtkinter.CTkRadioButton(screen, text="360p", value=360, variable=radio_giris, )
my_radiobutton4 = customtkinter.CTkRadioButton(screen, text="240p", value=240, variable=radio_giris, )
my_radiobutton5 = customtkinter.CTkRadioButton(screen, text="Sadece Ses", value=1, variable=radio_giris, )
my_radiobutton.place(x=30, y=165)
my_radiobutton1.place(x=30, y=195)
my_radiobutton2.place(x=30, y=225)
my_radiobutton3.place(x=30, y=255)
my_radiobutton4.place(x=30, y=285)
my_radiobutton5.place(x=30, y=315)

screen.mainloop()
