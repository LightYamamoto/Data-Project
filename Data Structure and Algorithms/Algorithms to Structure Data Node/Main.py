from MyPerson import Operation

class Main(Operation):
    def run(self):

       
        menu= '''
        +-------------------Menu------------------+

        Person Tree:
        1. Load the data from the file.
        2. Insert a new Person.
        3. Inorder traverse
        4. Breadth-First Traversal traverse
        5. Search by Person ID
        6. Delete by Person ID
        0. Exit

        +-----------------------------------------.+

        '''
        while True:
            print(menu)
            x= input('Please input the choice: ')
            if x == '1': 
                self.load()
            elif x=='2':
                self.insert()
            elif x=='3':
                self.InorderTraversal()
            elif x=='4':
                self.BFS()
            elif x=='5':
                self.SearchByID()
            elif x=='6':
                self.DeleteByID()
            elif  x=='0':
                print('Thanks')
                break
            else:
                print('Don\'t have option. Please press again!')
                pass

################################################################################
if __name__ == '__main__':
    main = Main()
    main.run()