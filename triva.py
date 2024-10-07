import random

# Questions for different difficulty levels
questions_easy = [
    {"question": "What is the capital of France?", "choices": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Which animal is known as the 'King of the Jungle'?", "choices": ["Tiger", "Lion", "Elephant", "Bear"], "answer": "Lion"},
    {"question": "What is the largest ocean on Earth?", "choices": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "choices": ["Shakespeare", "Dickens", "Hemingway", "Tolkien"], "answer": "Shakespeare"},
    {"question": "What is the boiling point of water?", "choices": ["50°C", "100°C", "150°C", "200°C"], "answer": "100°C"},
    {"question": "What is the main ingredient in guacamole?", "choices": ["Tomato", "Avocado", "Pepper", "Onion"], "answer": "Avocado"},
    {"question": "Which gas do we breathe in?", "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Oxygen"},
    {"question": "What is the square root of 16?", "choices": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "In what continent is Egypt located?", "choices": ["Africa", "Asia", "Europe", "Australia"], "answer": "Africa"},
    {"question": "What is the capital city of Australia?", "choices": ["Sydney", "Canberra", "Melbourne", "Brisbane"], "answer": "Canberra"},
    {"question": "What is the currency of Japan?", "choices": ["Yuan", "Won", "Yen", "Dollar"], "answer": "Yen"},
    {"question": "What is the main language spoken in Brazil?", "choices": ["Spanish", "Portuguese", "French", "English"], "answer": "Portuguese"},
    {"question": "How many continents are there?", "choices": ["5", "6", "7", "8"], "answer": "7"}
]

questions_medium = [
    {"question": "Which planet is the hottest in the solar system?", "choices": ["Mars", "Venus", "Mercury", "Jupiter"], "answer": "Venus"},
    {"question": "What is the longest river in the world?", "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "Who painted the Mona Lisa?", "choices": ["Van Gogh", "Picasso", "Da Vinci", "Rembrandt"], "answer": "Da Vinci"},
    {"question": "What is the capital of Canada?", "choices": ["Toronto", "Ottawa", "Vancouver", "Montreal"], "answer": "Ottawa"},
    {"question": "What is the powerhouse of the cell?", "choices": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"], "answer": "Mitochondria"},
    {"question": "Which element has the chemical symbol 'O'?", "choices": ["Osmium", "Oxygen", "Gold", "Iron"], "answer": "Oxygen"},
    {"question": "Which country is known as the Land of the Rising Sun?", "choices": ["China", "Japan", "Thailand", "Vietnam"], "answer": "Japan"},
    {"question": "What is the capital of Italy?", "choices": ["Milan", "Venice", "Rome", "Florence"], "answer": "Rome"},
    {"question": "What is the hardest natural substance on Earth?", "choices": ["Gold", "Iron", "Diamond", "Quartz"], "answer": "Diamond"},
    {"question": "Who discovered penicillin?", "choices": ["Fleming", "Einstein", "Curie", "Pasteur"], "answer": "Fleming"},
    {"question": "What is the largest desert in the world?", "choices": ["Sahara", "Arabian", "Gobi", "Kalahari"], "answer": "Sahara"},
    {"question": "What is the chemical formula for water?", "choices": ["H2O", "CO2", "O2", "H2"], "answer": "H2O"},
    {"question": "What is the main language spoken in Egypt?", "choices": ["Arabic", "English", "French", "Spanish"], "answer": "Arabic"},
    {"question": "What is the smallest prime number?", "choices": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "What year did the Titanic sink?", "choices": ["1905", "1912", "1918", "1920"], "answer": "1912"}
]

questions_hard = [
    {"question": "What is the capital of Iceland?", "choices": ["Reykjavik", "Oslo", "Copenhagen", "Helsinki"], "answer": "Reykjavik"},
    {"question": "Who wrote the Iliad?", "choices": ["Homer", "Virgil", "Ovid", "Plato"], "answer": "Homer"},
    {"question": "What is the second largest country in the world by area?", "choices": ["Canada", "United States", "China", "Brazil"], "answer": "Canada"},
    {"question": "What is the main ingredient in hummus?", "choices": ["Chickpeas", "Lentils", "Peas", "Beans"], "answer": "Chickpeas"},
    {"question": "In which year did World War I begin?", "choices": ["1912", "1914", "1916", "1918"], "answer": "1914"},
    {"question": "Which Shakespeare play features the characters Oberon and Titania?", "choices": ["A Midsummer Night's Dream", "Macbeth", "Hamlet", "Othello"], "answer": "A Midsummer Night's Dream"},
    {"question": "What is the capital of Bhutan?", "choices": ["Thimphu", "Katmandu", "Dhaka", "Lhasa"], "answer": "Thimphu"},
    {"question": "What is the main ingredient in a traditional Japanese sushi?", "choices": ["Rice", "Noodles", "Fish", "Seaweed"], "answer": "Rice"},
    {"question": "Which scientist proposed the laws of motion?", "choices": ["Einstein", "Newton", "Galileo", "Hawking"], "answer": "Newton"},
    {"question": "What is the largest organ in the human body?", "choices": ["Liver", "Heart", "Skin", "Lung"], "answer": "Skin"},
    {"question": "In what year was the first manned moon landing?", "choices": ["1965", "1969", "1972", "1975"], "answer": "1969"},
    {"question": "What is the chemical symbol for potassium?", "choices": ["K", "P", "Na", "Ca"], "answer": "K"},
    {"question": "Which philosopher is known for the statement 'I think, therefore I am'?", "choices": ["Plato", "Aristotle", "Descartes", "Kant"], "answer": "Descartes"},
    {"question": "Which organ is primarily responsible for detoxification in the body?", "choices": ["Heart", "Liver", "Kidneys", "Lungs"], "answer": "Liver"},
    {"question": "Which famous scientist developed the first successful polio vaccine?", "choices": ["Albert Sabin", "Jonas Salk", "Edward Jenner", "Louis Pasteur"], "answer": "Jonas Salk"}
]

questions_type_in = [
    {"question": "Name a color in the rainbow.", "answer": ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]},
    {"question": "What is the capital city of Japan?", "answer": ["Tokyo"]},
    {"question": "Who wrote 'Pride and Prejudice'?", "answer": ["Jane Austen"]},
    {"question": "What gas do plants absorb from the atmosphere?", "answer": ["Carbon Dioxide", "CO2"]},
    {"question": "In which continent is Egypt located?", "answer": ["Africa"]},
    {"question": "What is the chemical formula for table salt?", "answer": ["NaCl"]},
    {"question": "What is the largest planet in our solar system?", "answer": ["Jupiter"]},
    {"question": "What is the name of the longest river in South America?", "answer": ["Amazon"]},
    {"question": "What is the square root of 144?", "answer": ["12"]},
    {"question": "Name a type of cloud.", "answer": ["Cumulus", "Stratus", "Cirrus", "Nimbus"]},
    {"question": "What is the hardest natural substance on Earth?", "answer": ["Diamond"]},
    {"question": "What is the main ingredient in a Caesar salad dressing?", "answer": ["Garlic", "Lemon", "Olive Oil", "Parmesan"]},
    {"question": "What is the fastest land animal?", "answer": ["Cheetah"]},
    {"question": "Name a musical instrument.", "answer": ["Piano", "Guitar", "Violin", "Drums"]},
    {"question": "What is the capital city of Italy?", "answer": ["Rome"]}
]

# Function to run the trivia game
def run_trivia_game():
    print("WELCOME TO ALEX HARWOOD'S CLI TRIVIA GAME".center(80, ' '))
    print()
    
    total_score = 0
    rounds = int(input("How many rounds would you like to play? "))
    
    difficulty = input("Select difficulty (easy, medium, hard, type-in): ").strip().lower()
    
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}/{rounds}")
        if difficulty == 'easy':
            questions = random.sample(questions_easy, 5)
        elif difficulty == 'medium':
            questions = random.sample(questions_medium, 5)
        elif difficulty == 'hard':
            questions = random.sample(questions_hard, 5)
        elif difficulty == 'type-in':
            questions = random.sample(questions_type_in, 5)
        else:
            print("Invalid difficulty. Exiting the game.")
            return

        for question in questions:
            if difficulty == 'type-in':
                print(question["question"])
                answer = input("Your answer: ")
                if answer in question["answer"]:
                    print("Correct!\n")
                    total_score += 1
                else:
                    print(f"Wrong! The correct answer(s) are: {', '.join(question['answer'])}\n")
            else:
                print(question["question"])
                for i, choice in enumerate(question["choices"], 1):
                    print(f"{i}. {choice}")
                answer = input("Select the correct answer (1, 2, 3, or 4): ")
                if answer.isdigit() and 1 <= int(answer) <= 4:
                    if question["choices[int(answer)-1]"] == question["answer"]:
                        print("Correct!\n")
                        total_score += 1
                    else:
                        print(f"Wrong! The correct answer is: {question['answer']}\n")
                else:
                    print("Invalid choice. Please select a number between 1 and 4.\n")

    print(f"Game Over! Your total score is: {total_score}/{rounds * 5}")

# Run the trivia game
if __name__ == "__main__":
    run_trivia_game()
