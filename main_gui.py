import tkinter as tk
from tkinter import ttk
import analytics
import matplotlib.pyplot as plt
from database import districts

# =========================================================
# COLORS
# =========================================================
BG = "#dfe7ef"
CARD = "#f7f9fc"
ACCENT = "#4ea8de"
GREEN = "#52b788"
BTN_BORDER = "#2b2d42"

# =========================================================
# DETAILS WINDOW
# =========================================================
def open_details(district):

    win = tk.Toplevel()

    win.title(district["name"])
    win.geometry("340x280")
    win.configure(bg=BG)

    card = tk.Frame(
        win,
        bg=CARD,
        bd=1,
        relief="solid"
    )

    card.pack(
        padx=15,
        pady=15,
        fill="both",
        expand=True
    )

    tk.Label(
        card,
        text=district["name"],
        font=("Arial", 12, "bold"),
        bg=CARD
    ).pack(pady=8)

    tk.Label(
        card,
        text=f"Air Quality: {district['air_quality']} / 10",
        bg=CARD
    ).pack()

    tk.Label(
        card,
        text=f"Traffic Congestion: {district['traffic']} / 10",
        bg=CARD
    ).pack()

    tk.Label(
        card,
        text=f"Infrastructure: {district['infrastructure']} / 10",
        bg=CARD
    ).pack()

    tk.Label(
        card,
        text=f"Population Density: {district['population_density']} / 10",
        bg=CARD
    ).pack()

    tk.Button(
        card,
        text="← Back",
        bg=ACCENT,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=win.destroy
    ).pack(pady=10)


# =========================================================
# TABLE WINDOW
# =========================================================
def open_table():

    win = tk.Toplevel()

    win.title("District Table")
    win.geometry("760x420")
    win.configure(bg=BG)

    cols = (
        "Name",
        "Air",
        "Traffic",
        "Infrastructure",
        "Population"
    )

    style = ttk.Style()

    style.theme_use("default")

    style.configure(
        "Treeview",
        font=("Arial", 10),
        rowheight=25
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 10, "bold")
    )

    tree = ttk.Treeview(
        win,
        columns=cols,
        show="headings"
    )

    for c in cols:
        tree.heading(c, text=c)

    for i, d in enumerate(districts):

        tag = "even" if i % 2 == 0 else "odd"

        tree.insert(
            "",
            tk.END,
            values=(
                d["name"],
                d["air_quality"],
                d["traffic"],
                d["infrastructure"],
                d["population_density"]
            ),
            tags=(tag,)
        )

    tree.tag_configure(
        "even",
        background="#eef2f7"
    )

    tree.tag_configure(
        "odd",
        background="#dbe4ee"
    )

    tree.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    tk.Button(
        win,
        text="← Back",
        bg=GREEN,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=win.destroy
    ).pack(pady=5)


# =========================================================
# GRAPHICS
# =========================================================
def show_graphs():

    names = [d["name"] for d in districts]
    air = [d["air_quality"] for d in districts]
    traffic = [d["traffic"] for d in districts]
    infra = [d["infrastructure"] for d in districts]

    years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

    air_trend = [5.5, 6.8, 7.4, 7.0, 6.6, 6.3, 6.1, 5.9]
    traffic_trend = [7.8, 6.2, 6.8, 7.2, 7.6, 8.0, 8.3, 8.5]
    infra_trend = [5.5, 6.0, 6.5, 6.9, 7.3, 7.6, 7.9, 8.2]

    # =====================================================
    # MAIN FIGURE
    # =====================================================
    fig = plt.figure(figsize=(13, 8))

    fig.patch.set_facecolor("#cfd8e3")

    plt.suptitle(
        "Almaty Smart City Analytics",
        fontsize=15,
        fontweight="bold",
        color="#1d3557"
    )

    # =====================================================
    # GRAPH 1
    # =====================================================
    ax1 = plt.subplot(2, 2, 1)

    ax1.set_facecolor("#eef2f7")

    plt.plot(
        years,
        air_trend,
        color="#8ecae6",
        linewidth=2,
        label="Air Quality"
    )

    plt.plot(
        years,
        traffic_trend,
        color="#f4a261",
        linewidth=2,
        label="Traffic"
    )

    plt.plot(
        years,
        infra_trend,
        color="#90be6d",
        linewidth=2,
        label="Infrastructure"
    )

    plt.title(
        "City Trends Over Time",
        fontsize=12,
        fontweight="bold",
        color="#1d3557"
    )

    plt.xlabel("Years")
    plt.ylabel("Index")

    plt.legend()

    plt.grid(alpha=0.3)

    # =====================================================
    # GRAPH 2
    # =====================================================
    ax2 = plt.subplot(2, 2, 2)

    ax2.set_facecolor("#eef2f7")

    air_colors = []

    for v in air:

        if v >= 8:
            air_colors.append("#1c8958")

        elif v >= 7:
            air_colors.append("#68cf9f")

        elif v >= 6:
            air_colors.append("#95d5b2")

        elif v >= 5:
            air_colors.append("#dfbb67")

        elif v >= 4:
            air_colors.append("#e39168")

        else:
            air_colors.append("#e6603f")

    plt.bar(
        names,
        air,
        color=air_colors
    )

    plt.title(
        "Air Quality by District",
        fontsize=12,
        fontweight="bold",
        color="#1d3557"
    )

    plt.xlabel("Districts")
    plt.ylabel("Air Quality")

    plt.xticks(rotation=45)

    # =====================================================
    # GRAPH 3
    # =====================================================
    ax3 = plt.subplot(2, 2, 3)

    ax3.set_facecolor("#eef2f7")

    traffic_colors = []

    for v in traffic:

        if v <= 5:
            traffic_colors.append("#329c6c")

        elif v <= 6:
            traffic_colors.append("#97efc3")

        elif v <= 7:
            traffic_colors.append("#f0cf82")

        elif v <= 8:
            traffic_colors.append("#ea834f")

        else:
            traffic_colors.append("#cb6349")

    plt.bar(
        names,
        traffic,
        color=traffic_colors
    )

    plt.title(
        "Traffic Congestion Levels",
        fontsize=12,
        fontweight="bold",
        color="#1d3557"
    )

    plt.xlabel("Districts")
    plt.ylabel("Traffic")

    plt.xticks(rotation=45)

    # =====================================================
    # GRAPH 4
    # =====================================================
    ax4 = plt.subplot(2, 2, 4)

    ax4.set_facecolor("#eef2f7")

    district_colors = [
        "#88bfef",
        "#b264df",
        "#e76e9a",
        "#679c9d",
        "#85e092",
        "#eacf89",
        "#7d5576",
        "#71966a"
    ]

    total = sum(infra)

    infra_percent = [
        x / total * 100 for x in infra
    ]

    plt.pie(
        infra_percent,
        labels=names,
        colors=district_colors,
        autopct="%1.1f%%",
        startangle=140
    )

    plt.title(
        "Infrastructure Distribution",
        fontsize=12,
        fontweight="bold",
        color="#1d3557"
    )

    plt.tight_layout()
    plt.show()


