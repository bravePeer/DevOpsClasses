import kod
import pytest

class Testing:
    def test_sub(self):
        assert kod.sub(3,5) == -2, "should be -2"
    
    def test_mul(self):
        assert kod.mul(2,2) == 4, "should be 4"

    def test_div(self):
        assert kod.div(8, 2) == 4, "should be 4"
         
    def test_div_by_0(self):
        with pytest.raises(Exception, match="Can't divide by 0"):
            kod.div(2, 0) 
             
    def test_mean(self):
        assert kod.mean([3,4,5]) == 4, "should be 4"