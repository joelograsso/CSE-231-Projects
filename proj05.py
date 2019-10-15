#
#project 05
# Functions/ File input and output/ try-accept/algorithims
# This program asks for a .off file, then displays a list of options. Countiniously 
# asks user for  a valid integer with a loop. Calls to a functions in the menu
# and asks user for appropriate inputs. Executes appropriate response. 
# displays closing message once program has ended
#
import math
def display_options():
    ''' 
    This function displayes the menu of options.
    '''
    
    menu = '''\nPlease choose an option below:
        1- display the information of the first 5 faces
        2- compute face normal
        3- compute face area
        4- check two faces connectivity
        5- use another file
        6- exit
       '''
       
    print(menu)    
def open_file():
    '''
    Trys to open valid .off files. The function takes no paramaters and returns
    the valid file.
    '''
    valid_file = False    
    while valid_file == False:
        try:
            file_name = input("Enter an <off> file name: ")    #inputs user for a file
            file = open(file_name,'r')    #tries to open the file
            valid_file = True    #changes valid file to true, breaking the loop
        except FileNotFoundError:    #if the file cannot be found
            print("Error. Please try again")
            valid_file = False    #keeps valid file false to keep loop going
    return file    #returns the file
            
def check_valid(fp,index,shape):
    '''
    This function takes in 3 inputs, the file, the index, and the shape 
    (vertex or faces), and checks to see if the index is valid. If it is valid
    it returns True else it returns False.
    '''
    if shape == 'face':
        if index.isdigit() == False:
            return False    #returns false if it is not a digit
        else:
            index = int(index)
            if 0 <= index < total_faces(fp):    
                return True    #if 0 =< index < total # faces in the file, returns True
            else:   
                return False    #if index is negative or greater than total # faces, retrun False
    elif shape == 'vertex':
        if index.isdigit() == False:
            return False
        else:
            index = int(index)
            if 0 <= index < total_vert(fp):
                return True    #if 0 =< index < total # verticies in the file, returns True
            else:
                return False    #if index is negative or greater than total # verticies, retrun False
            
def read_face_data(fp, index):
    '''
    This function takes in 2 parameters, the file and the face index. It searches
    through all the vertex data then reads through the face data to the specified
    index. It returns the three verticies of the face as an int.
    '''
    index = int(index)
    fp.seek(0)# move to the beginning of the file -- necessary for multiple calls to this function
    fp.readline()     # read OFF in file
    fp.readline()     # read total number of verticies, faces, and edges in file
    coords_line = fp.readline()    #index 0 of coordinates 
    while coords_line[1] != '3':    #loops until coords_line = index 0 face value
        coords_line = fp.readline()    #read next line
    face_line0 = coords_line    #index 0 face line values = index 0 face values
    if index > 0: 
        for i in range(index - 1):
            fp.readline()    #skip line
        index_file = fp.readline() 
        v1 = int(index_file[2:7].strip())    #vertex 1 are the numbers in slicing index 2-7
        v2 = int(index_file[7:12].strip())
        v3 = int(index_file[12:].strip())
    else:    #if index = 0
        index_file = face_line0    
        v1 = int(index_file[2:7].strip())
        v2 = int(index_file[7:12].strip())
        v3 = int(index_file[12:].strip())
    return v1,v2,v3    #returns 3 verticies of face index

def read_vertex_data(fp, index):
    '''
    This function takes in 2 parameters, the file and the vertex index. It then
    searches through the vertex data to the certain index and slices the information.
    It returns the three coordinates of the vertex as a float.
    '''
    index = int(index)
    fp.seek(0)# move to the beginning of the file -- necessary for multiple calls to this function
    fp.readline()
    fp.readline()
    for i in range(index):
        fp.readline()
    index_file = fp.readline() 
    x = float(index_file[0:16].strip())    #x coordinate is the float in slicing index 0-16
    y = float(index_file[16:31].strip())
    z = float(index_file[31:].strip())
    return x,y,z    #returns x,y,z coordinates of vertex index       

def compute_cross(v1,v2,v3,w1,w2,w3):
    '''
    This function computes the cross product between two sides of a face.
    It takes in two sets of coordinates and returns 3 coordinates of the cross 
    product returned as floats rounded 5 decimal places
    '''
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)
    w1 = float(w1)
    w2 = float(w2)
    w3 = float(w3)
    num1 = (v2*w3) - (v3*w2)
    num2 = (v3*w1) - (v1*w3)
    num3 = (v1*w2) - (v2*w1)
    num1 = round(num1,5)
    num2 = round(num2,5)
    num3 = round(num3,5)
    return num1, num2, num3    #returns 3 coordinates rounded 5 decimal points 

