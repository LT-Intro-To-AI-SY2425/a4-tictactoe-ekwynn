# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

    Creating the has_won method was difficult because I had to visualize which indexes are which and which one was the right combinations, which made it actually very confusing. 

2. Explain how you would add a computer player to the game.
    Adding a computer to the game would require there to be an automated response. This could be done by just iterating through the board list to see where there is an open spot and the AI would just randomly generate X or O.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

    Have the AI iterate through all correct combinations after each turn and whichever combination is on the board, then the AI will play the next turn that would allow it to have the winning position.