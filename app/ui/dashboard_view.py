import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import logging

from app.ml.prediction import predict_personality
from app.utils.paths import image_path
from app.ui.theme import font, style_button

logger = logging.getLogger(__name__)

# Full 5-trait dictionary matching your custom trained model dataset
PERSONALITY_DETAILS = {
    "Honest": {
        "description": "The person appears trustworthy, sincere, practical, and emotionally balanced. This handwriting reflects clarity of thought, stable behavior, and genuine communication.",
        "mental_state": "At the moment of writing, the person was likely calm, focused, emotionally stable, and mentally composed."
    },
    "Persistent": {
        "description": "The person appears disciplined, determined, hardworking, and goal-oriented. Such individuals usually maintain consistency and do not give up easily.",
        "mental_state": "At the moment of writing, the person was likely highly focused, patient, and mentally committed to the task."
    },
    "Narcissist": {
        "description": "The person appears self-confident, attention-seeking, expressive, and socially dominant. They may value recognition, influence, and personal image strongly.",
        "mental_state": "At the moment of writing, the person was likely emotionally expressive, self-focused, and seeking validation or attention."
    },
    "Excitable": {
        "description": "The person appears energetic, emotionally reactive, spontaneous, and expressive. Such individuals may experience rapid emotional changes and high enthusiasm.",
        "mental_state": "At the moment of writing, the person was likely emotionally excited, mentally stimulated, anxious, stressed, or highly energetic."
    },
    "Criminal Intent": {
        "description": "The handwriting exhibits patterns historically associated with high impulsivity, defiance, or acute behavioral misalignment under pressure. Note: This analysis suggests underlying behavioral tension or stress patterns, not a definitive legal diagnosis.",
        "mental_state": "At the moment of writing, the individual may have been experiencing high internal friction, emotional hostility, defensive stress, or severe anxiety."
    }
}