def compute_distance(x1,y1,z1,x2,y2,z2):
    '''
    This function computes the Euclidian distance between two points and returns 
    the distance rounded 2 decimal places. It takes in 2 sets of verticies and
    converts them to floats, then uses Euclidian distance to find the distance.
    '''
    x1 = float(x1)  
    x2 = float(x2)
    y1 = float(y1)
    y2 = float(y2)
    z1 = float(z1)
    z2 = float(z2)
    distance = math.sqrt((((x1-x2)**2) + ((y1-y2)**2) + ((z1-z2)**2)))    #Euchlidian distance formula
    distance = round(distance,2)
    return distance    #returns distance rounded 2 decimal places

def compute_face_normal(fp, face_index):
    '''
    This function computes the normal vector of a face. Its parameters are the 
    file and the face index. Locates the face vertex index, then seeks those vertex 
    coordinates. Use coordinaters to find two sides(vectors) and then compute the 
    cross product of the two vectors. Returns the 3 normal vector coordinates of 
    the face index.
    '''
    first, second, third = read_face_data(fp, face_index)    #finds verticies of face
    x1,y1,z1 = read_vertex_data(fp, first)    #reads first vertex coordinates at vertex index
    x2,y2,z2 = read_vertex_data(fp, second)
    x3,y3,z3 = read_vertex_data(fp, third)
    side1_x, side1_y,side1_z= x2-x1,y2-y1,z2-z1    #finds the difference of x/y/z
    side2_x,side2_y,side2_z = x3-x1, y3-y1, z3-z1  #coordinates to form vectors
    normal_x,normal_y,normal_z = compute_cross(side1_x, side1_y, side1_z, side2_x, side2_y, side2_z)
    return normal_x, normal_y, normal_z    #returns the x,y,z coordinates of normal vector

def compute_face_area(fp, face_index):
    '''
    This function computes the face area. Its parameters are the file and the 
    face index. Locates the face vertex information, then seeks those vertex 
    coordinates. Use coordinaters to find 3 sides by using the Euclidian distance
    function of the two coordinates. Then uses Heron's formula to compute the area 
    and returns the area rounded 2 decimal places.
    '''
    first, second, third = read_face_data(fp, face_index)
    x1,y1,z1 = read_vertex_data(fp, first)
    x2,y2,z2 = read_vertex_data(fp, second)
    x3,y3,z3 = read_vertex_data(fp, third)
    ab = compute_distance(x1,y1,z1,x2,y2,z2)    #find distance of two verticies
    ac = compute_distance(x1,y1,z1,x3,y3,z3)
    bc = compute_distance(x3,y3,z3,x2,y2,z2)
    P = (ab+ac+bc)/2    #constant for Heron's formula
    area = math.sqrt(P*(P-ab)*(P-ac)*(P-bc))    #Heron's formula
    area = round(area,2)
    return area    #returns area rounded 2 decimal places

def is_connected_faces(fp, f1_ind, f2_ind):
    '''
    This function checks if two faces are connected by seeing if they share two
    common verticies. It accepts the file and two face index values. It then 
    stores the second face data as variables. Then loops through 3 time evaluating 
    the value of read_face_data(fp,f1_ind)[i] to each value of face 2. If any 
    values are equal to each other, 1 is added to the counter. If there are 2 
    common verticies, it returns True else it returns False
    '''
    face2_x, face2_y, face2_z = read_face_data(fp, f2_ind)
    counter = 0    #counter of common verticies
    i = 0    #interval
    while i < 3:
        if read_face_data(fp,f1_ind)[i] == face2_x:
            counter += 1
            i += 1
        elif read_face_data(fp,f1_ind)[i] == face2_y:
            counter += 1
            i += 1
        elif read_face_data(fp,f1_ind)[i] == face2_z:
            counter += 1
            i += 1
        else:
            i+=1
    if counter == 2:
        return True    #if there are 2 common verticies, return True
    else:
        return False    #if there are less than 2 common verticies, return False

def total_vert(fp):
    '''
    This function takes in the file and returns the total number of verticies in 
    the file
    '''
    fp.seek(0)
    fp.readline()
    line = fp.readline()
    total = int(line[0:6])
    return total

def total_faces(fp):
    '''
    This function takes in the file and returns the total number of faces in the
    file
    '''
    fp.seek(0)
    fp.readline()
    line = fp.readline()
    total = int(line[6:11])
    return total
        