# =========================================================
# LIST + SEARCH + FILTER + MODE
# =========================================================
def show_all():

    listbox.delete(0, tk.END)

    for d in districts:
        listbox.insert(tk.END, d["name"])


def on_select(event):

    if not listbox.curselection():
        return

    name = listbox.get(listbox.curselection()[0])

    for d in districts:

        if d["name"] == name:
            open_details(d)
            return


def search_district():

    name = search_entry.get().lower()

    listbox.delete(0, tk.END)

    found = False

    for d in districts:

        if name in d["name"].lower():
            listbox.insert(tk.END, d["name"])
            found = True

    if not found:
        listbox.insert(tk.END, "Not found")


def apply_filter(): # фильтрую данные выводятся лучшие

    listbox.delete(0, tk.END)

    filtered = districts.copy()

    if air_var.get():
        filtered = [
            d for d in filtered
            if d["air_quality"] >= 7
        ]

    if traffic_var.get():
        filtered = [
            d for d in filtered
            if d["traffic"] <= 7
        ]

    if infra_var.get():
        filtered = [
            d for d in filtered
            if d["infrastructure"] >= 7
        ]

    for d in filtered:
        listbox.insert(tk.END, d["name"])


def reset_filter():

    air_var.set(0)
    traffic_var.set(0)
    infra_var.set(0)

    show_all()


def set_mode(): 

    mode = mode_var.get()

    listbox.delete(0, tk.END)

    if mode == "air":

        data = sorted(
            districts,
            key=lambda x: x["air_quality"], # сортировка районов по воздкхк и тд
            reverse=True
        )

        for d in data:
            listbox.insert(
                tk.END,
                f"{d['name']} — {d['air_quality']}/10"
            )

    elif mode == "traffic":

        data = sorted(
            districts,
            key=lambda x: x["traffic"]
        )

        for d in data:
            listbox.insert(
                tk.END,
                f"{d['name']} — {d['traffic']}/10"
            )

    else:

        data = sorted(
            districts,
            key=lambda x: x["infrastructure"],
            reverse=True
        )

        for d in data:
            listbox.insert(
                tk.END,
                f"{d['name']} — {d['infrastructure']}/10"
            )


