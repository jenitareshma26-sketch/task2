import tkinter as tk
from tkinter import messagebox


# ============================================================
# DIGITAL DETECTIVE
# A Tkinter Mystery Investigation Game
# ============================================================

root = tk.Tk()
root.title("Digital Detective")
root.geometry("950x650")
root.resizable(False, False)
root.configure(bg="#0F172A")


# ============================================================
# GAME VARIABLES
# ============================================================

current_case = 1
score = 0
solved_cases = []


# ============================================================
# COLORS
# ============================================================

BG = "#0F172A"
PANEL = "#1E293B"
PANEL2 = "#334155"
GOLD = "#FACC15"
WHITE = "#F8FAFC"
TEXT = "#CBD5E1"
BLUE = "#2563EB"
GREEN = "#22C55E"
RED = "#EF4444"


# ============================================================
# CLEAR SCREEN
# ============================================================

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# ============================================================
# TITLE
# ============================================================

def create_title(title, subtitle=""):
    tk.Label(
        root,
        text=title,
        font=("Arial", 28, "bold"),
        bg=BG,
        fg=GOLD
    ).pack(pady=(20, 5))

    if subtitle:
        tk.Label(
            root,
            text=subtitle,
            font=("Arial", 12),
            bg=BG,
            fg=TEXT
        ).pack(pady=(0, 15))


# ============================================================
# HOME SCREEN
# ============================================================

def home_screen():

    clear_screen()

    create_title(
        "🕵 DIGITAL DETECTIVE",
        "Solve mysteries. Collect evidence. Catch the culprit."
    )

    # Case panel
    panel = tk.Frame(root, bg=PANEL, padx=30, pady=20)
    panel.pack(padx=80, pady=15, fill="x")

    tk.Label(
        panel,
        text="CASE FILES",
        font=("Arial", 18, "bold"),
        bg=PANEL,
        fg=WHITE
    ).pack(pady=(0, 15))

    cases = [
        ("CASE 1", "The Missing Project", "📁"),
        ("CASE 2", "The Stolen Phone", "📱"),
        ("CASE 3", "The Secret Hacker", "💻"),
        ("CASE 4", "The Fake Email", "📧"),
        ("CASE 5", "The Final Mystery", "🔐")
    ]

    for i, (number, name, icon) in enumerate(cases, start=1):

        if i == 1 or i in solved_cases or i == current_case:
            state = "normal"
            bg_color = BLUE

            if i in solved_cases:
                text = f"✓ {number}  {icon} {name}  — SOLVED"
                bg_color = GREEN
            else:
                text = f"{number}  {icon} {name}"

            command = lambda case=i: start_case(case)

        else:
            state = "disabled"
            bg_color = PANEL2
            text = f"🔒 {number}  {icon} {name}"
            command = None

        button = tk.Button(
            panel,
            text=text,
            command=command,
            state=state,
            width=48,
            height=2,
            font=("Arial", 11, "bold"),
            bg=bg_color,
            fg=WHITE,
            disabledforeground="#64748B",
            relief="flat"
        )

        button.pack(pady=5)

    # Score
    tk.Label(
        root,
        text=f"⭐ Detective Score: {score}",
        font=("Arial", 15, "bold"),
        bg=BG,
        fg=GOLD
    ).pack(pady=15)

    tk.Button(
        root,
        text="EXIT GAME",
        command=root.destroy,
        width=15,
        font=("Arial", 10, "bold")
    ).pack()


# ============================================================
# START CASE
# ============================================================

def start_case(case_number):

    global current_case

    current_case = case_number

    if case_number == 1:
        case1()

    elif case_number == 2:
        case2()

    elif case_number == 3:
        case3()

    elif case_number == 4:
        case4()

    elif case_number == 5:
        case5()


# ============================================================
# CASE 1
# ============================================================

