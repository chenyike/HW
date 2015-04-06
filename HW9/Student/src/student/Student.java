package student;

public class Student {
	//Define directory's data type
	String name;
	double totalScore;
	int numberOfHw;


	/**
	 * Constructor
	 */
	Student(String name, double totalScore, int numberOfHw) {
		// allocate space for HashMap
		this.name = name;
		this.totalScore = totalScore;
		this.numberOfHw = numberOfHw;
	}


	/**
	 * Get the name
	 */
	String getName() {
		return this.name;
	}


	/**
	 * Add HW Score
	 */
	void addHWScore(double score){
		this.totalScore += score;
	}


	/**
	 * get total score
	 */
	double getTotalScore() {
		if (this.numberOfHw > 0) {
			return this.totalScore;
		}
		return 0;
	}


	/**
	 * get average score
	 */
	double getAverageScore() {
		if (this.numberOfHw > 0){
			return this.totalScore/this.numberOfHw;
		}
		return 0;
	}


	/**
	 * toString Function
	 */
	public String toString() {
		return "Student " + this.name + " has " + this.numberOfHw + " homework(s) on file," + " the total score of which is " + this.totalScore + ". " ;
	}


}
