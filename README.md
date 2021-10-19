# nat_pagle
Python Bot with OpenCV

## Bot Progression Tracker

| Description | Status      | Challenges |
| ----------- | ----------- | ----------- |
| Arbitrary Static Image Matching  | Done        |                  |
| Real-Time Image Matching         | Not Started |                  |
| Inputs with PyAutoGUI            | Not Started | Learn PyAutoGUI  |
| New World Static Image Matching  | Done        |                  |
| New World Image Collection       | Test Ready  |                  |
| New World Fishing Procedure      | Test Ready  |                  |
| New World Live Image Matching    | Not Started |                  |

## New World Fishing Procedure

Prerequisites

1. Facing Water
    - Potential need turning to specific direction using compass 

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
