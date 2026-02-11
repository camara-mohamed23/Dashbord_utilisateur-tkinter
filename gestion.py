import tkinter as tk
from tkinter import ttk

BG = "#edf1f7"
SIDEBAR_BG = "#142949"
CARD_BG = "#ffffff"
PRIMARY = "#0e3b70"
ACCENT = "#f7a600"
TEXT = "#111111"
SUB = "#7b8ba5"

root = tk.Tk()
root.title("User Dashboard")
root.geometry("1100x600")
root.configure(bg=BG)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# ---------- SIDEBAR ----------
sidebar = tk.Frame(root, bg=SIDEBAR_BG, width=220)
sidebar.grid(row=0, column=0, sticky="nsw")
sidebar.grid_propagate(False)

# Profil rond (placeholder)
avatar_wrap = tk.Frame(sidebar, bg=SIDEBAR_BG)
avatar_wrap.pack(pady=30)
avatar = tk.Canvas(avatar_wrap, width=80, height=80,
                   bg=SIDEBAR_BG, highlightthickness=0)
avatar.pack()
avatar.create_oval(5, 5, 75, 75, fill=PRIMARY, outline=PRIMARY)

tk.Label(sidebar, text="JOHN DON", bg=SIDEBAR_BG,
         fg="white", font=("Segoe UI", 12, "bold")).pack()
tk.Label(sidebar, text="johndon@company.com", bg=SIDEBAR_BG,
         fg="#c5d1e5", font=("Segoe UI", 9)).pack(pady=(4, 20))

menu = tk.Frame(sidebar, bg=SIDEBAR_BG)
menu.pack(fill="x", padx=30)

for item in ["home", "file", "messages", "notification",
             "location", "graph"]:
    tk.Label(menu, text=item, bg=SIDEBAR_BG, fg="#c5d1e5",
             font=("Segoe UI", 10)).pack(anchor="w", pady=4)

# ---------- ZONE PRINCIPALE ----------
main = tk.Frame(root, bg=BG)
main.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
main.grid_columnconfigure((0, 1, 2, 3), weight=1)

header = tk.Frame(main, bg=BG)
header.grid(row=0, column=0, columnspan=4, sticky="ew", pady=(0, 10))
tk.Label(header, text="Dashboard User", bg=BG,
         fg=TEXT, font=("Segoe UI", 16, "bold")).pack(side="left")

# ---------- CARTES DE STATS ----------
def stat_card(col, title, value):
    c = tk.Frame(main, bg=CARD_BG)
    c.grid(row=1, column=col, padx=8, pady=8, sticky="nsew")
    tk.Label(c, text=title, bg=CARD_BG, fg=SUB,
             font=("Segoe UI", 9)).pack(anchor="w", padx=12, pady=(10, 0))
    tk.Label(c, text=value, bg=CARD_BG, fg=TEXT,
             font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=12, pady=(4, 10))
    return c

stat_card(0, "Earning", "$ 628")
stat_card(1, "Share", "2434")
stat_card(2, "Likes", "1259")
stat_card(3, "Rating", "8.5")

# ---------- GRAPHIQUE BARRES (placeholder) ----------
result_card = tk.Frame(main, bg=CARD_BG)
result_card.grid(row=2, column=0, columnspan=3, padx=8, pady=8, sticky="nsew")

top_r = tk.Frame(result_card, bg=CARD_BG)
top_r.pack(fill="x", padx=12, pady=(8, 0))
tk.Label(top_r, text="Result", bg=CARD_BG, fg=TEXT,
         font=("Segoe UI", 11, "bold")).pack(side="left")
tk.Button(top_r, text="Check now", bg=ACCENT, fg="white",
          bd=0, padx=12, pady=4,
          font=("Segoe UI", 9, "bold")).pack(side="right")

canvas_bar = tk.Canvas(result_card, bg=BG, height=140,
                       highlightthickness=0)
canvas_bar.pack(fill="both", expand=True, padx=12, pady=10)

# quelques barres factices
for i in range(12):
    x0 = 20 + i * 30
    x1 = x0 + 18
    h = 40 + (i % 5) * 12
    canvas_bar.create_rectangle(x0, 120 - h, x1, 120,
                                fill=PRIMARY, outline=PRIMARY)

# ---------- COURBE + MINI-CALENDRIER (placeholders) ----------
bottom_card = tk.Frame(main, bg=CARD_BG)
bottom_card.grid(row=3, column=0, columnspan=3,
                 padx=8, pady=8, sticky="nsew")

canvas_wave = tk.Canvas(bottom_card, bg=BG, height=120,
                        highlightthickness=0)
canvas_wave.pack(fill="both", expand=True, padx=12, pady=10)
canvas_wave.create_line(10, 80, 80, 60, 160, 90, 240, 50,
                        320, 70, 400, 40, smooth=True, fill=ACCENT, width=3)

# ---------- JAUGE CIRCULAIRE DROITE ----------
gauge_card = tk.Frame(main, bg=CARD_BG, width=200)
gauge_card.grid(row=2, column=3, rowspan=2, padx=8, pady=8, sticky="nsew")
gauge_card.grid_propagate(False)

tk.Label(gauge_card, text="Progress", bg=CARD_BG,
         fg=TEXT, font=("Segoe UI", 11, "bold")).pack(pady=(10, 0))

g_canvas = tk.Canvas(gauge_card, width=120, height=120,
                     bg=CARD_BG, highlightthickness=0)
g_canvas.pack(pady=5)
g_canvas.create_oval(10, 10, 110, 110, outline="#e2e6f0", width=12)
g_canvas.create_arc(10, 10, 110, 110, start=90, extent=-162,
                    outline=ACCENT, style="arc", width=12)
g_canvas.create_text(60, 60, text="45%", fill=TEXT,
                     font=("Segoe UI", 12, "bold"))

for txt in ["Lorem ipsum", "Lorem ipsum", "Lorem ipsum", "Lorem ipsum"]:
    tk.Label(gauge_card, text=txt, bg=CARD_BG,
             fg=SUB, font=("Segoe UI", 9)).pack(anchor="w", padx=20)

tk.Button(gauge_card, text="Check now", bg=ACCENT, fg="white",
          bd=0, padx=14, pady=5,
          font=("Segoe UI", 9, "bold")).pack(pady=10)

root.mainloop()