def main():
    '''
    This function calls to open a file, then prompts the user with a list of options
    and continuiously asks the user for a choice. If choice is not a valid integer 
    an error is prompted and user is asked again. If choice is 1, the first 5 faces
    will be displayed of the file. Then asks for choice again. If choice is 2, 
    the normal vector coordinates are displayed. Will prompt for face index and
    check if it is valid. Will ask until valid input is entered. If choice is 3,
    the area of the face will be computed. Will continue to prompt user for a 
    valid face index, and display and error if invalid. Then ask for a choice again.
    If choice is 4, it will check to see if two faces are connected. It will prompt 
    the user for 2 face index values that are valid, and reprompt until 2 valid 
    indexes are inputed. then will display correct message if the are of are not 
    connected. Then reprompt the user with options and choice. If choice is 5,
    the file will be changed by entering another valid .off file. If choice is
    6, the progrm is ended.
    '''
    print('''\nWelcome to Computer Graphics!
\tWe are creating and handling shapes. Any shape can be represented by polygon meshes, 
\twhich is a collection of vertices, edges and faces.''')
    choice = ' '
    file = open_file()
    display_options()
    choice = input(">> Choice: ")
    while choice != '6':
        if choice == '1':
            i = 0
            print("{:^7s}{:^15s}".format('face','vertices'))
            while i < 5:
                face = read_face_data(file,i)
                V1 = face[0]    #reads first vertex
                V2 = face[1]    #reads second vertex
                V3 = face[2]    #reads third vertex
                #prints the face index and corresponding verticies
                print('{:>5d}{:>5d}{:>5d}{:>5d}'.format(i,V1,V2,V3))    
                i += 1              
            display_options()    #display options 
            choice = input(">> Choice: ")    #prompts for choice
        elif choice == '2':
            VALID = False    #constant for loop
            face_index = input("Enter face index as integer: " )     #prompts face index
            while VALID == False:
                if face_index.isdigit() == False:    #checks to see if index is not a digit
                    print("This is not a valid face index.")
                    face_index = input("Enter face index as integer: " )
                    VALID = False
                else:
                    face_index = int(face_index)
                    if 0 <= face_index < total_faces(file):    #checks to make sure 
                        VALID = True                    #index is in range of file
                    else:    #if index > total # faces in file
                        print("This is not a valid face index.")
                        face_index = input("Enter face index as integer: " )
                        VALID = False
            norm1,norm2,norm3 = compute_face_normal(file, face_index)    #stores 3 values of normal vector
            print("The normal of face {}:{:>9.5f}{:>9.5f}{:>9.5f}".format(face_index, norm1,norm2,norm3))
            display_options()
            choice = input(">> Choice: ")
        elif choice == '3':
            VALID = False
            face_index = input("Enter face index as integer: " )
            while VALID == False:    #checks to make sure index is valid
                if face_index.isdigit() == False:
                    print("This is not a valid face index.")
                    face_index = input("Enter face index as integer: " )
                    VALID = False
                else:
                    face_index = int(face_index)
                    if 0 <= face_index < total_faces(file):
                        VALID = True
                    else:
                        print("This is not a valid face index.")
                        face_index = input("Enter face index as integer: " )
                        VALID = False
            print("The area of face {}:{:>9.2f}".format(face_index, compute_face_area(file, face_index)))
            display_options()
            choice = input(">> Choice: ")
        elif choice == '4':
            VALID1 = False    #constant for first face index
            VALID2 = False    #constant for second face index
            face_index1 = input("Enter face 1 index as integer: ")
            while VALID1 == False:    #checks that first face index is valid
                if face_index1.isdigit() == False:
                    print("This is not a valid face index.")
                    face_index1 = input("Enter face 1 index as integer: " )
                    VALID1 = False
                else:
                    face_index1 = int(face_index1)
                    if 0 <= face_index1 < total_faces(file):
                        VALID1 = True
                    else:
                        print("This is not a valid face index.")
                        face_index1 = input("Enter face 1 index as integer: " )
                        VALID1 = False
            face_index2 = input("Enter face 2 index as integer: ")
            while VALID2 == False:    #checks that second face index is valid
                if face_index2.isdigit() == False:
                    print("This is not a valid face index.")
                    face_index2 = input("Enter face 2 index as integer: ")
                    VALID2 = False
                else:
                    face_index2 = int(face_index2)
                    if 0 <= face_index2 < total_faces(file):
                        VALID2 = True
                    else:
                        print("This is not a valid face index.")
                        face_index2 = input("Enter face 2 index as integer: ")
                        VALID2 = False
            if is_connected_faces(file,face_index1,face_index2) == True:
                print("The two faces are connected.")
                display_options()
                choice = input(">> Choice: ")
            else:
                print("The two faces are NOT connected.")
                display_options()
                choice = input(">> Choice: ")
        elif choice == '5':
            file = open_file()
            display_options()
            choice = input(">> Choice: ")
        else:
            try:
                choice_int = int(choice)    #turn choice into an int
                if choice_int == 0 or choice_int > 6:    #if choice isn't and int 1-7
                     print("Please choose a valid option number.")
                     choice = input(">> Choice: ")
            except ValueError:    #if choice can't turn into int
                print("Please choose a valid option number.")
                choice = input(">> Choice: ")    #asks for choice again
    else:    #when choice = 6
      print("Thank you, Goodbye!")  
       
    
# Do not modify the next two lines.
if __name__ == "__main__":
    main()