def case1():

    clear_screen()

    create_title(
        "CASE #001 — THE MISSING PROJECT",
        "📁 A confidential project has disappeared."
    )

    story = (
        "A project file called Project_Final.pdf disappeared from\n"
        "Computer #3 in the college computer laboratory.\n\n"
        "The file was last accessed between 5:25 PM and 5:35 PM.\n"
        "Three students were connected to the investigation."
    )

    tk.Label(
        root,
        text=story,
        font=("Arial", 13),
        bg=BG,
        fg=TEXT,
        justify="center"
    ).pack(pady=20)

    tk.Button(
        root,
        text="🔍 EXAMINE CLUES",
        command=case1_clues,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="👥 VIEW SUSPECTS",
        command=case1_suspects,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="💻 COMPUTER LOG",
        command=case1_logs,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="⚖ SOLVE CASE",
        command=case1_answer,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=15)

    tk.Button(
        root,
        text="⬅ CASE FILES",
        command=home_screen
    ).pack()


def case1_clues():

    messagebox.showinfo(
        "Evidence Found",
        "🔑 CLUE 1\n\n"
        "A USB drive was found near Computer #3.\n\n"
        "💡 The USB may have been used to copy the project."
    )

    messagebox.showinfo(
        "Evidence Found",
        "🕒 CLUE 2\n\n"
        "The project was copied at exactly 5:31 PM."
    )

    messagebox.showinfo(
        "Evidence Found",
        "🔐 CLUE 3\n\n"
        "Computer #3 was unlocked using Maya's student ID."
    )


def case1_suspects():

    messagebox.showinfo(
        "Suspect: Alex",
        "Alex was working on the project earlier.\n"
        "He left the laboratory at 5:15 PM."
    )

    messagebox.showinfo(
        "Suspect: Maya",
        "Maya entered the laboratory at 5:25 PM.\n"
        "Her student ID unlocked Computer #3."
    )

    messagebox.showinfo(
        "Suspect: Rahul",
        "Rahul claims that he never entered the laboratory."
    )


def case1_logs():

    messagebox.showinfo(
        "Computer #3 — System Log",
        "5:10 PM → Computer turned ON\n"
        "5:12 PM → Alex logged in\n"
        "5:15 PM → Alex left\n"
        "5:25 PM → Maya entered\n"
        "5:28 PM → USB connected\n"
        "5:31 PM → Project_Final.pdf copied\n"
        "5:35 PM → Maya logged out"
    )


def case1_answer():

    ask_answer(
        "CASE #001",
        "Who stole the project file?",
        ["Alex", "Maya", "Rahul"],
        "Maya",
        100,
        case_solved
    )


# ============================================================
# CASE 2
# ============================================================

def case2():

    clear_screen()

    create_title(
        "CASE #002 — THE STOLEN PHONE",
        "📱 A phone disappeared during lunch break."
    )

    story = (
        "A student's phone disappeared from Classroom 204.\n\n"
        "The owner left the phone on the desk at 12:30 PM.\n"
        "When she returned at 12:50 PM, it was gone.\n\n"
        "Three students were nearby."
    )

    tk.Label(
        root,
        text=story,
        font=("Arial", 13),
        bg=BG,
        fg=TEXT,
        justify="center"
    ).pack(pady=20)

    tk.Button(
        root,
        text="🔍 EXAMINE CLUES",
        command=case2_clues,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="👥 INVESTIGATE SUSPECTS",
        command=case2_suspects,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="🕒 CHECK TIMELINE",
        command=case2_timeline,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="⚖ SOLVE CASE",
        command=case2_answer,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=15)

    tk.Button(
        root,
        text="⬅ CASE FILES",
        command=home_screen
    ).pack()


def case2_clues():

    messagebox.showinfo(
        "Clue 1",
        "🎧 A witness saw someone wearing black headphones\n"
        "near the classroom at 12:40 PM."
    )

    messagebox.showinfo(
        "Clue 2",
        "📱 The phone's last Bluetooth connection was detected\n"
        "near the library."
    )

    messagebox.showinfo(
        "Clue 3",
        "👣 A student was seen walking from Classroom 204\n"
        "towards the library at 12:42 PM."
    )


def case2_suspects():

    messagebox.showinfo(
        "Alex",
        "Alex says he was in the cafeteria from 12:30 PM."
    )

    messagebox.showinfo(
        "Maya",
        "Maya says she was studying in the library."
    )

    messagebox.showinfo(
        "Rahul",
        "Rahul says he was in Classroom 204 at 12:40 PM."
    )


