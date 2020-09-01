class LeafElement: 

    def __init__(self, *args): 
        self.position = args[0]
         
    def showDetails(self): 
        '''Prints the position of the child element.'''
        print(r'\t', end = '' )
        print(self.position)
        
         
class CompositeElement: 
  
    def __init__(self, *args): 
        self.position = args[0] 
        self.children = [] 

    def add(self, child): 
        self.children.append(child) 
        
    def remove(self, child): 
        self.children.remove(child)
  
    def showDetails(self): 
        print(self.position)
        for el in self.children:
            print(r'\t', end = '' )
            el.showDetails()
