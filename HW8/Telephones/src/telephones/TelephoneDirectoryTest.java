package telephones;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class TelephoneDirectoryTest {

	TelephoneDirectory testAccount;

	@Before
	public void setUp() throws Exception {
		//it runs before everything else
		this.testAccount = new TelephoneDirectory();
	}


	@Test
	public void testAddEntry() {
		this.testAccount.addEntry("xxx","000-000-0000");
		assertEquals("000-000-0000", this.testAccount.directory.get("xxx"));
	}


	@Test
	public void testGetNumber() {
		//search a non-existing person
		assertEquals( this.testAccount.getNumber("xxx"), "This person is not in the directory.") ; 
		// add an entry and then search it
		this.testAccount.addEntry("xxx","000-000-0000");
		assertEquals( this.testAccount.getNumber("xxx"), "000-000-0000") ; 
	}

	
	@Test
	public void testWhoCalled() {
		//search a non-existing phone number
		assertEquals( this.testAccount.whoCalled("000-000-0000"), "This phone number is not in the directory") ; 
		// add an entry and then search it
		this.testAccount.addEntry("xxx","000-000-0000");
		assertEquals( this.testAccount.whoCalled("000-000-0000"), "xxx") ; 
	}

	
	@Test
	public void testCopyDirectory() {
		TelephoneDirectory td = new TelephoneDirectory();
		td.addEntry("Dawn","551-421-4032");
		td.addEntry("Arvind","266-123-1111");
		testAccount.addEntry("Tyke","913-232-4851");
		testAccount.copyDirectory(td);
		assertEquals( this.testAccount.directory.get("Tyke"), "913-232-4851") ; 
		assertEquals( this.testAccount.directory.get("Dawn"), "551-421-4032") ; 

	}



}
