from Player import Player

player = Player("SuperCrazyLazy")

game=True
while(game):
    if(player.play()):
        print("PLAY")