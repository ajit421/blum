from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Coordinates: ({x}, {y})')
        
# Set up the listener for mouse clicks
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

    
# python -u "c:\code\BlumAutoClicker\Axis_check.py"