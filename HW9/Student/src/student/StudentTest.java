package student;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class StudentTest {
	Student std1;
	Student std2;
	Student std3;
	Student std4;
	
	@Before
	public void setUp() throws Exception {
		std1 = new Student("xxx",99.9,1);
		std2 = new Student("yyy",200.0,2);
		std3 = new Student("zzz",0,0);	
		std4 = new Student("aaa",88.8,0);
	}

	
	
	@Test
	public void testGetName() {
		assertEquals( this.std1.getName(), "xxx" ) ;
		assertEquals( this.std2.getName(), "yyy" ) ;
		assertEquals( this.std3.getName(), "zzz" ) ;
	}
	

	@Test
	public void testAddHWScore() {
		double previousScore = std1.totalScore;
		this.std1.addHWScore(97.2);
		double currentScore = std1.totalScore;
		//System.out.println(currentScore - previousScore);
		assertEquals((currentScore - previousScore), 97.2, 0.00000001);
		
	}

	
	@Test
	public void testGetTotalScore() {
		assertEquals( this.std1.getTotalScore(), 99.9, 0.00000001 );
		assertEquals( this.std2.getTotalScore(), 200, 0.00000001 );
		assertEquals( this.std3.getTotalScore(), 0.0, 0.00000001 );
		// if there is a typo, meaning if numberOfHw is zero, but total score is not, then we still treat this score as zero
		assertEquals( this.std4.getTotalScore(), 0.0, 0.00000001 );
	}

	
	@Test
	public void testGetAverageScore() {
		assertEquals( this.std1.getAverageScore(), 99.9, 0.00000001) ;
		assertEquals( this.std2.getAverageScore(), 100.0, 0.00000001) ;
		// if number of Hw is zero, no matter there are toalScore or not, average is zero
		assertEquals( this.std3.getAverageScore(), 0, 0.00000001) ;
		assertEquals( this.std4.getAverageScore(), 0, 0.00000001) ;
	}

	
	@Test
	public void testToString() {
		assertEquals( this.std1.toString(), "Student xxx has 1 homework(s) on file, the total score of which is 99.9. " );
		assertEquals( this.std2.toString(), "Student yyy has 2 homework(s) on file, the total score of which is 200.0. " );
		assertEquals( this.std3.toString(), "Student zzz has 0 homework(s) on file, the total score of which is 0.0. " );
		assertEquals( this.std4.toString(), "Student aaa has 0 homework(s) on file, the total score of which is 88.8. " );

	}

}
