# nat_pagle
Python Bot with OpenCV

## Useful Links

| Link    | Purpose |
| ------- | ------- |
| [PyAutoGUI Docs](https://pyautogui.readthedocs.io/en/latest/)                 | Control mouse and keyboard |
| [OpenCV Docs](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)    | Computer Vision            | 
| [Example Project](https://www.learncodebygaming.com/blog/fast-window-capture) | Blog with example bot      |
| [Test Mouse Clicks](https://www.onlinemictest.com/mouse-test/)                | Mouse click website        |

## Bot Progression Tracker

| Description | Status      | Challenges |
| ----------- | ----------- | ----------- |
| Arbitrary Static Image Matching  | Done        |                                 |
| Real-Time Image Matching         | Done        |                                 |
| Inputs with PyAutoGUI            | Working     |                                 |
| New World Static Image Matching  | Done        |                                 |
| New World Image Collection       | Done        | Different resolutions needed    |
| New World Fishing Procedure      | Working     |                                 |
| New World Live Image Matching    | Done        |                                 |
| Rare Catch Rotation to Pin       | Not Started |                                 |
| Stop Bot on X Repeated Actions   | Not Started |                                 |
| Dead Check and Logout            | Not Started |                                 |                                               
| Compile to .exe                  | Not Started |                                 |                                               
| GUI                              | Not Started |                                 |                                               
| How to Use                       | Poorly Done |                                 |                                               
| Global Keypress for Operation    | Test Done   |                                 |                                               
| Custom Parameters                | Not Started |                                 |                                               

## How to Use

1. Run *main.py*
2. Alt-Tab to game
3. Facing water, pull out fishing pole
4. If you catch a rare fish you have to re-orient to water (fix soon, maybe)

## New World Fishing Procedure

Fishing Loop

1. Press F3 to pull out your pole and bait.
    - Optional: Press R to add bait to your line.
2. Hold LMB (left mouse button) to cast your line.
3. Release LMB at the desired cast distance.
    - A longer cast distance makes fish easier to reel in, as you have more "slack" when they fight.
    - When your line lands, the water depth and cast distance will be displayed.
    - When you're about to get a bite, it will say Get ready!
4. When you see Hook! click LMB to hook the fish. You will have short window of time to do this, shown with the colored circle around the picture of a hook next to a fish, that quickly depletes.
5. If you miss the hook, you will have to cast again.
6. If hooked, you will get a green checkmark and the message Reel in. Hold LMB to reel in.
7. Watch the tension meter, and release LMB to give slack as needed. Do not let the tension raise too high or your line will snap.
    - The tension color will go from green, to orange, to blinking red - red means it will snap soon, be careful!
    - Reel in the fish until the white circle on the outside of the tension meter completes the circle, and the distance reaches 0.0m.

Congratulations! You've caught a fish!


## How to build

```shell
pyinstaller --noconfirm --onedir --console --icon "C:/Users/narfa/Documents/_git/nat_pagle/03_hook_2.ico" --add-data "C
:/Users/narfa/Documents/_git/nat_pagle/new_world_images/needles;new_world_images/needles/"  "C:/Users/narfa/Documents/_git/nat_pagle/main.py"
```