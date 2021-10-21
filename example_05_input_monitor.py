"""This is for testing input tracking when not focussed.

Reference: https://pynput.readthedocs.io/en/latest/
"""

from pynput import keyboard


def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except AttributeError as e:
        k = key.name  # other keys

    if k == 'b':
        print("Start fishing")

    if k == 'n':
        print("Stop fishing")

    # Multi Catch
    # if k in ['1', '2', 'left', 'right']:  # keys of interest
    #     print('Key pressed: ' + k)
    #     return False  # stop listener; remove this if want more keys


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys