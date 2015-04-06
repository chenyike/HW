package sets;
import static org.junit.Assert.*;
import java.util.ArrayList;
import org.junit.Before;
import org.junit.Test;

public class SetOfNamesTest {
	SetOfNames testSet;
	SetOfNames otherSet;
	SetOfNames otherSet2;
	SetOfNames otherSet3;

	@Before
	public void setUp() throws Exception {
		testSet = new SetOfNames();
		otherSet = new SetOfNames();
		otherSet2 = new SetOfNames();
		otherSet3 = new SetOfNames();
	}


	@Test
	public void testAddString() {
		testSet.add("Eddie Van Halen");
		assertTrue(testSet.nameSet.contains( "Eddie Van Halen"));
		int previous_size = testSet.nameSet.size();
		//if add this again, the size of testSet should remain the same
		testSet.add("Eddie Van Halen");
		int current_size = testSet.nameSet.size();
		assertEquals(previous_size, current_size,0.00001);
	}


	/**
	 * for modularity purpose, not a testing function
	 */
	public void array_creation() {
		ArrayList<String> array = new ArrayList<String>();
		array.add("Eddie Van Halen");
		array.add("David Lee Roth");
		testSet.add(array);

		//otherSet has element that could not be found in testSet, but also has element that is in testSet
		otherSet.add("Alex Van Halen");
		otherSet.add("David Lee Roth");
		otherSet.add( "Michael Anthony");		

		//otherSet2 is a subset of testSet
		otherSet2.add("David Lee Roth");
		
		//otherSet3 contains an element could not be found in testSet
		otherSet3.add("Michael Anthony");
	}


	@Test
	public void testAddArrayListOfString() {

		array_creation();
		assertTrue(testSet.nameSet.contains( "Eddie Van Halen"));
		assertTrue(testSet.nameSet.contains( "David Lee Roth"));
		int previous_size = testSet.nameSet.size();
		// if add this again, the size of testSet should remain the same.
		// meaning, we are not adding the same thing again and again
		array_creation();
		int current_size = testSet.nameSet.size();
		assertEquals(previous_size, current_size, 0.00001);
	}


	@Test
	/**
	 * Test a different array adding function that I created
	 */
	public void testAddStringArray() {
		String[] namelist = {"Eddie Van Halen", "David Lee Roth"};
		testSet.add(namelist);
		assertTrue(testSet.nameSet.contains( "Eddie Van Halen"));
		assertTrue(testSet.nameSet.contains( "David Lee Roth"));	
		int previous_size = testSet.nameSet.size();
		// if add this array again, the size of testSet should remain the same.
		// meaning, we are not adding the same thing again and again
		testSet.add(namelist);
		int current_size = testSet.nameSet.size();
		assertEquals(previous_size, current_size, 0.00001);
	}


	@Test
	public void testDelete() {
		array_creation();
		testSet.delete("David Lee Roth");
		// test delete function
		assertFalse(testSet.nameSet.contains( "David Lee Roth"));	
		// test if delete function affects something else
		assertTrue(testSet.nameSet.contains( "Eddie Van Halen"));
	}


	@Test
	public void testIsELementOf() {
		array_creation();
		assertTrue(testSet.isELementOf( "David Lee Roth"));	
		// test a non-existing name
		assertFalse(testSet.isELementOf( "Eddie Halen"));
	}


	@Test
	public void testToString() {
		//test empty set scenario
		assertEquals(testSet.toString(),  "Empty set");
		array_creation();
		assertEquals(testSet.toString(), "{Eddie Van Halen, David Lee Roth}");	
	}


	@Test
	public void testIntersect() {
		array_creation();
		assertTrue(testSet.intersect(otherSet).contains("David Lee Roth") );	
		assertFalse(testSet.intersect(otherSet).contains("Eddie Van Halen") );	
		// check if testSet intersect otherSet equals an empty set
		assertEquals(testSet.intersect(otherSet3).size(),0,0.0);
	}


	@Test
	public void testUnion() {
		array_creation();
		assertTrue(testSet.union(otherSet).contains("David Lee Roth") );	
		assertTrue(testSet.union(otherSet).contains("Eddie Van Halen") );	
		assertTrue(testSet.union(otherSet).contains("Alex Van Halen") );	
		assertTrue(testSet.union(otherSet).contains("Michael Anthony") );	
		//check if David Lee Roth has been added twice, if the size equals 5 then it is fine.
		assertEquals(testSet.union(otherSet).size(),5,0.0);
		// second check
		assertEquals(testSet.union(otherSet3).size(),3,0.0);
	}


	@Test
	public void testDifference() {
		array_creation();
		assertTrue(testSet.difference(otherSet).contains("Eddie Van Halen") );	
		assertFalse(testSet.difference(otherSet).contains("Alex Van Halen") );	
		assertFalse(testSet.difference(otherSet).contains("Michael Anthony") );	
		assertFalse(testSet.difference(otherSet).contains("David Lee Roth") );	
		//check size of the difference set, which is more accurate.
		assertEquals(testSet.difference(otherSet2).size(),1, 0.0);
		//third check
		assertEquals(testSet.difference(otherSet3).size(),2 ,0.0);
	}


	@Test
	public void testIsSubset() {
		array_creation();
		assertTrue(testSet.isSubset(otherSet2));
		assertFalse(testSet.isSubset(otherSet));

	}


	@Test
	public void testCardinality() {
		array_creation();
		assertEquals(testSet.cardinality(),2,0);
		assertEquals(otherSet.cardinality(),3,0);
		assertEquals(otherSet2.cardinality(),1,0);
	}

}
