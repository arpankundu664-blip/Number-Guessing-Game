# 🎯 Number Guessing Game

A simple and interactive **Number Guessing Game** built with **Python** and **Streamlit**.

The computer randomly selects a number between **1 and 100**, and the player has to guess the number. After every guess, the game gives a hint to go **higher** or **lower** until the correct number is found.

## 🚀 Features

* 🎲 Random number generation between 1 and 100
* 🎯 Interactive guessing interface
* ⬆️ Hint when the guessed number is too low
* ⬇️ Hint when the guessed number is too high
* 🔢 Tracks the number of attempts
* 🎉 Shows a success message when the correct number is guessed
* 🔄 New Game option
* 🌐 Browser-based UI using Streamlit

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Random module**

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── app.py
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Number-Guessing-Game
```

### 3. Install Streamlit

```bash
pip install streamlit
```

## ▶️ Run the Application

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, the local URL will be:

```text
http://localhost:8501
```

## 🎮 How to Play

1. Start the application.
2. Enter a number between **1 and 100**.
3. Click the **Guess** button.
4. Follow the hint:

   * ⬆️ **Go higher** → Your guess is too low.
   * ⬇️ **Go lower** → Your guess is too high.
5. Continue guessing until you find the correct number.
6. The game displays how many attempts you used.
7. Click **New Game** to start again.

## 🧠 How It Works

The game uses Python's `random` module to generate a random number:

```python
random.randint(1, 100)
```

The player's guess is then compared with the randomly generated number.

```text
             Start Game
                  ↓
        Generate Random Number
             (1 - 100)
                  ↓
          Enter Your Guess
                  ↓
        Compare With Number
           ↙       ↓       ↘
        Lower    Correct   Higher
          ↓        ↓         ↓
       Guess     🎉 Win    Guess
       Again                Again
```

## 📸 Application

The application provides a simple and clean browser-based interface where users can enter their guesses, receive hints, and track their attempts.

## 🔮 Future Improvements

Some possible improvements are:

* 🏆 Add a high-score system
* ⏱️ Add a timer
* 🎚️ Add different difficulty levels
* 💾 Store game history
* 🎨 Improve the UI with custom CSS
* 👥 Add multiplayer mode
* 📊 Show statistics such as average attempts

## 👨‍💻 Author

ARPAN KUNDU
Built with ❤️ using Python and Streamlit.

## 📄 License

This project is open-source and available for learning and educational purposes.
