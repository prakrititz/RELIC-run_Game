# Relic Run: Pursuit for the Eldritch Gem

**Developers: Prakrititz Borah, Satyam Ambi, Unnath Chittimalla**

## Game Overview

Welcome to Relic Run, an enchanting adventure game that invites you to embark on a quest to discover the mythical Eldritch Gem. Immerse yourself in a captivating world filled with challenging levels, mystical gems, and a rich auditory experience. This game features visually stunning and diverse gaming environments with assets sourced from [OpenGameArt](https://opengameart.org/).

## Installation

Before running the game, make sure the `pygame` module is installed. You can install it using the following command:

```bash
pip install pygame
```

## Gameplay

### Objective

Embark on a journey to guide the player through intricate levels, collecting various gems, and uncovering the secrets of the Eldritch Gem. Enjoy a visually appealing experience with assets from OpenGameArt, accompanied by dynamic background music and immersive sound effects.

### Movement

Use the arrow keys to navigate the player through the game world, shift to run.

### Level Design

- Dynamic background music, powered by the `pygame.mixer` module, enhances different game states, providing a seamless and atmospheric experience.
- Sound effects, including the collection of gems, are implemented using the `pygame.sound` module, creating a satisfying and immersive gameplay environment.
- Utilizing assets from OpenGameArt, the game boasts a visually stunning aesthetic that complements the mystical theme.
- Custom Player Camera that moves the map instead of the player. (The YSortCameraGroup() function)
- Completely original collision and tile mapping process! No use of pytmx at all.
- An optional feature to reset game, clear all sprites, etc. to improve performance (Not fully implemented for all stages yet)
- Custom UI using only pygame.

### Visual and Auditory Design

- Two layers of images, background, and foreground, combined with OpenGameArt assets, create a visually appealing and immersive gaming experience.
- Enjoy a rich auditory landscape with carefully chosen background music and satisfying sound effects, enhancing the overall atmosphere of the game.
- Cutscenes made frame by frame in PowerPoint/ GIF images blitted successively onto the screen.
- Transitions made using similar time and blitting logic.
- Map designed in Tiled. The map itself doesn't contain sprites, it is an image. Only the collision's were imported as `.csv` and blitted invisibly onto the map image which optimizes performance keeping in mind pygame's poor performance when there are too many sprites.

### Inventory System

- Collect various gems to affect the player's inventory and stats, adding an extra layer of strategy to your gameplay.
- Collectables Logic implemented, that affect the player's stats. It works through making a Collectable class group and setting their sprites to be kiled and player stat's to chnage on collision using the inbuilt pygame.sprite.Sprite collision methods.

### Enemies

- Overcome challenges posed by enemies, strategically navigating through each level to progress in your quest.
- Currently there are 3 kinds of enemies in-game, each with their own set of properties and abilities.

## How to Run the Game

(A .exe executable will be available soon on releases section!)
1. Ensure that the `pygame` module is installed using the provided command.
```bash
pip install pygame
```
3. Run the game script.

```bash
python main.py
```

Embark on this magical journey, where the combination of OpenGameArt assets and dynamic audio design awaits to transport you into the world of Relic Run!
