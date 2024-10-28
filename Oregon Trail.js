import java.util.*;
import java.io.*;
import java.util.concurrent.*;

public class OregonTrailDeluxe {

    // Constants
    private static final int START_MONEY = 100;
    private static final int DISTANCE_GOAL = 1000;
    private static final int START_HEALTH = 100;
    private static final int START_FOOD = 50;
    private static final int START_WATER = 40;
    private static final int START_STAMINA = 100;
    private static final int START_MORALE = 75;
    private static final int FOOD_PER_TRAVEL = 10;
    private static final int WATER_PER_TRAVEL = 5;
    private static final int STAMINA_PER_TRAVEL = 10;
    private static final int MORALE_LOSS_TRAVEL = 5;
    private static final int EVENT_COUNTDOWN = 3;
    private static final boolean DEBUG_MODE = false;

    // Events, terrains, and professions
    private static final String[] EVENTS = {
        "You encounter a wild animal!",
        "A storm is approaching.",
        "You meet a stranger who offers you food.",
        "You find a river to rest by.",
        "A band of hostile travelers attacks you!",
        "You find an abandoned cabin.",
        "You discover a hidden stash of supplies.",
        "You stumble upon a lost traveler who needs help.",
        "You experience a miraculous turn of luck!",
        "A local merchant offers rare goods."
    };

    private static final String[] TERRAINS = {"Desert", "Forest", "Mountains", "Plains", "River"};
    private static final String[] WEATHERS = {"Sunny", "Rainy", "Snowy", "Windy"};
    private static final String[] PROFESSIONS = {"Hunter", "Fisher", "Trapper", "Merchant", "Traveler"};

    // Player stats
    private static String playerName = "";
    private static int health = START_HEALTH;
    private static int food = START_FOOD;
    private static int water = START_WATER;
    private static int stamina = START_STAMINA;
    private static int morale = START_MORALE;
    private static int money = START_MONEY;
    private static int milesTraveled = 0;
    private static int daysPassed = 0;
    private static Map<String, Integer> inventory = new HashMap<>();
    private static List<String> companions = new ArrayList<>();
    private static int eventCounter = EVENT_COUNTDOWN;
    private static String difficulty = "";
    private static String pace = "Normal";

    // Color themes
    private static final Map<String, String> THEMES = new HashMap<>();
    static {
        THEMES.put("default", "\033[0m");
        THEMES.put("red", "\033[91m");
        THEMES.put("green", "\033[92m");
        THEMES.put("yellow", "\033[93m");
        THEMES.put("blue", "\033[94m");
        THEMES.put("magenta", "\033[95m");
        THEMES.put("cyan", "\033[96m");
        THEMES.put("white", "\033[97m");
    }

    // ASCII visuals
    private static final Map<String, String> ASCII_VIEWS = new HashMap<>();
    static {
        ASCII_VIEWS.put("river", """
                 ~ ~ ~
               ~       ~
             ~~~~~~~~~~~~
            """);
        ASCII_VIEWS.put("cabin", """
                ___
               /   \\
              |     |
              |_____|
            """);
    }

    // Game save slots
    private static final int SAVE_SLOTS = 5;
    private static final String SAVE_FILE_PREFIX = "save_game_";

    // Function to run a separate console for displaying actions
    private static void runConsole() {
        ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
        executor.scheduleAtFixedRate(() -> {
            System.out.printf("Current Stats: Health: %d, Food: %d, Water: %d, Stamina: %d, Morale: %d, Money: %d, Miles Traveled: %d, Days Passed: %d%n",
                    health, food, water, stamina, morale, money, milesTraveled, daysPassed);
        }, 0, 3, TimeUnit.SECONDS);
    }

    // Introduction
    private static void displayIntro() {
        System.out.println("Welcome to Oregon Trail Deluxe Edition!");
        System.out.println("Your goal is to survive the treacherous journey to Oregon.");
        System.out.println("Make wise choices and manage your resources well!");
        System.out.printf("You have a starting balance of $%d.%n", START_MONEY);
        chooseProfession();
    }

    // Profession selection
    private static void chooseProfession() {
        System.out.println("Choose your profession:");
        for (int i = 0; i < PROFESSIONS.length; i++) {
            System.out.printf("%d. %s%n", i + 1, PROFESSIONS[i]);
        }
        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt() - 1;
        String profession = PROFESSIONS[choice];
    }

    // Display player stats
    private static void displayStats() {
        System.out.println("\nCurrent Stats:");
        System.out.printf("Health: %d%n", health);
        System.out.printf("Food: %d%n", food);
        System.out.printf("Water: %d%n", water);
        System.out.printf("Stamina: %d%n", stamina);
        System.out.printf("Morale: %d%n", morale);
        System.out.printf("Money: $%d%n", money);
        System.out.printf("Miles Traveled: %d%n", milesTraveled);
        System.out.printf("Days Passed: %d%n", daysPassed);
    }

    // Function to handle traveling
    private static void travel() {
        if (food <= 0 || water <= 0 || stamina <= 0) {
            System.out.println("You can't travel anymore. You need food, water, or rest!");
            return;
        }

        // Change pace based on player choice
        Scanner scanner = new Scanner(System.in);
        System.out.print("Choose your pace (Normal, Fast, Slow): ");
        String paceChoice = scanner.nextLine();
        pace = Arrays.asList("Normal", "Fast", "Slow").contains(paceChoice) ? paceChoice : "Normal";

        int distance = new Random().nextInt(51) + 50;  // Random travel distance between 50 and 100
        if (pace.equals("Fast")) {
            distance *= 1.5;
            stamina -= 15;
        } else if (pace.equals("Slow")) {
            distance *= 0.75;
            stamina -= 5;
        }

        milesTraveled += distance;
        food -= FOOD_PER_TRAVEL;
        water -= WATER_PER_TRAVEL;
        stamina -= STAMINA_PER_TRAVEL;
        morale -= MORALE_LOSS_TRAVEL;
    }

    public static void main(String[] args) {
        // Initialize game
        inventory.put("medicine", 0);
        inventory.put("ammunition", 0);
        inventory.put("tools", 0);

        displayIntro();
        runConsole();
    }
}

