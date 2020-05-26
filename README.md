# digu_card_game
A card game played in the Maldives built using python with some simple logic.

This game uses pygame and tkinter libraries.

Below are the instructions on how Digu is played.

As the game starts player will be asked to toss a coin to decide if player or computer calls trumps.
Trumps are decided normally by checking the player's hand and selecting the most amount of cards with the same suit.
The higher the value of the trump is an added advantage.

Once a trump suit is selected, the game can begin.
The person who calls trumps gets the first play. For now its just the computer or player.
There are four players in this game.  Two players in two teams (Team 1 - computer and computer's teammate, Team 2 - player and player's teammate).  
For now the computer manages computer, computer's teammate and player's teammate.
The person who plays will play from the player's hand.
There will be a total of 13 rounds and each round will select a winning hand(four cards that were played in that round) obtained by one of the players from the four.

Once a card is played at the beginnig of the round, the rest of the players will have to follow with that suit if they have in their hands.  The highest value will be awarded the win of the hand for that round.  If in case you dont have a suit that is played, you can play a trump card and win the hand depending if another player didnt play a higher value trump card than what you played.

At the end of 13th round the number of hands obtained by each player are counted and the player with highest number of hands wins.

For the win, The player and player's teammates hands are added and the computer and computer's teammates hands are added and checked if player or computer win.

NOTE: In the actual game the player who wins the hand in that round gets to play first, but for now i have just started with the player who calls trumps gets to play first in every round.  Will make changes soon.  I Welcome any changes and modification.

Thank you.



