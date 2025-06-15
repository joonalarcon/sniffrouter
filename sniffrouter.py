import nmap
import time
import json
import csv
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

console = Console()

def escanear_dispositivos_agresivo(rango_ip):
    nm = nmap.PortScanner()
    dispositivos = []

    inicio = time.time()
    hora_inicio = datetime.now().strftime("%H:%M:%S")
    console.print(f"\n[bold cyan]Iniciando escaneo agresivo en {rango_ip}...[/bold cyan]")
    console.print(f"[bold]Hora de inicio:[/bold] {hora_inicio}")

    with Progress(
        SpinnerColumn(),
        "[progress.description]{task.description}",
        TimeElapsedColumn(),
        transient=True,
    ) as progress:
        task = progress.add_task("[green]Escaneando agresivamente...", total=None)
        # Escaneo agresivo completo
        nm.scan(hosts=rango_ip, arguments='-A')
        progress.update(task, completed=1)

    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            info = {'ip': host}

            # Hostname
            try:
                hostname = nm[host].hostname()
                info['hostname'] = hostname if hostname else 'No disponible'
            except:
                info['hostname'] = 'Error al obtener hostname'

            # MAC Address
            try:
                mac = nm[host]['addresses'].get('mac', 'No disponible')
                info['mac'] = mac
            except:
                info['mac'] = 'Error al obtener MAC'

            # Sistema Operativo
            try:
                os_matches = nm[host].get('osmatch', [])
                if os_matches:
                    os_name = os_matches[0]['name']
                    os_accuracy = os_matches[0]['accuracy']
                    info['os'] = f"{os_name} ({os_accuracy}%)"
                else:
                    info['os'] = 'No detectado'
            except:
                info['os'] = 'Error al detectar SO'

            # Puertos abiertos
            try:
                puertos_abiertos = []
                for proto in nm[host].all_protocols():
                    for port in sorted(nm[host][proto].keys()):
                        estado = nm[host][proto][port]['state']
                        puertos_abiertos.append(f"{port}/{proto} ({estado})")
                info['puertos'] = ', '.join(puertos_abiertos) if puertos_abiertos else 'Ninguno'
            except:
                info['puertos'] = 'Error al detectar puertos'

            dispositivos.append(info)

    duracion = time.time() - inicio
    hora_fin = datetime.now().strftime("%H:%M:%S")
    console.print(f"[bold green]Escaneo completado en {duracion:.2f} segundos[/bold green]")
    console.print(f"[bold]Hora de fin:[/bold] {hora_fin}")
    console.print(f"[bold yellow]Dispositivos encontrados:[/bold yellow] {len(dispositivos)}\n")

    return dispositivos

def mostrar_resultados(dispositivos):
    table = Table(title="Dispositivos Activos Detectados")

    table.add_column("IP", style="cyan", no_wrap=True)
    table.add_column("Hostname", style="magenta")
    table.add_column("MAC", style="yellow")
    table.add_column("Sistema Operativo", style="green")
    table.add_column("Puertos Abiertos", style="red")

    for d in dispositivos:
        table.add_row(d['ip'], d['hostname'], d['mac'], d['os'], d['puertos'])

    console.print(table)

def exportar_resultados(dispositivos):
    with open("resultados.json", "w") as f:
        json.dump(dispositivos, f, indent=4)

    with open("resultados.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["ip", "hostname", "mac", "os", "puertos"])
        writer.writeheader()
        writer.writerows(dispositivos)

    console.print("[bold blue]Resultados exportados a [italic]resultados.json[/italic] y [italic]resultados.csv[/italic][/bold blue]")

if __name__ == '__main__':
    rango = '192.168.1.0/24'
    dispositivos_activos = escanear_dispositivos_agresivo(rango)
    mostrar_resultados(dispositivos_activos)
    exportar_resultados(dispositivos_activos)
