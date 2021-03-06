import json
import logging
import toga
from toga.style import Pack
from toga.style.pack import COLUMN


logging.basicConfig(
    format="%(asctime)s | %(levelname)s: %(message)s",
    level=logging.NOTSET
)

def build(app):
    # Lista de monedas
    with open("coins.json") as json_file:
        coins_data = json.load(json_file)
        logging.info(coins_data)
    coins = [coin for coin in coins_data]
    logging.info(f"Coins available: {coins}")

    # Caja de primera moneda
    first_coin_box = toga.Box(id='first_coin', style=Pack(direction=COLUMN, padding_top=10))
    first_coin_selection = toga.Selection(items=coins)
    first_coin_box.add(first_coin_selection)
    first_coin_input = toga.TextInput()
    first_coin_box.add(first_coin_input)

    # Caja de segunda moneda
    second_coin_box = toga.Box(id="second_coin", style=Pack(direction=COLUMN, padding_top=10))
    second_coin_selection = toga.Selection(items=coins)
    second_coin_box.add(second_coin_selection)
    second_coin_input = toga.TextInput(readonly=True)
    second_coin_box.add(second_coin_input)

    # Boton de calcular
    def calculate(widget):
        first_coin = first_coin_selection.value
        logging.info(f"Primera moneda: {first_coin}")
        second_coin = second_coin_selection.value
        logging.info(f"Segunda moneda: {second_coin}")

        if not first_coin_input.value.isdigit():
            second_coin_input.value = ""
            return None

        if first_coin == second_coin:
            second_coin_input.value = first_coin_input.value
        else:
            logging.info(coins_data[first_coin])
            logging.info(coins_data[first_coin][second_coin])
            result = float(first_coin_input.value) / float(coins_data[first_coin][second_coin])
            second_coin_input.value = f"{result:.2f}"

        logging.info(f"Resultado: {first_coin_input.value} {first_coin} equivale a {second_coin_input.value} {second_coin}")

    button = toga.Button("Calcular", on_press=calculate)

    # Caja principal
    box = toga.Box(id='box', style=Pack(direction=COLUMN, padding_top=10))
    box.add(first_coin_box)
    box.add(second_coin_box)
    box.add(button)

    return box


def main():
    return toga.App('Convertidor de monedas', 'org.medina.aurora', startup=build)


if __name__=="__main__":
    main().main_loop()