class DashboardView(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.logged_user = "User"

        self.selected_img_path = None
        self.uploaded_image = None

        # ================= SCREEN =================
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # ================= BACKGROUND =================
        self.configure(bg="#0f172a")

        try:
            bg_img = Image.open(image_path("neural2.jpeg"))
            bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_img)

            bg_label = Label(self, image=self.bg_photo, bd=0)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()
        except Exception as e:
            logger.error(f"Background image not found: {e}")

        # ================= SIDEBAR =================
        sidebar = Frame(self, bg="#111827", width=180)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        Label(
            sidebar,
            text="AI Handwriting",
            bg="#111827",
            fg="white",
            font=font(16, "bold"),
            justify="center"
        ).pack(pady=(40, 5))

        Label(
            sidebar,
            text="Analysis Studio",
            bg="#111827",
            fg="#94a3b8",
            font=font(10)
        ).pack()

        # ================= NAVIGATION =================
        def logout():
            self.controller.show_frame("LoginView")

        def about_us():
            self.controller.show_frame("AboutView")

        about_btn = Button(
            sidebar,
            text="About Us",
            font=font(10, "bold"),
            command=about_us,
            bd=0,
            relief="flat",
            cursor="hand2",
            activeforeground="white"
        )
        style_button(about_btn, "#1e293b", "#334155")
        about_btn.pack(pady=(60, 10), fill="x", padx=15, ipady=6)

        logout_btn = Button(
            sidebar,
            text="Logout",
            font=font(10, "bold"),
            command=logout,
            bd=0,
            relief="flat",
            cursor="hand2",
            activeforeground="white"
        )
        style_button(logout_btn, "#dc2626", "#b91c1c")
        logout_btn.pack(side="bottom", fill="x", ipady=8)

        # ================= HEADER =================
        self.welcome_label = Label(
            self,
            text="Welcome, User",
            bg="#0f172a",
            fg="white",
            font=font(24, "bold")
        )
        self.welcome_label.place(x=220, y=30)

        Label(
            self,
            text="Upload a handwriting sample and run personality analysis.",
            bg="#0f172a",
            fg="#cbd5e1",
            font=font(12)
        ).place(x=222, y=80)

        # =========================================================
        # ================= UPLOAD CARD ===========================
        # =========================================================
        upload_card = Frame(
            self,
            bg="#1e293b",
            width=600,       
            height=620,      
            bd=0,
            highlightbackground="#0f172a",
            highlightthickness=2
        )
        upload_card.place(x=230, y=130)  
        upload_card.pack_propagate(False)

        Label(
            upload_card,
            text="Upload Handwriting Sample",
            bg="#1e293b",
            fg="white",
            font=font(20, "bold")
        ).place(relx=0.5, y=60, anchor="center")

        Label(
            upload_card,
            text="Choose a clear JPG or PNG sample for best results.",
            bg="#1e293b",
            fg="#94a3b8",
            font=font(13)
        ).place(relx=0.5, y=90, anchor="center")

        self.preview_label = Label(
            upload_card,
            text="No image selected",
            bg="#0f172a",
            fg="#94a3b8",
            font=font(14),
            relief="flat",
            bd=0
        )
        self.preview_label.place(relx=0.5, y=305, width=420, height=300, anchor="center")

        # ================= UPLOAD FUNCTION =================
        def upload_image():
            file_path = filedialog.askopenfilename(
                filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
            )
            if not file_path:
                return

            self.selected_img_path = file_path
            image = Image.open(file_path)
            image.thumbnail((400, 190)) 
            self.uploaded_image = ImageTk.PhotoImage(image)

            self.preview_label.config(
                image=self.uploaded_image,
                text=""
            )

            self.detected_trait_label.config(text="Ready")
            self.accuracy_label.config(text="Ready")
            self.percentage_label.config(text="0%")
            self.reset_progress_bar()

        # Button Container for horizontal layout
        btn_container = Frame(upload_card, bg="#1e293b")
        btn_container.place(relx=0.5, y=560, anchor="center") 

        upload_btn = Button(
            btn_container,
            text="Choose Image",
            command=upload_image,
            font=font(11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        style_button(upload_btn, "#2563eb", "#1d4ed8")
        upload_btn.pack(side="left", padx=15, ipadx=25, ipady=6)

        reset_btn = Button(
            btn_container,
            text="Reset",
            command=self.reset_page,
            font=font(11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        style_button(reset_btn, "#f59e0b", "#d97706")
        reset_btn.pack(side="left", padx=15, ipadx=35, ipady=6)

        # =========================================================
        # ================= ANALYSIS CARD =========================
        # =========================================================
        analysis_card = Frame(
            self,
            bg="#1e293b",
            width=600,       
            height=620,      
            bd=0,
            highlightbackground="#0f172a",
            highlightthickness=2
        )
        analysis_card.place(x=860, y=130) 
        analysis_card.pack_propagate(False)

        Label(
            analysis_card,
            text="AI Personality Analysis",
            bg="#1e293b",
            fg="white",
            font=font(18, "bold")
        ).place(relx=0.5, y=40, anchor="center")

        Label(
            analysis_card,
            text="Prediction confidence updates after analysis.",
            bg="#1e293b",
            fg="#94a3b8",
            font=font(11)
        ).place(relx=0.5, y=75, anchor="center")

        # ================= SCI-FI PROGRESS BAR (CANVAS) =================
        self.bar_width = 420 
        self.progress_canvas = Canvas(
            analysis_card,
            width=self.bar_width,
            height=36,
            bg="#1e293b",
            highlightthickness=0
        )
        self.progress_canvas.place(relx=0.5, y=130, anchor="center")

        # HUD Corner Brackets
        self.progress_canvas.create_line(0, 12, 0, 0, 12, 0, fill="#38bdf8", width=2)
        self.progress_canvas.create_line(0, 24, 0, 36, 12, 36, fill="#38bdf8", width=2)
        self.progress_canvas.create_line(self.bar_width, 12, self.bar_width, 0, self.bar_width - 12, 0, fill="#38bdf8", width=2)
        self.progress_canvas.create_line(self.bar_width, 24, self.bar_width, 36, self.bar_width - 12, 36, fill="#38bdf8", width=2)

        # Trough Line
        self.progress_canvas.create_rectangle(16, 8, self.bar_width - 16, 28, outline="#334155", fill="#0f172a")

        # Generate Segments
        self.segments = []
        self.total_segments = 42 
        start_x = 19

        for i in range(self.total_segments):
            seg = self.progress_canvas.create_rectangle(
                start_x + (i * 9), 11, start_x + (i * 9) + 6, 25,
                fill="#0f172a", outline=""
            )
            self.segments.append(seg)

        # ================= RESULTS AREA =================
        results_frame = Frame(analysis_card, bg="#0f172a", width=520, height=360)
        results_frame.place(relx=0.5, y=340, anchor="center")
        results_frame.pack_propagate(False)

        self.percentage_label = Label(
            results_frame,
            text="0%",
            bg="#0f172a",
            fg="#38bdf8",
            font=font(38, "bold")
        )
        self.percentage_label.pack(pady=(10, 5))

        # Trait Result
        trait_container = Frame(results_frame, bg="#0f172a")
        trait_container.pack(fill="x", padx=50, pady=4)
        Label(trait_container, text="Detected Trait:", bg="#0f172a", fg="white", font=font(11, "bold")).pack(side="left")
        self.detected_trait_label = Label(trait_container, text="--", bg="#0f172a", fg="#60a5fa", font=font(11, "bold"))
        self.detected_trait_label.pack(side="right")

        # Accuracy Result
        accuracy_container = Frame(results_frame, bg="#0f172a")
        accuracy_container.pack(fill="x", padx=50, pady=4)
        Label(accuracy_container, text="Accuracy:", bg="#0f172a", fg="white", font=font(11, "bold")).pack(side="left")
        self.accuracy_label = Label(accuracy_container, text="--", bg="#0f172a", fg="#0ea5e9", font=font(11, "bold"))
        self.accuracy_label.pack(side="right")

        # Personality Overview 
        self.description_title = Label(results_frame, text="Personality Overview", bg="#0f172a", fg="#38bdf8", font=font(12, "bold"))
        self.description_title.pack(pady=(10, 4))

        self.personality_description = Text(
            results_frame, bg="#0f172a", fg="#e2e8f0", font=font(11),
            wrap=tk.WORD, width=50, height=3, bd=0, highlightthickness=0
        )
        self.personality_description.pack(padx=20, pady=2)
        self.personality_description.insert(tk.END, "--")
        self.personality_description.config(state=tk.DISABLED)

        # Possible Mental State 
        self.state_title = Label(results_frame, text="Possible Mental State", bg="#0f172a", fg="#38bdf8", font=font(12, "bold"))
        self.state_title.pack(pady=(10, 4))

        self.mental_state_label = Text(
            results_frame, bg="#0f172a", fg="#cbd5e1", font=font(11),
            wrap=tk.WORD, width=50, height=3, bd=0, highlightthickness=0
        )
        self.mental_state_label.pack(padx=20, pady=(0, 10))
        self.mental_state_label.insert(tk.END, "--")
        self.mental_state_label.config(state=tk.DISABLED)

        # ================= ACTION BUTTON (RUN ANALYSIS) =================
        analyze_btn = Button(
            analysis_card,
            text="Run Personality Analysis",
            command=self.analyze_image,
            font=font(11, "bold"),
            bd=0,
            relief="flat",
            cursor="hand2"
        )
        style_button(analyze_btn, "#10b981", "#059669")
        analyze_btn.place(relx=0.5, y=560, anchor="center", width=240, height=38)

    # ================= CLASS HELPER METHODS =================
    def reset_progress_bar(self):
        for seg in self.segments:
            self.progress_canvas.itemconfig(seg, fill="#0f172a")

    def animate_progress(self, target=100):
        self.reset_progress_bar()

        def step(value=0):
            if value <= target:
                active_count = int((value / 100) * self.total_segments)
                for i, seg in enumerate(self.segments):
                    if i < active_count:
                        if i == active_count - 1:
                            color = "#ffffff"  
                        elif i > active_count - 4:
                            color = "#7dd3fc"  
                        else:
                            color = "#0284c7"  
                        self.progress_canvas.itemconfig(seg, fill=color)
                    else:
                        self.progress_canvas.itemconfig(seg, fill="#0f172a")

                self.percentage_label.config(text=f"{value}%")
                self.after(12, lambda: step(value + 1))

        step()

    # ================= ANALYZE FUNCTION =================
    def analyze_image(self):
        if not self.selected_img_path:
            messagebox.showwarning("Warning", "Please upload an image first.")
            return

        try:
            self.detected_trait_label.config(text="Scanning...", fg="#facc15")
            self.accuracy_label.config(text="--", fg="#94a3b8")
            
            for text_widget, msg in [(self.personality_description, "Analyzing personality patterns..."), 
                                     (self.mental_state_label, "Detecting emotional state...")]:
                text_widget.config(state=tk.NORMAL)
                text_widget.delete("1.0", tk.END)
                text_widget.insert(tk.END, msg)
                text_widget.config(state=tk.DISABLED)
                
            self.update()

            label, confidence = predict_personality(self.selected_img_path)

            self.animate_progress(int(confidence))
            
            # FIXED: Reformats raw predictions like 'criminal_intent' safely into 'Criminal Intent'
            formatted_label = label.replace("_", " ").title() 

            self.detected_trait_label.config(text=formatted_label, fg="#60a5fa")
            self.accuracy_label.config(text=f"{confidence:.2f}%", fg="#0ea5e9")

            details = PERSONALITY_DETAILS.get(
                formatted_label,
                {
                    "description": "Personality description not available.",
                    "mental_state": "Mental state prediction not available."
                }
            )

            self.personality_description.config(state=tk.NORMAL)
            self.personality_description.delete("1.0", tk.END)
            self.personality_description.insert(tk.END, details["description"])
            self.personality_description.config(state=tk.DISABLED)

            self.mental_state_label.config(state=tk.NORMAL)
            self.mental_state_label.delete("1.0", tk.END)
            self.mental_state_label.insert(tk.END, details["mental_state"])
            self.mental_state_label.config(state=tk.DISABLED)

        except Exception as exc:
            logger.exception("Prediction failed")
            messagebox.showerror("Prediction Error", str(exc))

            self.detected_trait_label.config(text="Failed", fg="#f87171")
            self.accuracy_label.config(text="--", fg="#94a3b8")
            self.percentage_label.config(text="0%")
            self.reset_progress_bar()

            self.personality_description.config(state=tk.NORMAL)
            self.personality_description.delete("1.0", tk.END)
            self.personality_description.insert(tk.END, "Analysis failed.")
            self.personality_description.config(state=tk.DISABLED)

            self.mental_state_label.config(state=tk.NORMAL)
            self.mental_state_label.delete("1.0", tk.END)
            self.mental_state_label.insert(tk.END, "Unable to detect mental state.")
            self.mental_state_label.config(state=tk.DISABLED)

    # ================= USER METHODS =================
    def refresh_user(self):
        self.welcome_label.config(text=f"Welcome, {self.logged_user}")

    def set_user(self, username):
        self.logged_user = username
        self.welcome_label.config(text=f"Welcome, {username}")

    def reset_page(self):
        self.selected_img_path = None
        self.uploaded_image = None
        self.preview_label.config(
            image="",
            text="No image selected",
            bg="#0f172a",
            fg="#94a3b8"
        )
        self.detected_trait_label.config(text="--", fg="#60a5fa")
        self.accuracy_label.config(text="--", fg="#0ea5e9")
        self.percentage_label.config(text="0%", fg="#38bdf8")
        
        for text_widget in [self.personality_description, self.mental_state_label]:
            text_widget.config(state=tk.NORMAL)
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, "--")
            text_widget.config(state=tk.DISABLED)
            
        self.reset_progress_bar()