def case2_timeline():

    messagebox.showinfo(
        "Timeline",
        "12:30 PM → Phone left on desk\n"
        "12:35 PM → Alex went to cafeteria\n"
        "12:40 PM → Person seen near classroom\n"
        "12:42 PM → Phone moved toward library\n"
        "12:50 PM → Phone reported missing"
    )


def case2_answer():

    ask_answer(
        "CASE #002",
        "Who stole the phone?",
        ["Alex", "Maya", "Rahul"],
        "Rahul",
        100,
        case_solved
    )


# ============================================================
# CASE 3
# ============================================================

def case3():

    clear_screen()

    create_title(
        "CASE #003 — THE SECRET HACKER",
        "💻 Someone accessed the college server."
    )

    story = (
        "The college server detected an unauthorized login.\n\n"
        "The hacker accessed a restricted folder at 2:17 AM.\n"
        "Your task is to determine which account was compromised."
    )

    tk.Label(
        root,
        text=story,
        font=("Arial", 13),
        bg=BG,
        fg=TEXT,
        justify="center"
    ).pack(pady=20)

    tk.Button(
        root,
        text="💻 SERVER LOGS",
        command=case3_logs,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="🌐 IP EVIDENCE",
        command=case3_ip,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="👥 SUSPECTS",
        command=case3_suspects,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="⚖ SOLVE CASE",
        command=case3_answer,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=15)

    tk.Button(
        root,
        text="⬅ CASE FILES",
        command=home_screen
    ).pack()


def case3_logs():

    messagebox.showinfo(
        "Server Log",
        "SERVER ACCESS LOG\n\n"
        "01:58 AM → Failed login\n"
        "02:03 AM → Failed login\n"
        "02:15 AM → Successful login\n"
        "02:17 AM → Restricted folder accessed\n"
        "02:22 AM → File downloaded\n"
        "02:25 AM → Session terminated"
    )


def case3_ip():

    messagebox.showinfo(
        "IP Evidence",
        "Suspicious IP: 192.168.10.45\n\n"
        "The IP belongs to a computer in the\n"
        "college computer laboratory."
    )


def case3_suspects():

    messagebox.showinfo(
        "Alex",
        "Alex uses Computer Lab #1."
    )

    messagebox.showinfo(
        "Maya",
        "Maya uses Computer Lab #2."
    )

    messagebox.showinfo(
        "Rahul",
        "Rahul uses Computer Lab #3.\n"
        "Computer Lab #3 contains IP 192.168.10.45."
    )


def case3_answer():

    ask_answer(
        "CASE #003",
        "Who is responsible for the unauthorized access?",
        ["Alex", "Maya", "Rahul"],
        "Rahul",
        100,
        case_solved
    )


# ============================================================
# CASE 4
# ============================================================

def case4():

    clear_screen()

    create_title(
        "CASE #004 — THE FAKE EMAIL",
        "📧 A suspicious scholarship email has been reported."
    )

    story = (
        "Several students received an email claiming to offer\n"
        "a ₹50,000 scholarship.\n\n"
        "The email asks students to click a link and enter\n"
        "their college login credentials."
    )

    tk.Label(
        root,
        text=story,
        font=("Arial", 13),
        bg=BG,
        fg=TEXT,
        justify="center"
    ).pack(pady=20)

    tk.Button(
        root,
        text="📧 EXAMINE EMAIL",
        command=case4_email,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="🔗 CHECK LINK",
        command=case4_link,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="🔍 FIND RED FLAGS",
        command=case4_flags,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=8)

    tk.Button(
        root,
        text="⚖ SOLVE CASE",
        command=case4_answer,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=15)

    tk.Button(
        root,
        text="⬅ CASE FILES",
        command=home_screen
    ).pack()


def case4_email():

    messagebox.showinfo(
        "Suspicious Email",
        "FROM:\n"
        "scholarship@college-support-example.com\n\n"
        "SUBJECT:\n"
        "Congratulations! You have won ₹50,000!\n\n"
        "MESSAGE:\n"
        "Click the link immediately and verify your\n"
        "college username and password."
    )


def case4_link():

    messagebox.showinfo(
        "Link Analysis",
        "The link does NOT point to the official\n"
        "college website.\n\n"
        "⚠ This is a major phishing warning."
    )


