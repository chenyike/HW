package telephones;
import java.util.*;
public class TelephoneDirectory {
	//Define directory's data type
	HashMap<String, String> directory;
	
	/**
	 * Constructor
	 */
	TelephoneDirectory() {
		// allocate space for HashMap
		this.directory = new HashMap<String, String>();
	}


	/**
	 * return the directory entries one by one. Ensure that the directory is returned in sorted order.
	 */
	public String toString() {
		// equivalent of  __str__ method
		String s = "";
		Set<String> names = this.directory.keySet();
		ArrayList<String> nameList = new ArrayList<String>();
		// add every name to this nameList
		for (String name: names){
			nameList.add(name);
		}
		//Sort this list
		Collections.sort(nameList);
		//put into String s
		for (String name : nameList){
			s += name + ": " + this.directory.get(name)+"\n";
		}
		return s;
	}

	
	/**
	 * Add a name and phone number to database	 
	 **/
	void addEntry(String name, String number) {
		//add a single new person to the directory.
		// phone number will be a string in the xxx-xxx-xxxx format.
		if ( ! this.directory.keySet().contains(name)) {
			this.directory.put(name, number);
		}
	}

	
	/**
	 * get the number based on the name	 
	 **/
	String getNumber(String name) {
		//get the number based on the name
		if ( this.directory.keySet().contains(name)) {
			return this.directory.get(name);
		}
		return "This person is not in the directory.";	
	}

	
	/**
	 * get the name based on the phone number
	 **/
	String whoCalled(String searchPhone) {
		//get the name based on the number
		for (String name : this.directory.keySet()) {
			if (this.directory.get(name).equals(searchPhone)) {
				return name;
			}
		}
		return "This phone number is not in the directory";
	}


	/**
	 * given a source directory, copy all names to this directory, make sure any existing information is not destroyed.
	 */
	void copyDirectory(TelephoneDirectory sourceDirectory) {
		//CopyDirectory
		this.directory.putAll(sourceDirectory.directory);
	}

	
	/**
	 * main function
	 */
	public static void main(String[] args) {
		// main function
		TelephoneDirectory td = new TelephoneDirectory();
		td.addEntry("Dawn","551-421-4032");
		td.addEntry("Arvind","266-123-1111");
		TelephoneDirectory td1 = new TelephoneDirectory();
		td1.addEntry("Tyke","913-232-4851");
		td1.copyDirectory(td);
		System.out.println("Here are all the entries in the directory");
		System.out.println(td1); 
		//search the directory for Arvind
		String number = td1.getNumber("Arvind") ;
		System.out.println("Arvind's number is: "+number+". ");
		//test whoCalled function
		String whoCalled = td1.whoCalled("551-421-4032");
		System.out.println("551-421-4032"+", "+"aka, "+whoCalled+" Just called. ");
	}

}
