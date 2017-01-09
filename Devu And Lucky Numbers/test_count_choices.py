import unittest
import sum_of_lucky_combinatorial

class TestCountChoices(unittest.TestCase):
	known_values = [(0,0,0,1,0),
					(1,1,1,1,3),
					(1,1,1,2,6),
					(1,2,3,1,3),
					(1,2,3,2,8),
					(1,2,3,3,19),
					(3,5,9,1,3),
					(3,5,9,2,9),
					(3,5,9,10,28712),
					(3,5,9,9,11965)
					]
	def test_count_choices(self):
		for x,y,z,d,count in self.known_values:
			try:
				returned_count = sum_of_lucky_combinatorial.count_choices(x,y,z,d)
				self.assertEqual(count, returned_count)
			except AssertionError:
				print "Failed at ", x, y, z, d, count, "and printed", returned_count
			
if __name__ == "__main__":
	unittest.main()