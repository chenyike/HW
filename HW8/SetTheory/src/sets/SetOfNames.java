package sets;
import java.util.*;

public class SetOfNames {
	//Define arraylist's data type
	ArrayList<String> nameSet = new ArrayList<String>();

	/**
	 * Constructor
	 */
	SetOfNames() {
		// make an empty arrayList
		this.nameSet = new ArrayList<String>();
	}


	/**
	 * a method to add an element to the set. It takes a single string and adds it to the set. 
	 */
	void add(String a_string) {
		if (! this.nameSet.contains(a_string)){
			this.nameSet.add(a_string);		
		}
	}


	/**
	 * Add an arrayList into an existing list
	 */
	void add(ArrayList<String> arrayList) {
		for (String a_string : arrayList){
			if (! this.nameSet.contains(a_string)) {
				this.nameSet.add(a_string);
			}
		}
	}


	/**
	 * A different function to add string array to an existing array. Notice that the data type is different
	 */
	void add(String[] array_of_string) {
		for (String a_string : array_of_string){
			if (! this.nameSet.contains(a_string)) {
				this.nameSet.add(a_string);
			}
		}		
	}


	/**
	 * a method to delete a string from the set. 
	 */
	void delete(String a_string) {
		if (this.nameSet.contains(a_string)){
			this.nameSet.remove(a_string);		
		}
	}


	/**
	 * a method to delete a string from the set. 
	 */
	boolean isELementOf(String a_string){
		if (this.nameSet.contains(a_string)) {
			return true;
		}
		return false;
	}


	/**
	 * This method computes the intersection of this set with the other set that is being passed in.
	 *  It returns a set that represents the intersection.
	 */
	public ArrayList<String> intersect (SetOfNames otherSet){
		ArrayList<String> intersection = new ArrayList<String>();
		for(String otherset : otherSet.nameSet ){
			if (this.nameSet.contains(otherset)){
				intersection.add(otherset);
			}
		}
		return intersection;
	}


	/**
	 * This method computes the union of this set with the other set that is being passed in. It return a set that represents the union.
	 */
	public ArrayList<String> union (SetOfNames otherSet){
		ArrayList<String> union = new ArrayList<String>();
		for(String otherset : otherSet.nameSet ){
			union.add(otherset);
		}
		for(String nameset : this.nameSet ){
			union.add(nameset);
		}
		return union;
	}


	/**
	 * This method computes the set that consists of elements in this set that cannot be found in the otherSet. 
	 * Again it returns a set of names.
	 */
	public ArrayList<String> difference (SetOfNames otherSet){
		ArrayList<String> difference = new ArrayList<String>();
		for(String nameset : this.nameSet ){
			if (! otherSet.nameSet.contains(nameset)){
				difference.add(nameset);
			}
		}
		return difference;
	}


	/**
	 * This method returns true (in Java it is in lower case) or false depending upon 
	 * whether all the elements of otherSet can be found in this set.
	 */
	boolean isSubset(SetOfNames otherSet){
		int i = 0;
		for(String otherset : otherSet.nameSet ){
			if (this.nameSet.contains(otherset)){
				i ++;
			}
		}
		if (i == otherSet.nameSet.size()){
			return true;
		}
		return false;
	}


	/**
	 * This method just returns the number of elements in the set.
	 */
	int cardinality(){
		return this.nameSet.size();
	}


	/**
	 * Print out function
	 */
	public String toString() {
		// equivalent of  __str__ method
		if (this.nameSet.size() >0){
			String s = "{";
			// add every name to this nameList
			for (int i = 0; i < this.nameSet.size()-1; i++){
				s += this.nameSet.get(i) + ", ";
			}
			s += this.nameSet.get(this.nameSet.size()-1) + "}";
			return s;
		}
		return "Empty set";
	}


	/**
	 * main function
	 */
	public static void main(String[] args) {
		// initialize everything
		SetOfNames vanHalen = new SetOfNames();
		//System.out.println(vanHalen); 
		String[] namelist = {"Eddie Van Halen", "David Lee Roth", "Alex Van Halen", "Michael Anthony"};
		vanHalen.add(namelist);      //need to ask TA to see if it is OK.
		System.out.println(vanHalen); 
		//Delete an entry
		vanHalen.delete("David Lee Roth");
		System.out.println(vanHalen); 
		//Add an entry
		vanHalen.add("Sammy Hagar");
		System.out.println(vanHalen); 
	}

}
