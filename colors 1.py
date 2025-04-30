import flet as ft
#credits to michelle for helping me
#yo no fui el dia que pusieron el assignment entonces estoy leyendo y dice algo de repository link ?? no se que es esooo
def main(page: ft.Page):
  
    page.bgcolor = "#FFFFFF"  

    
    red = 0
    green = 0
    blue = 0

    
    def update_color(e):
        nonlocal red, green, blue
        red = red_slider.value
        green = green_slider.value
        blue = blue_slider.value
        
        
        page.bgcolor = f"#{red:02x}{green:02x}{blue:02x}"
        
        
        rgb_text.value = f"RGB: ({red}, {green}, {blue})"
        hex_text.value = f"Hex: #{red:02x}{green:02x}{blue:02x}"
        
        page.update()

    
    red_slider = ft.Slider(min=0, max=255, value=0, label="Red", on_change=update_color)
    green_slider = ft.Slider(min=0, max=255, value=0, label="Green", on_change=update_color)
    blue_slider = ft.Slider(min=0, max=255, value=0, label="Blue", on_change=update_color)

    
    rgb_text = ft.Text("RGB: (0, 0, 0)", size=20, color="black")  
    hex_text = ft.Text("Hex: #000000", size=20, color="black")  
    
    page.add(red_slider, green_slider, blue_slider, rgb_text, hex_text)

ft.app(target=main)