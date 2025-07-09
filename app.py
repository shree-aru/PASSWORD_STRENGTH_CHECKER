
import tkinter as tk
from tkinter import ttk
from password_analyzer import analyze_password_strength

class PasswordStrengthCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Styling
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10, "bold"))
        self.style.configure("Strength.TLabel", font=("Arial", 12, "bold"))

        # Main Frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Password Input
        password_label = ttk.Label(main_frame, text="Enter Password:")
        password_label.pack(pady=(0, 5))

        self.password_entry = ttk.Entry(main_frame, show="*", width=50)
        self.password_entry.pack(pady=(0, 10))
        self.password_entry.bind("<KeyRelease>", self.check_password)

        # Strength Display
        self.strength_label = ttk.Label(main_frame, text="Strength: ", style="Strength.TLabel")
        self.strength_label.pack(pady=(10, 5))

        # Feedback Display
        self.feedback_label = ttk.Label(main_frame, text="Feedback: ", wraplength=450, justify=tk.LEFT)
        self.feedback_label.pack(pady=(0, 10))

        # Analyze Button
        analyze_button = ttk.Button(main_frame, text="Analyze Password", command=self.check_password)
        analyze_button.pack(pady=(10, 0))

    def check_password(self, event=None):
        password = self.password_entry.get()
        if not password:
            self.strength_label.config(text="Strength: ")
            self.feedback_label.config(text="Feedback: ")
            return

        strength, feedback = analyze_password_strength(password)
        self.strength_label.config(text=f"Strength: {strength}")
        self.feedback_label.config(text="Feedback:\n" + "\n".join(feedback))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthCheckerApp(root)
    root.mainloop()


