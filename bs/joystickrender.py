import json
from rich.live import Live
from rich.table import Table
from joysticksocket import s
import logging
from datetime import datetime

logging.basicConfig(filename='joystick_receive_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_instruction(move, turn, depth):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - Move: {move}, Turn: {turn}, Depth: {depth}"
    logging.info(log_entry)


def generate_table() -> Table:
    x = s.recvfrom(1000000)
    client_ip = x[1][0]
    data = x[0]
    data_final = json.loads(data.decode())
    print(data_final)

    table = Table(title="Joystick Control Values")

    table.add_column("Control", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="yellow")

    table.add_row("Move", str(data_final['move']))
    table.add_row("Turn", str(data_final['turn']))
    table.add_row("Depth", str(data_final['depth']))

    # Write the data
    log_instruction(data_final['move'], data_final['turn'], data_final['depth'])



with Live(generate_table(), refresh_per_second=40) as live:
    while True:
        live.update(generate_table())