def case4_flags():

    messagebox.showinfo(
        "Red Flags",
        "🚩 Unknown sender domain\n"
        "🚩 Urgent language\n"
        "🚩 Requests password\n"
        "🚩 Unofficial website\n"
        "🚩 Unrealistic reward"
    )


def case4_answer():

    ask_answer(
        "CASE #004",
        "What type of attack is this?",
        ["Phishing", "DDoS Attack", "Malware"],
        "Phishing",
        100,
        case_solved
    )


# ============================================================
# CASE 5
# ============================================================

def case5():

    clear_screen()

    create_title(
        "CASE #005 — THE FINAL MYSTERY",
        "🔐 The hardest case. Use everything you have learned."
    )

    story = (
        "A confidential examination paper disappeared from\n"
        "the faculty computer one day before the exam.\n\n"
        "Four people had access to the building.\n"
        "Only ONE person had the opportunity to copy it.\n\n"
        "Study the evidence carefully before making your accusation."
    )

    tk.Label(
        root,
        text=story,
        font=("Arial", 13),
        bg=BG,
        fg=TEXT,
        justify="center"
    ).pack(pady=15)

    tk.Button(
        root,
        text="🔍 EVIDENCE",
        command=case5_evidence,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=6)

    tk.Button(
        root,
        text="💻 COMPUTER LOG",
        command=case5_logs,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=6)

    tk.Button(
        root,
        text="👥 SUSPECT STATEMENTS",
        command=case5_suspects,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=6)

    tk.Button(
        root,
        text="🧩 FINAL PUZZLE",
        command=case5_puzzle,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=6)

    tk.Button(
        root,
        text="⚖ FINAL ACCUSATION",
        command=case5_answer,
        width=30,
        height=2,
        font=("Arial", 11, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=12)

    tk.Button(
        root,
        text="⬅ CASE FILES",
        command=home_screen
    ).pack()


def case5_evidence():

    messagebox.showinfo(
        "Evidence #1",
        "🗝 The faculty room door was opened using\n"
        "a staff access card at 6:42 PM."
    )

    messagebox.showinfo(
        "Evidence #2",
        "💾 A USB device was connected to the faculty\n"
        "computer at 6:47 PM."
    )

    messagebox.showinfo(
        "Evidence #3",
        "📄 The examination paper was copied at 6:49 PM."
    )

    messagebox.showinfo(
        "Evidence #4",
        "📱 A security camera detected someone leaving\n"
        "the faculty room at 6:52 PM."
    )


def case5_logs():

    messagebox.showinfo(
        "Faculty Computer Log",
        "06:40 PM → Computer unlocked\n"
        "06:42 PM → Staff access card detected\n"
        "06:47 PM → USB connected\n"
        "06:49 PM → Exam_Paper.pdf copied\n"
        "06:50 PM → USB removed\n"
        "06:52 PM → User logged out"
    )


def case5_suspects():

    messagebox.showinfo(
        "Professor Arun",
        "Says he left the building at 6:30 PM."
    )

    messagebox.showinfo(
        "Professor Meena",
        "Says she was in the faculty room until 7:00 PM."
    )

    messagebox.showinfo(
        "Lab Assistant Ravi",
        "Says he was repairing a computer in Lab #2."
    )

    messagebox.showinfo(
        "Student Rahul",
        "Says he was outside the building after 6:30 PM."
    )


def case5_puzzle():

    messagebox.showinfo(
        "Final Puzzle",
        "Think carefully!\n\n"
        "The file was copied at 6:49 PM.\n"
        "The person had to be inside the faculty room.\n\n"
        "Who claimed to still be inside at that time?\n\n"
        "💡 The answer is hidden in the suspect statements."
    )


def case5_answer():

    ask_answer(
        "CASE #005",
        "Who stole the examination paper?",
        [
            "Professor Arun",
            "Professor Meena",
            "Lab Assistant Ravi",
            "Student Rahul"
        ],
        "Professor Meena",
        200,
        final_victory
    )


# ============================================================
# ANSWER SYSTEM
# ============================================================

def ask_answer(case_name, question, options, correct_answer,
               points, success_function):

    clear_screen()

    create_title(
        case_name,
        "⚖ Make your accusation carefully."
    )

    tk.Label(
        root,
        text=question,
        font=("Arial", 16, "bold"),
        bg=BG,
        fg=WHITE
    ).pack(pady=25)

    selected = tk.StringVar()

    for option in options:

        tk.Radiobutton(
            root,
            text=option,
            variable=selected,
            value=option,
            font=("Arial", 13),
            bg=BG,
            fg=WHITE,
            selectcolor=PANEL,
            activebackground=BG,
            activeforeground=WHITE
        ).pack(pady=8)

    def submit():

        answer = selected.get()

        if answer == "":
            messagebox.showwarning(
                "No Answer",
                "Please select a suspect."
            )
            return

        if answer == correct_answer:

            success_function(points)

        else:

            messagebox.showerror(
                "❌ Wrong Accusation",
                "That suspect does not match the evidence.\n\n"
                "Review the clues and try again."
            )

    tk.Button(
        root,
        text="🔎 MAKE ACCUSATION",
        command=submit,
        width=25,
        height=2,
        font=("Arial", 12, "bold"),
        bg=GOLD,
        fg="black"
    ).pack(pady=25)

    tk.Button(
        root,
        text="⬅ BACK",
        command=home_screen
    ).pack()


# ============================================================
# CASE SOLVED
# ============================================================

def case_solved(points):

    global score
    global current_case

    # Add score only once
    if current_case not in solved_cases:
        solved_cases.append(current_case)
        score += points

    # Unlock next case
    if current_case < 5:

        next_case = current_case + 1

        messagebox.showinfo(
            "🎉 CASE SOLVED!",
            f"Excellent Detective!\n\n"
            f"You solved Case #{current_case}.\n"
            f"+{points} points\n\n"
            f"🔓 Case #{next_case} has been unlocked!"
        )

        # IMPORTANT: Move to the next case
        current_case = next_case

        home_screen()

    else:
        final_victory()


# ============================================================
# FINAL VICTORY
# ============================================================

def final_victory(points=0):

    global score

    if current_case not in solved_cases:

        solved_cases.append(current_case)
        score += points

    clear_screen()

    create_title(
        "🏆 ALL CASES SOLVED!",
        "You are officially a DIGITAL DETECTIVE!"
    )

    tk.Label(
        root,
        text="🎉 CONGRATULATIONS 🎉",
        font=("Arial", 25, "bold"),
        bg=BG,
        fg=GREEN
    ).pack(pady=25)

    tk.Label(
        root,
        text=(
            "You successfully solved all five mysteries!\n\n"
            "📁 Missing Project     ✓\n"
            "📱 Stolen Phone       ✓\n"
            "💻 Secret Hacker      ✓\n"
            "📧 Fake Email         ✓\n"
            "🔐 Final Mystery      ✓"
        ),
        font=("Arial", 14),
        bg=BG,
        fg=WHITE,
        justify="left"
    ).pack(pady=15)

    tk.Label(
        root,
        text=f"⭐ FINAL SCORE: {score}/600",
        font=("Arial", 22, "bold"),
        bg=BG,
        fg=GOLD
    ).pack(pady=20)

    if score >= 500:
        rank = "🏆 MASTER DETECTIVE"
    elif score >= 300:
        rank = "🥇 EXPERT DETECTIVE"
    else:
        rank = "🥈 JUNIOR DETECTIVE"

    tk.Label(
        root,
        text=rank,
        font=("Arial", 18, "bold"),
        bg=BG,
        fg=GREEN
    ).pack(pady=10)

    tk.Button(
        root,
        text="🔄 PLAY AGAIN",
        command=restart_game,
        width=20,
        height=2,
        font=("Arial", 11, "bold"),
        bg=BLUE,
        fg=WHITE
    ).pack(pady=15)

    tk.Button(
        root,
        text="EXIT",
        command=root.destroy,
        width=15
    ).pack()


# ============================================================
# RESTART
# ============================================================

def restart_game():

    global score
    global solved_cases
    global current_case

    score = 0
    solved_cases = []
    current_case = 1

    home_screen()


# ============================================================
# START PROGRAM
# ============================================================

home_screen()

root.mainloop()