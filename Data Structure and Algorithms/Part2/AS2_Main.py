from OperationToProduct import OperationToProduct

class AS2_Main(OperationToProduct):
    def menu(self):
        MENU ='''
        +-----------------Menu------------------+
        |   1.Load data for file and display    |
        |   2.input & add to the end            |
        |   3.Display data                      |
        |   4.Save product list to file         |
        |   5.Search by ID                      |
        |   6.Delete by ID                      |
        |   7.Sort by ID                        |
        |   8.Convert to Binary                 |    
        |   9.Load to stack and display         |    
        |   10.Load to queue and display        |    
        |   0.Exit                              |    
        '''
        print(MENU)
        x = input('Please enter the choice: ')
        if x == '1':
            self.load()
            print('Thanks!!!')
        elif x =='2':
            self.append()
        elif x =='3':
            self.display()
        elif x =='4':
            self.saveProductListToFile()
        elif x =='5':
            self.searchByID()
        elif x =='6':
            self.deletebyID()
        elif x =='7':
            self.sortByID()
        elif x =='8':
            self.convertToBinary()
        elif x =='9':
            self.loadToStackAndDisplay()
        elif x =='10':
            self.loadToQueueAndDisplay()
        elif x =='0':
            return
        else:
            print('No option, please enter a choice again: ')
        return self.menu()
        

main = AS2_Main()
main.menu()