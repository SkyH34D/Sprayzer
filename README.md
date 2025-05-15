
# 🔐 Sprayzer - Password Sprayer w/ GUI

  <p align="center">
    <a align="center" href="" target="https://github.com/SkyH34D/Sprayzer">
      <img
        width="500"
        height="200"
        src="https://github.com/SkyH34D/Sprayzer/blob/48802ce7195ad0bea44d524f9854af66a47b67d8/media/Sprayzer.png"
      >
    </a>
  </p>

Herramienta con interfaz gráfica en Python para realizar **password spraying** sobre servicios SSH y SMB de forma sencilla, controlada y eficaz.

## ✨ Características

- ✅ Interfaz gráfica con `Tkinter`
- ✅ Soporte para **SSH y SMB**
- ✅ Múltiples contraseñas por lote (rotación de password spraying)
- ✅ Resultados en tiempo real en la ventana de la aplicación
- ✅ Spraying por lotes: prueba una contraseña contra todos los usuarios antes de pasar a la siguiente
- ✅ Modular, adaptable facilmente a otros servicios como LDAP o FTP

## 🧰 Requisitos

### ⚙️ Sistema

- Linux (recomendado: Kali, Parrot, Ubuntu)
- Python 3.x

### 📦 Dependencias del sistema

```bash
sudo apt install sshpass crackmapexec
```

### 📦 Dependencias Python

```bash
pip install tkinter
```

> `tkinter` ya viene incluido con la mayoría de instalaciones de Python. Si no lo tienes:
```bash
sudo apt install python3-tk
```

## 🚀 Uso

```bash
python3 gui_password_sprayer.py
```

1. Escribe la IP o dominio del objetivo.
2. Selecciona protocolo (`ssh` o `smb`).
3. Carga un archivo `.txt` con lista de usuarios (uno por línea).
4. Carga un archivo `.txt` con contraseñas (uno por línea).
5. Haz clic en “Iniciar Spraying”.

## ⚠️ Ética y Legalidad

> Esta herramienta debe ser usada **únicamente** en entornos autorizados:
>
> - Laboratorios de pruebas
> - Simulaciones internas
> - Pentests con consentimiento

**El uso sin permiso es ilegal y puede tener consecuencias graves.**
