import tkinter as tk
from tkinter import messagebox
import threading
from summarizer import summarizeStream

def on_summarize():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Missing URL", "Please enter a YouTube URL.")
        return

    # Disable button & clear previous output
    summarize_btn.config(state=tk.DISABLED)
    status_label.config(text="Summarizing…", fg="#f0c040")
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.config(state=tk.DISABLED)

    def run():
        try:
            # Get selected mood
            selection = mood_listbox.curselection()
            tone = mood_listbox.get(selection[0]) if selection else "Professional"
            
            for chunk in summarizeStream(url, tone):
                token = getattr(chunk.choices[0].delta, "content", "") or ""
                if token:
                    root.after(0, append_text, result_box, token)
            root.after(0, finish_summarize, True)
        except Exception as e:
            root.after(0, finish_summarize, False, str(e))

    threading.Thread(target=run, daemon=True).start()


def finish_summarize(success, error_msg=""):
    summarize_btn.config(state=tk.NORMAL)
    if success:
        status_label.config(text="Done!", fg="#40c057")
    else:
        status_label.config(text=f"Error: {error_msg}", fg="#e03131")

def append_text(widget, text):
    widget.config(state=tk.NORMAL)
    widget.insert(tk.END, text)
    widget.see(tk.END)
    widget.config(state=tk.DISABLED)

root = tk.Tk()
root.title("YT Summarizer")
root.geometry("700x560")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

BG = "#1e1e2e"
FG = "#cdd6f4"
ENTRY_BG = "#313244"
BTN_BG = "#7c3aed"
BTN_FG = "#ffffff"
TEXT_BG = "#181825"
FONT = ("Segoe UI", 11)
FONT_BOLD = ("Segoe UI", 12, "bold")
FONT_TITLE = ("Segoe UI", 18, "bold")

# Title
tk.Label(root, text="YouTube Video Summarizer", font=FONT_TITLE, bg=BG, fg=FG).pack(pady=(20, 2))
tk.Label(root, text="Paste any YouTube URL and get a summary in seconds", font=("Segoe UI", 10), bg=BG, fg="#a6adc8").pack()

# URL input row
input_frame = tk.Frame(root, bg=BG)
input_frame.pack(fill=tk.X, padx=20, pady=(18, 6))

url_entry = tk.Entry(input_frame, font=FONT, bg=ENTRY_BG, fg=FG, insertbackground=FG,
                     relief=tk.FLAT, borderwidth=8)
url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=4)

summarize_btn = tk.Button(input_frame, text="Summarize", font=FONT_BOLD,
                          bg=BTN_BG, fg=BTN_FG, activebackground="#6d28d9",
                          activeforeground=BTN_FG, relief=tk.FLAT, padx=18, pady=4,
                          cursor="hand2", command=on_summarize)
summarize_btn.pack(side=tk.LEFT, padx=(10, 0))

# Mood selection
mood_frame = tk.Frame(root, bg=BG)
mood_frame.pack(fill=tk.X, padx=20, pady=(0, 10))

tk.Label(mood_frame, text="Select Mood:", font=("Segoe UI", 10, "bold"), bg=BG, fg="#a6adc8").pack(anchor=tk.W)

mood_listbox = tk.Listbox(mood_frame, font=("Segoe UI", 10), bg=ENTRY_BG, fg=FG, 
                          selectbackground=BTN_BG, selectforeground=BTN_FG, 
                          height=4, relief=tk.FLAT, borderwidth=0, highlightthickness=0)
mood_listbox.pack(fill=tk.X, pady=(4, 0))

moods = ["Professional", "Funny", "Sarcastically Mean", "Informative", "Short & Concise"]
for mood in moods:
    mood_listbox.insert(tk.END, mood)
mood_listbox.selection_set(0) # Default to Professional

# Status label
status_label = tk.Label(root, text="", font=("Segoe UI", 10), bg=BG, fg=FG)
status_label.pack(anchor=tk.W, padx=20)

# Result text box
result_box = tk.Text(root, font=FONT, bg=TEXT_BG, fg=FG, wrap=tk.WORD,
                     relief=tk.FLAT, borderwidth=8, height=14, state=tk.DISABLED)
result_box.pack(fill=tk.BOTH, padx=20, pady=(4, 0), expand=True)

root.mainloop()
