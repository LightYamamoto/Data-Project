#Nhập một dãy các số thực gồm có n số (n<=20)  lưu vào tệp INPUT.TXT
class Sort:
    def __init__(self):
        self.n= None
        self.data=None
    #1. Thiết kế menu   
    def menu(self):
        return'''
        +-------------------Menu------------------+

|      1.Manual Input                 |

|      2.File input                        |

|      3.Bubble sort                    |

|      4.Selection sort                 |

|      5.Insertion sort                  |

|      6.Search > value                |

|      7.Search = value                |

|      0.Exit                              |

+-----------------------------------------.+'''
    

    def option(self):
        print(self.menu())
        x=int(input('Please input option you want to do '))
        if x==1:
            self.input_data()
        elif x==2:
            self.output_data()
        elif x==3:
            self.BubbleSort()
        elif x==4:
            self.SelectionSort()
        elif x==5:
            self.InsertSort()
        elif x==6:
            self.LinearSearch()
        elif x==7:
            self.BinarySearch()
        elif x==0:
            print('Thanks!!!')
        else:
            print('Please input the corect number of the above menu')



        self.option()
    def input_data(self):
        with open('INPUT.TXT','w') as f:
            f.writelines([input('Please enter input number of elements: '),'\n'])
            f.write(input("Please enter input elements: "))        
        
    #Đọc dữ liệu từ tệp INPUT.TXT lưu vào mảng 1 chiều a và hiển thị ra màn hình
    def output_data(self):
        with open("INPUT.TXT",'r') as d:
            self.n=int(d.readline().strip())
            data = d.readline()
            self.data = list(map(float,data.strip().split()))

        with open(input("Please enter the file path:"),"w+") as f:           
            f.write('Input array:'+ str(self.data)) 
        print(self.data)                      
        return self.data

#Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Bubble Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT1.TXT
    def BubbleSort(self):
        arr=self.data.copy()
        n=len(arr)
        with open('OUTPUT1.TXT','w') as f:           
            for i in range(n):
                for j in range(n-1,i,-1):
                    if arr[j]<arr[j-1]:
                        arr[j],arr[j-1]=arr[j-1],arr[j]
                st = ' '.join(list(map(str, arr)))        
                print(st+'\n')                
            f.write(str(arr))
            self.sorted_arr=arr            
            return self.sorted_arr

#Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Selection Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT2.TXT
    def SelectionSort(self):
        with open('OUTPUT2.TXT','w') as f2:
            arr1=self.data.copy()
            n=len(arr1)
            for i in range(n):
                minIndex=i
                for j in range(i+1,n):
                    if arr1[j]<arr1[i]:
                        minIndex=j
                arr1[i], arr1[minIndex] = arr1[minIndex], arr1[i]
                st=' '.join(list(map(str,arr1)))
                print(st+'\n')
            f2.write(str(arr1))
            
            return arr1
    #Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Insert Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT3.TXT
    def InsertSort(self):
        arr2=self.data.copy()
        n=len(arr2)
        with open('OUTPUT3.TXT','w') as f:
            for i in range(1,n):
                for j in range(i,0,-1):
                    if arr2[j-1]>arr2[j]:
                        arr2[j-1],arr2[j]=arr2[j],arr2[j-1]
                st=' '.join(list(map(str,arr2)))
                print(st+'\n')
            f.write(str(arr2))            
        return arr2
#Sử dụng phương pháp tìm kiếm tuần tự, hãy liệt kê ra màn hình chỉ số các phần tử (biết rằng phần tử đầu tiên có chỉ số là 0) trong mảng a  chưa được sắp xếp ở câu 2 có giá trị lớn hơn value (value là một số thực được nhập vào từ bàn phím), kết quả tìm được lưu vào dòng tiếp theo trong tệp OUTPUT4.TXT
    def LinearSearch(self):
        arr3=self.sorted_arr.copy()
        list_Index=[]
        val=float(input("Please enter searched input value:"))
        with open('OUTPUT4.TXT',"w") as f:
            for i in range(len(arr3)):
                if arr3[i]>val:
                    list_Index.append(str(i))
            a=' '.join(str(i) for i in list_Index)
            f.write(a)
        print(f'Larger position:{a}')
        return a
#Sử dụng phương pháp tìm kiếm nhị phân, hãy tìm chỉ số phần tử đầu tiên có giá trị bằng value (value là một số thực được nhập vào từ bàn phím) trên mảng a đã được sắp xếp.
    def BinarySearch(self):
        #a=self.BubbleSort().copy()
        a=self.sorted_arr.copy()
        print(a)
        val=float(input('Please enter searched input value:'))
        n=len(a)-1        
        l=0
        r=len(a)-1
        while (l<=r):            
            mid=(l+r)//2
            if val==a[mid]:
                print(f'The right position: {mid}')
                return mid            
            elif val<a[mid]:
                r=mid-1
            else:
                l=mid+1
        
                
        print("Khong co gia tri can tim")
        
                


        
            

data=Sort()
data.option()
