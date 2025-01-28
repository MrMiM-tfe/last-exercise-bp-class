# 6 Questions from basic programming class in university

Last Exercise

Q1_ Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

Q2_ You are designing a banking system where customers can have savings or checking accounts. The system tracks deposits, withdrawals, and account balances.

Example input output :

Input:
1. Create Savings Account for Alice with $1000 (Interest Rate: 5%)
2. Create Checking Account for Bob with $500
3. Deposit $200 to Bob's account
4. Withdraw $100 from Alice's account
5. Apply interest to Alice's account
6. Transfer $300 from Alice to Bob
7. Display balances

Output:
Savings account created for Alice with balance: $1000
Checking account created for Bob with balance: $500

Deposited $200 to Bob's account. New balance: $700
Withdrawn $100 from Alice's account. New balance: $900

Interest applied to Alice's account. New balance: $945

Transferred $300 from Alice to Bob.
Alice's new balance: $645
Bob's new balance: $1000

Final Balances:
- Alice (Savings Account): $645
- Bob (Checking Account): $1000

Q3 _ Design an online multiplayer game where players can join rooms, chat, and play a turn-based card game.
 Hints: * Create a Player class with attributes: name, id, room, score, and hand (list of cards).
*create Game,Server Class . 
* create Room class with attributes room_name, players , chat_history

Example input output :
Input:
1. Create Room: "Fantasy Arena"
2. Player Alice joins "Fantasy Arena"
3. Player Bob joins "Fantasy Arena"
4. Alice sends message: "Hello, Bob!"
5. Bob sends message: "Ready to play?"
6. Start a game: Turn 1
   - Alice plays card: 8
   - Bob plays card: 10
7. Display scores.

Output:
Room "Fantasy Arena" created.

Alice joined "Fantasy Arena."
Bob joined "Fantasy Arena."

Chat History:
- Alice: Hello, Bob!
- Bob: Ready to play?

Game Started: Fantasy Arena
Turn 1:
- Alice played: 8
- Bob played: 10
Winner: Bob

Current Scores:
- Alice: 0
- Bob: 1

Q4_ write Tic Tac Toe with OOP 
Hints :
•  Grid Initialization:
•	Use a 2D list to represent the board. Each cell starts as " " (empty space).
•	Example: self.grid = [[" " for _ in range(3)] for _ in range(3)].
•  Displaying the Board:
•	Use loops to print the board in a structured way.
•	Separate rows with a line (e.g., -----) and columns with |.
•  Check if the Board is Full:
•	Use nested loops or a one-liner with all() to verify all cells are filled.
•  Placing a Marker:
•	Before placing the marker, ensure the cell is empty (" "). If it’s already occupied, reject the move.
•  Checking for a Winner:
•	Check rows: Loop through each row and see if all cells contain the same marker.
•	Check columns: Loop through column indices and see if all cells in that column match the marker.
•	Check diagonals: Use list indices to check the two diagonals.

Example Input Output : 
Alice's turn. You are 'X'.
Enter your move (row and column): 0 2

Here is the updated board:
X|X|X
-----
 |O| 
-----
 | |O

Q5_ Cleaning and Manipulating Data : create dataframe like this :
Student,Math,English,Science
Alice,85,78,92
Bob,90,88,84
Charlie,NaN,76,89
David,72,95,NaN
Eve,88,85,91
1.	Load the data into a pandas DataFrame.
2.	Find and fill all missing values (NaN) with the value 0.
3.	Calculate the average score for each student across all subjects. Add it as a new column Average.
4.	Find the student(s) with the highest average score.
5.	Save the modified DataFrame into a new file called cleaned_grades.csv.

Q6_ create a To-Do list application , containing these items:
1-	Create the Data Structure for a To-Do Item
2-	Add a New To-Do Task
3-	Mark a Task as Completed
4-	Delete a Task
5-	Filter Tasks by Status (Incomplete/Completed)
6-	Sort Tasks by Priority
7-	Search for a Task by Description


Extra point Question:
Q1_ Sudoku Solver Game in Python using OOP
A Sudoku solver is a program that solves a given Sudoku puzzle by filling in the empty spaces with the correct numbers according to Sudoku rules. The rules are:
1.	Every row must contain the digits 1-9 without repetition.
2.	Every column must contain the digits 1-9 without repetition.
3.	Every 3x3 subgrid (also called a "box") must contain the digits 1-9 without repetition.
Approach to Solve Sudoku using OOP:
1.	SudokuBoard: A class that represents the entire Sudoku board. It will store the board's state and provide methods for checking validity and displaying the board.
2.	Solver: A class that contains the algorithm to solve the Sudoku puzzle using a backtracking approach.
