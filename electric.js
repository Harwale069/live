import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

public class ElectricalEngineeringGame {
    private static int score = 0;
    private static int questionIdx = 0;
    private static List<Question> questions = new ArrayList<>();
    private static JLabel questionLabel;
    private static JTextField entry;

    public static void main(String[] args) {
        // Initialize main window
        JFrame frame = new JFrame("Electrical Engineering Interactive Game");
        frame.setSize(600, 400);
        frame.getContentPane().setBackground(new Color(240, 240, 245));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        // Sample Questions and Answers
        questions.add(new Question("What is the total resistance (R_total) for R1 = 5 Ω and R2 = 3 Ω in series?", 8, "In series circuits, resistances add up."));
        questions.add(new Question("What is the secondary voltage (V_s) for a primary voltage of 131 V and turns ratio of 1.57?", 206.04, "Use V_secondary = V_primary * turns ratio."));

        // Main UI elements
        questionLabel = new JLabel(questions.get(questionIdx).getQuestion());
        questionLabel.setFont(new Font("Arial", Font.PLAIN, 14));
        questionLabel.setPreferredSize(new Dimension(500, 50));
        frame.add(questionLabel);

        entry = new JTextField(10);
        entry.setFont(new Font("Arial", Font.PLAIN, 14));
        frame.add(entry);

        JPanel buttonPanel = new JPanel();
        frame.add(buttonPanel);

        JButton checkButton = new JButton("Submit Answer");
        checkButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                checkAnswer();
            }
        });
        buttonPanel.add(checkButton);

        JButton hintButton = new JButton("Hint");
        hintButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                showHint();
            }
        });
        buttonPanel.add(hintButton);

        JButton calcButton = new JButton("Calculator");
        calcButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                calculator();
            }
        });
        buttonPanel.add(calcButton);

        // Start with the first question
        nextQuestion();

        // Run the main loop
        frame.setVisible(true);
    }

    private static void checkAnswer() {
        String userAnswer = entry.getText();
        try {
            if (Double.parseDouble(userAnswer) == questions.get(questionIdx).getAnswer()) {
                score++;
                JOptionPane.showMessageDialog(null, "Well done! Correct answer.", "Correct!", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(null, "Oops! The correct answer was " + questions.get(questionIdx).getAnswer() + ".", "Incorrect", JOptionPane.INFORMATION_MESSAGE);
            }
            nextQuestion();
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Please enter a numeric value.", "Invalid Input", JOptionPane.WARNING_MESSAGE);
        }
    }

    private static void nextQuestion() {
        questionIdx++;
        if (questionIdx < questions.size()) {
            questionLabel.setText(questions.get(questionIdx).getQuestion());
            entry.setText("");
        } else {
            JOptionPane.showMessageDialog(null, "Final Score: " + score + "/" + questions.size(), "Game Over", JOptionPane.INFORMATION_MESSAGE);
            System.exit(0);
        }
    }

    private static void showHint() {
        JOptionPane.showMessageDialog(null, questions.get(questionIdx).getHint(), "Hint", JOptionPane.INFORMATION_MESSAGE);
    }

    private static void calculator() {
        JFrame calcFrame = new JFrame("Calculator");
        calcFrame.setSize(300, 200);
        calcFrame.setLayout(new FlowLayout());

        JTextField calcEntry = new JTextField(20);
        calcFrame.add(calcEntry);

        JButton calcButton = new JButton("Calculate");
        calcButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    double result = eval(calcEntry.getText());
                    JOptionPane.showMessageDialog(null, "Result: " + result, "Result", JOptionPane.INFORMATION_MESSAGE);
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(null, "Invalid expression", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });
        calcFrame.add(calcButton);

        calcFrame.setVisible(true);
    }

    private static double eval(String expression) {
        // Simple evaluation logic (for demonstration purposes)
        // In a real application, consider using a library for expression evaluation
        return new ScriptEngineManager().getEngineByName("JavaScript").eval(expression);
    }

    static class Question {
        private String question;
        private double answer;
        private String hint;

        public Question(String question, double answer, String hint) {
            this.question = question;
            this.answer = answer;
            this.hint = hint;
        }

        public String getQuestion() {
            return question;
        }

        public double getAnswer() {
            return answer;
        }

        public String getHint() {
            return hint;
        }
    }
}

