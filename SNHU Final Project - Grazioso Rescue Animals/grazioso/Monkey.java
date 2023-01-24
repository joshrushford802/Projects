public class Monkey extends RescueAnimal {

	// Instance variables
	private String tailLength;
	private String height;
	private String bodyLength;
	private String species;
	
	// Constructor
	public Monkey(String name, String gender, String age,
	String weight, String acquisitionDate, String acquisitionCountry,
	String trainingStatus, boolean reserved, String inServiceCountry, String tailLn,
	String hght, String bodyLn, String spcies) {
		setName(name);
		setGender(gender);
		setAge(age);
		setWeight(weight);
		setAcquisitionDate(acquisitionDate);
		setAcquisitionLocation(acquisitionCountry);
		setTrainingStatus(trainingStatus);
		setReserved(reserved);
		setInServiceCountry(inServiceCountry);
		setTailLength(tailLn);
		setHeight(hght);
		setBodyLength(bodyLn);
		setSpecies(spcies);
		setAnimalType("monkey");

	}
	
	public void setTailLength(String tailLn) {
		tailLength = tailLn;
	}
	
	public String getTailLength() {
		return tailLength;
	}
	
	public void setHeight(String hght) {
		height = hght;
	}
	
	public String getHeight() {
		return height;
	}
	
	public void setBodyLength(String bodyLn) {
		bodyLength = bodyLn;
	}
	
	public String getBodyLength() {
		return bodyLength;
	}
	
	public void setSpecies(String spcies) {
		species = spcies;
	}
	
	public String getSpecies() {
		return species;
	}
	
}
