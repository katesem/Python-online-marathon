class Testpaper:
    
    def __init__(self, subject, markscheme = [], pass_mark = None):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    
    def __init__(self,tests_taken = "No tests taken",**kwargs):
        if not kwargs:
            self.tests_taken = tests_taken
        else:
            self.tests_taken = kwargs

    
    def take_test(self, testpaper, answer = []):
        mark,res = 0, {}
        for el in answer :
            if el in testpaper.markscheme:
                mark += 1
                
        perc = str(round(mark / len(testpaper.markscheme)*100)) +"%"
        res[testpaper.subject] = ("Passed! " if testpaper.pass_mark <= perc \
                                            else "Failed! ") +"("+perc+")"

        if type(self.tests_taken) == dict:
            self.tests_taken = {**self.tests_taken, **res}
        else:
            self.tests_taken = res
            
