# 🔍 Escáner de Red Agresivo (Python + Nmap)

Este script realiza un escaneo agresivo sobre tu red local utilizando `nmap`. Detecta:

- Dispositivos activos
- IPs, hostnames y direcciones MAC
- Sistemas operativos (probables)
- Puertos abiertos

Incluye una interfaz en terminal enriquecida con `rich` (tablas a color, barra de progreso) y exporta los resultados en archivos `.json` y `.csv`.

> ⚠️ Diseñado para auditorías éticas, uso educativo o redes personales. No utilizar en redes ajenas sin permiso.

---

## ⚙️ Requisitos Generales

- Python 3.7 o superior
- Nmap instalado en el sistema
- Permisos de superusuario (`sudo`)
- Librerías de Python:
  - `rich`
  - `python-nmap`

---
