import tkinter as tk
from tkinter import ttk, messagebox
from fuzzy_logic import get_fuzzy_result
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_gui():
    root = tk.Tk()
    root.title("🌿 Akıllı Sera Kontrol Sistemi")
    root.geometry("600x820")  # Yüksekliği artırdık
    root.resizable(False, False)

    # Başlık
    tk.Label(root, text="Akıllı Sera Ortam Kontrolü", font=("Arial", 20, "bold")).pack(pady=10)

    # Ana giriş çerçevesi
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Girdi oluşturucu
    def create_input(label_text, from_, to_, default, step=1):
        tk.Label(frame, text=label_text, font=("Arial", 11)).pack()
        var = tk.Scale(frame, from_=from_, to=to_, orient=tk.HORIZONTAL, length=400, resolution=step)
        var.set(default)
        var.pack(pady=5)
        return var

    temp_input = create_input("🌡️ Hava Sıcaklığı (°C)", 10, 45, 25)
    hum_input = create_input("💧 Nem Oranı (%)", 20, 100, 60)
    hour_input = create_input("⏰ Saat", 0, 24, 12)
    soil_input = create_input("🌱 Toprak Nemliliği (%)", 0, 100, 50)

    # Bitki türü seçimi
    tk.Label(frame, text="🪴 Bitki Türü", font=("Arial", 11)).pack()
    plant_var = tk.StringVar()
    plant_combobox = ttk.Combobox(frame, textvariable=plant_var, state="readonly", width=20, font=("Arial", 10))
    plant_combobox['values'] = ("Kaktüs", "Domates", "Marul")
    plant_combobox.current(1)
    plant_combobox.pack(pady=5)

    # Buton çerçevesi (girdilerin hemen altında, görünürlük iyi)
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    def calculate():
        try:
            temp = temp_input.get()
            hum = hum_input.get()
            hour = hour_input.get()
            soil = soil_input.get()

            plant_map = {"Kaktüs": 1, "Domates": 2, "Marul": 3}
            plant = plant_map.get(plant_var.get(), 2)

            water, fan = get_fuzzy_result(temp, hum, plant, hour, soil)

            result_text = f"💧 Sulama Süresi: {water:.2f} dakika\n💨 Fan Gücü: {fan:.2f} %"
            result_label.config(text=result_text)

            bars[0].set_height(water * 100 / 30)  # normalize
            bars[1].set_height(fan)
            canvas.draw()

        except Exception as e:
            messagebox.showerror("Hata", f"Hesaplama sırasında hata oluştu:\n{e}")

    tk.Button(
        btn_frame,
        text="💾 HESAPLA",
        font=("Arial", 14, "bold"),
        bg="#4CAF50",
        fg="white",
        width=20,
        height=2,
        command=calculate
    ).pack()

    # Sonuç etiketi
    result_label = tk.Label(root, text="", font=("Arial", 13), justify="left", fg="black")
    result_label.pack(pady=10)

    # Grafik
    fig, ax = plt.subplots(figsize=(4, 2))
    bars = ax.bar(["Sulama", "Fan"], [0, 0], color=["blue", "green"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("% / dk", fontsize=10)
    ax.set_title("Çıkış Grafiği", fontsize=12)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=5)

    root.mainloop()
