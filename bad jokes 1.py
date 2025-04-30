import flet as ft
import random

def main(page: ft.Page):
    
    jokes = [
        "How does a penguin build its house? Igloos it together 😂. (please laugh)",
        "How much does a chimey cost? nothing, is on the house",
        "Why was cinderella bad at the ball? she ran away from the ball",
        "What do you call fake spaghetti? An impasta 🍝.",
        "Why do bananas wear sunscreen? They don't want to peel."
        "What did one Post-it Note say to the other? Let's stick together.",
        "Why don't zombies eat clowns? Because they taste funny.",
        "Where do spiders buy their clothes? On the web. (laugh now)",
        "Can February March? No, but April May.",
        "How can you tell if a plant is good at math? It has square roots."
    ]

#yeah I got the jokes from a website and my broken humour couldn't stop laughing
    
    def tell_joke(e):
        joke_text.value = random.choice(jokes)
        page.open(joke_sheet)


    def close_joke(e):
        page.close(joke_sheet)

    
    joke_text = ft.Text(value="", size=16)

   
    joke_sheet = ft.BottomSheet(
        content=ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    joke_text,
                    ft.ElevatedButton(text="Close", on_click=close_joke)
                ],
                tight=True,
                spacing=20
            )
        )
    )

    
    tell_joke_button = ft.ElevatedButton(
        text="Tell me a joke",
        on_click=tell_joke
    )

    page.add(tell_joke_button)

ft.app(target=main)