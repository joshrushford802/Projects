import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();
    // Instance variables (if needed)

    public static void main(String[] args) {
    	Scanner scnr = new Scanner(System.in);
        String userInput = "";

        initializeDogList();
        initializeMonkeyList();

        // Print the menu, prompt the user for input, and execute the action(s) based on that input.
        // Furthermore, check user input and if it's invalid, re-prompt until they enter a valid option.
        while (true) {
        	displayMenu();
    		userInput = scnr.nextLine();
    		
        	if (!userInput.equals("1") && !userInput.equals("2") && !userInput.equals("3") && !userInput.equals("4") &&
        		!userInput.equals("5") && !userInput.equals("6") && !userInput.equals("q")) {
        		System.out.println("Invalid input");
        	} else if (userInput.equals("1")) {
        		intakeNewDog(scnr);
        	} else if (userInput.equals("2")) {
        		intakeNewMonkey(scnr);
        	} else if (userInput.equals("3")) {
        		reserveAnimal(scnr);
        	} else if (userInput.equals("4")) {
        		printAnimals("dogs");
        	} else if (userInput.equals("5")) {
        		printAnimals("monkies");
        	} else if (userInput.equals("6")) {
        		printAnimals("availability");
        	// If user types "q", break the loop and end the program
        	} else {
        		break;
        	}
        }

    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }

    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", true, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", false, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }

    // Adds monkeys to a list for testing
    //Optional for testing
    public static void initializeMonkeyList() {
    	Monkey monkey1 = new Monkey("Ben", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States", "10", "9", "5", "Tamarin");
    	Monkey monkey2 = new Monkey("Zander", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", true, "United States", "10", "9", "5", "Tamarin");
    	Monkey monkey3 = new Monkey("Toby", "female", "4", "25.6", "12-12-2019", "Canada", "in service", false, "Canada", "10", "9", "5", "Tamarin");

        monkeyList.add(monkey1);
        monkeyList.add(monkey2);
        monkeyList.add(monkey3);
    }

    // Complete the intakeNewDog method
    // The input validation to check that the dog is not already in the list
    // is done for you
    public static void intakeNewDog(Scanner scanner) {
    	
        System.out.println("What is the dog's name?");
        String name = scanner.nextLine();
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu
            }
        }
        
        System.out.print("Breed: ");
		String breed = scanner.nextLine();
        System.out.print("Gender: ");
		String gender = scanner.nextLine();
		System.out.print("Age: ");
		String age = scanner.nextLine();
		System.out.print("Weight: ");
		String weight = scanner.nextLine();
		System.out.print("Acquisition Date: ");
		String acquisitionDate = scanner.nextLine();
		System.out.print("Acquisition Country: ");
		String acquisitionCountry = scanner.nextLine();		
		System.out.print("Country in Service: ");
		String inServiceCountry = scanner.nextLine();
		
		// Add monkey to the array
		dogList.add(new Dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry,
						"intake", false, inServiceCountry));
		
		// Confirm to the user that the monkey has been added to the system
		System.out.println("\n\nDog Added\n\n");
        
    }

    	// Prompt the user for the information required to form a new item for the monkeyList array,
    	// and add that item to the array
        public static void intakeNewMonkey(Scanner scanner) {
        	String species = "";
        	
            System.out.print("Monkey Name: ");
            String name = scanner.nextLine();
            
            // Checks if monkey is already in the system
            for(Monkey monkey: monkeyList) {
                if(monkey.getName().equalsIgnoreCase(name)) {
                    System.out.println("\n\nThis monkey is already in our system\n\n");
                    return; //returns to menu
                }
            }
            
            System.out.print("Gender: ");
    		String gender = scanner.nextLine();
    		System.out.print("Age: ");
    		String age = scanner.nextLine();
    		System.out.print("Weight: ");
    		String weight = scanner.nextLine();
    		System.out.print("Acquisition Date: ");
    		String acquisitionDate = scanner.nextLine();
    		System.out.print("Acquisition Country: ");
    		String acquisitionCountry = scanner.nextLine();   		
    		System.out.print("Country in Service: ");
    		String inServiceCountry = scanner.nextLine();
    		System.out.print("Tail Length: ");
    		String tailLn = scanner.nextLine();
    		System.out.print("Height: ");
    		String hght = scanner.nextLine();
    		System.out.print("Body Length: ");
    		String bodyLn = scanner.nextLine();
    		
    		while (!species.equalsIgnoreCase("Capuchin") && !species.equalsIgnoreCase("Guenon") && !species.equalsIgnoreCase("Macaque")
    				 && !species.equalsIgnoreCase("Marmoset") && !species.equalsIgnoreCase("Squirrel Monkey") && !species.equalsIgnoreCase("Tamarin")) {
    			System.out.print("Species (Capuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, or Tamarin): ");
    			species = scanner.nextLine();
    			
    			if (!species.equalsIgnoreCase("Capuchin") && !species.equalsIgnoreCase("Guenon") && !species.equalsIgnoreCase("Macaque")
       				 && !species.equalsIgnoreCase("Marmoset") && !species.equalsIgnoreCase("Squirrel Monkey") && !species.equalsIgnoreCase("Tamarin")) {
    				System.out.println("Please enter a valid option");
    			}
    		}
    		
    		// Add monkey to the array
    		monkeyList.add(new Monkey(name, gender, age, weight, acquisitionDate, acquisitionCountry,
    						"intake", false, inServiceCountry, tailLn, hght, bodyLn, species));
    		
    		// Confirm to the user that the monkey has been added to the system
    		System.out.println("\n\nMonkey Added\n\n");
        }

        // Complete reserveAnimal
        // You will need to find the animal by animal type and in service country
        public static void reserveAnimal(Scanner scanner) {
        	String animalType;
        	String country;
        	String name;
        	String temp = "";
        	int i = 1;
        	
            System.out.println("Enter animal type: ");
            animalType = scanner.nextLine();
            System.out.println("Enter country: ");
            country = scanner.nextLine();
            System.out.println("Animal name: ");
            name = scanner.nextLine();
            System.out.println("Set reservation status (Y or N): ");
            temp = scanner.nextLine();
            
            // Set reservation status to true or false for a dog or a monkey
            if (animalType.equalsIgnoreCase("dog")) {
            	for(Dog dog: dogList) {
                    if((!dog.getName().equalsIgnoreCase(name) || !dog.getInServiceLocation().equalsIgnoreCase(country)) && i == dogList.size()) {
                        System.out.println("\n\nThis dog is not in our system\n\n");
                        return; //returns to menu
                    } else if (dog.getName().equalsIgnoreCase(name) && dog.getInServiceLocation().equalsIgnoreCase(country) && temp.equalsIgnoreCase("Y")) {
                    	dog.setReserved(true);
                    	System.out.println("Reservation Status updated to true");
                    	return;
                    } else if (dog.getName().equalsIgnoreCase(name) && dog.getInServiceLocation().equalsIgnoreCase(country) && temp.equalsIgnoreCase("N")) {
                    	dog.setReserved(false);
                    	System.out.println("Reservation Status updated to false");
                    	return;
              
                    }
                    
                    i += 1;
                }
            	i = 0;
            } else if (animalType.equalsIgnoreCase("monkey")) {
            	for(Monkey monkey: monkeyList) {
                    if((!monkey.getName().equalsIgnoreCase(name) || !monkey.getInServiceLocation().equalsIgnoreCase(country)) && i == monkeyList.size()) {
                        System.out.println("\n\nThis monkey is not in our system\n\n");
                        return; //returns to menu
                    } else if (monkey.getName().equalsIgnoreCase(name) && monkey.getInServiceLocation().equalsIgnoreCase(country) && temp.equalsIgnoreCase("Y")) {
                    	monkey.setReserved(true);
                    	System.out.println("Reservation Status updated to true");
                    	 return;
                    } else if (monkey.getName().equalsIgnoreCase(name) && monkey.getInServiceLocation().equalsIgnoreCase(country) && temp.equalsIgnoreCase("N")) {
                    	monkey.setReserved(false);
                    	System.out.println("Reservation Status updated to false");
                    	 return;
                    }
                    
                    i += 1;
                }
            	i = 0;
            }

        }

        // Complete printAnimals
        // Include the animal name, status, acquisition country and if the animal is reserved.
	// Remember that this method connects to three different menu items.
        // The printAnimals() method has three different outputs
        // based on the listType parameter
        // dog - prints the list of dogs
        // monkey - prints the list of monkeys
        // available - prints a combined list of all animals that are
        // fully trained ("in service") but not reserved 
	// Remember that you only have to fully implement ONE of these lists. 
	// The other lists can have a print statement saying "This option needs to be implemented".
	// To score "exemplary" you must correctly implement the "available" list.
        public static void printAnimals(String action) {
            
        	if (action.equals("dogs")) {
        		for(Dog dog: dogList) {
        			System.out.println();
                    System.out.println(dog.getName());
                    System.out.println(dog.getBreed());
                    System.out.println(dog.getGender());
                    System.out.println(dog.getAge());
                    System.out.println(dog.getWeight());
                    System.out.println(dog.getAcquisitionDate());
                    System.out.println(dog.getAcquisitionLocation());
                    System.out.println(dog.getTrainingStatus());
                    System.out.println(dog.getReserved());
                    System.out.println(dog.getInServiceLocation());
                    System.out.println();
                }
        	} else if (action.equals("monkies")) {
        		for(Monkey monkey: monkeyList) {
        			System.out.println();
                    System.out.println(monkey.getName());
                    System.out.println(monkey.getGender());
                    System.out.println(monkey.getAge());
                    System.out.println(monkey.getWeight());
                    System.out.println(monkey.getAcquisitionDate());
                    System.out.println(monkey.getAcquisitionLocation());
                    System.out.println(monkey.getTrainingStatus());
                    System.out.println(monkey.getReserved());
                    System.out.println(monkey.getInServiceLocation());
                    System.out.println(monkey.getTailLength());
                    System.out.println(monkey.getHeight());
                    System.out.println(monkey.getBodyLength());
                    System.out.println(monkey.getSpecies());
                    System.out.println();
                }
        	} else if (action.equals("availability")) {
        		
        		// Print dogs and monkies who's reservation status is set to "false" and training status is set to "in service"
        		System.out.println("In-service & available monkies:");
        		for(Monkey monkey: monkeyList) {
        			if (monkey.getReserved() == false && monkey.getTrainingStatus() == "in service") {
	        			System.out.println();
	                    System.out.println("Name: " + monkey.getName());
	                    System.out.println("Gender: " + monkey.getGender());
	                    System.out.println("Age: " + monkey.getAge());
	                    System.out.println("Weight: " + monkey.getWeight());
	                    System.out.println("Acquisition Date: " + monkey.getAcquisitionDate());
	                    System.out.println("Acquisition Location: " + monkey.getAcquisitionLocation());
	                    System.out.println("In-Service Location: " + monkey.getInServiceLocation());
	                    System.out.println("Tail Length: " + monkey.getTailLength());
	                    System.out.println("Height: " + monkey.getHeight());
	                    System.out.println("Body Length: " + monkey.getBodyLength());
	                    System.out.println("Species: " + monkey.getSpecies());
	                    System.out.println();
        		    }
                }
        		
        		System.out.println();
        		
        		System.out.println("In-service & available dogs:");
        		for(Dog dog: dogList) {
        			if (dog.getReserved() == false && dog.getTrainingStatus() == "in service") {
        				System.out.println();
                        System.out.println("Name: " + dog.getName());
                        System.out.println("Breed: " + dog.getBreed());
                        System.out.println("Gender: " + dog.getGender());
                        System.out.println("Age: " + dog.getAge());
                        System.out.println("Weight: " + dog.getWeight());
                        System.out.println("Acquisition Date: " + dog.getAcquisitionDate());
                        System.out.println("Acquisition Location: " + dog.getAcquisitionLocation());
                        System.out.println("In-Service Location: " + dog.getInServiceLocation());
                        System.out.println();
        		    }
                }
        	}
            
        }
}