# =========================================================
# DASHBOARD
# =========================================================
def open_dashboard():

    win = tk.Toplevel()

    win.title("Smart City Dashboard")
    win.geometry("500x420")
    win.configure(bg=BG)

    air_avg, air_max, air_min = analytics.get_air_stats()
    traffic_avg, traffic_max, traffic_min = analytics.get_traffic_stats()
    infra_avg, infra_max, infra_min = analytics.get_infra_stats()

    tk.Label(
        win,
        text="SMART CITY DASHBOARD",
        bg=BG,
        font=("Arial", 13, "bold")
    ).pack(pady=10)

    tk.Label(
        win,
        text=f"Air Avg: {air_avg:.1f} | Max: {air_max} | Min: {air_min}",
        bg=BG
    ).pack()

    tk.Label(
        win,
        text=f"Traffic Avg: {traffic_avg:.1f} | Max: {traffic_max} | Min: {traffic_min}",
        bg=BG
    ).pack()

    tk.Label(
        win,
        text=f"Infrastructure Avg: {infra_avg:.1f} | Max: {infra_max} | Min: {infra_min}",
        bg=BG
    ).pack()

    tk.Button(
        win,
        text="Graphs",
        bg=ACCENT,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=show_graphs
    ).pack(pady=10)

    tk.Button(
        win,
        text="Table View",
        bg=GREEN,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=open_table
    ).pack(pady=5)

    tk.Button(
        win,
        text="← Back",
        bg="#999",
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=win.destroy
    ).pack(pady=10)


# =========================================================
# MAIN UI
# =========================================================
def open_main():

    welcome.destroy()

    main = tk.Tk()

    main.title("Smart City - Almaty")
    main.geometry("900x600")
    main.configure(bg=BG)

    tk.Label(
        main,
        text="Smart City System",
        bg=BG,
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    top = tk.Frame(main, bg=BG)
    top.pack()

    tk.Button(
        top,
        text="Dashboard",
        bg=ACCENT,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=open_dashboard
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        top,
        text="Show All",
        bg=GREEN,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=show_all
    ).grid(row=0, column=1, padx=5)

    search_frame = tk.Frame(main, bg=BG)
    search_frame.pack(pady=5)

    global search_entry

    search_entry = tk.Entry(
        search_frame,
        width=25
    )

    search_entry.grid(row=0, column=0)

    tk.Button(
        search_frame,
        text="Search",
        bg=ACCENT,
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=search_district
    ).grid(row=0, column=1, padx=5)

    left_panel = tk.Frame(main, bg=BG)

    left_panel.pack(
        side="left",
        padx=10,
        pady=10,
        anchor="n"
    )

    filter_frame = tk.LabelFrame(
        left_panel,
        text="Filters",
        bg=BG
    )

    filter_frame.pack(pady=10)

    global air_var, traffic_var, infra_var

    air_var = tk.IntVar()
    traffic_var = tk.IntVar()
    infra_var = tk.IntVar()

    tk.Checkbutton(
        filter_frame,
        text="Good Air Quality",
        variable=air_var
    ).pack(anchor="w")

    tk.Checkbutton(
        filter_frame,
        text="Low Traffic",
        variable=traffic_var
    ).pack(anchor="w")

    tk.Checkbutton(
        filter_frame,
        text="Good Infrastructure",
        variable=infra_var
    ).pack(anchor="w")

    tk.Button(
        filter_frame,
        text="Apply",
        command=apply_filter,
        bg="#cccccc",
        fg="black",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER
    ).pack()

    tk.Button(
        filter_frame,
        text="Reset",
        command=reset_filter,
        bg="#bbbbbb",
        fg="black",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER
    ).pack()

    mode_frame = tk.LabelFrame(
        left_panel,
        text="Analysis Mode",
        bg=BG
    )

    mode_frame.pack(pady=10)

    global mode_var

    mode_var = tk.StringVar(value="air")

    tk.Radiobutton(
        mode_frame,
        text="Air",
        variable=mode_var,
        value="air",
        command=set_mode
    ).pack(anchor="w")

    tk.Radiobutton(
        mode_frame,
        text="Traffic",
        variable=mode_var,
        value="traffic",
        command=set_mode
    ).pack(anchor="w")

    tk.Radiobutton(
        mode_frame,
        text="Infrastructure",
        variable=mode_var,
        value="infra",
        command=set_mode
    ).pack(anchor="w")

    global listbox

    listbox = tk.Listbox(
        main,
        height=18,
        width=85
    )

    listbox.pack(pady=10)

    listbox.bind("<<ListboxSelect>>", on_select)

    show_all()

    tk.Button(
        main,
        text="← Back",
        bg="#999",
        fg="white",
        bd=1,
        relief="solid",
        highlightbackground=BTN_BORDER,
        command=main.destroy
    ).pack(pady=15)


# =========================================================
# WELCOME WINDOW
# =========================================================
welcome = tk.Tk()

welcome.title("Welcome")
welcome.geometry("900x600")
welcome.configure(bg=BG)

card = tk.Frame(
    welcome,
    bg=CARD,
    bd=1,
    relief="solid"
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=320,
    height=220
)

tk.Label(
    card,
    text="SMART CITY",
    font=("Arial", 18, "bold"),
    bg=CARD
).pack(pady=10)

tk.Label(
    card,
    text="Almaty District Analytics",
    bg=CARD
).pack()

tk.Label(
    card,
    text="Data • Analysis • Visualization",
    bg=CARD,
    fg="#666"
).pack(pady=5)

tk.Button(
    card,
    text="START",
    width=18,
    bg=ACCENT,
    fg="white",
    bd=1,
    relief="solid",
    highlightbackground=BTN_BORDER,
    command=open_main
).pack(pady=18)

welcome.mainloop()