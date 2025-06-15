# 🔍 SniffRouter - Escáner de Red Agresivo (Python + Nmap)

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![Nmap](https://img.shields.io/badge/Nmap-Installed-important?logo=nmap)](https://nmap.org/)
[![Rich](https://img.shields.io/badge/Rich-%F0%9F%92%8E-purple?logo=python)](https://github.com/Textualize/rich)
[![python-nmap](https://img.shields.io/badge/python--nmap-%F0%9F%9A%80-orange)](https://github.com/alexxy/python-nmap)

> 🚨 Herramienta para escaneos agresivos y visuales en redes personales o de laboratorio.

---

## 📡 ¿Qué hace?

Este script realiza un escaneo agresivo sobre tu red local utilizando `nmap`. Detecta:

- 🖥️ **Dispositivos activos**
- 🌐 **IPs, hostnames y direcciones MAC**
- 🧠 **Sistemas operativos (probables)**
- 🔐 **Puertos abiertos**

Presenta los resultados en una **interfaz de terminal enriquecida con `rich`**, y permite exportar los datos a:

- 📄 `.json`
- 📊 `.csv`

> ⚠️ **Uso ético solamente**: diseñado para redes personales, entornos educativos o auditorías autorizadas. ¡No lo uses en redes ajenas sin permiso!

---

## ⚙️ Requisitos

- 🐍 Python 3.7 o superior
- 🔧 `nmap` instalado en el sistema
- 🔐 Permisos de superusuario (`sudo`)
- 📦 Librerías de Python:
  - [`rich`](https://github.com/Textualize/rich)
  - [`python-nmap`](https://github.com/alexxy/python-nmap)

Instalación rápida:

```bash
pip install -r requirements.txt
