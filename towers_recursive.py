import time #import time module 


def move(from_,to_,disk):#define move function with three parameters
    
    return (f"disk {disk} from {from_} -> to {to_}\n")#returns result string 

def towers(n, from_,to_,aux_):#define recursive function 
    
    result = []#initialize empty result string 
    
    if n == 0:#establish base case 
        return result 
    
    else:
        result.extend(towers(n-1, from_,aux_,to_))#first recrusive call 
        result.append(move(from_,to_,n))#prints move, keeps track of n 
        result.extend(towers(n-1, aux_,to_,from_))#second recursive call 
   
   return result #returns result so that it can be written to output file 
        



def extractinputfiles(filename,outputfile):
   
   #opens and reads input file
    with open(filename, 'r') as file:
        lines = file.readlines() #makes lines equal to the lines in input file  
        with open(outputfile, 'w') as RecurOutputs:#opens and writes to RecurOutputs.txt
            for line in lines:#iterates through input file
                line = line.strip()#strips white spaces from lines  
                if line:#ignores blank spaces
                    
                    if not line.isdigit():
                        RecurOutputs.write(f"Invalid input '{line}'")#error checking,makes sure value is an integer
                        continue
                    
                    num_disk = int(line)#stores integer value from input file into a variable
                    total_moves = (2**num_disk)-1#calculates total moves to be echoed into output file 
                    start = time.perf_counter()#starts timer 
                    output = towers(num_disk,'A','C','B')#first instance of the function 
                    end = time.perf_counter()#ends timer 
                    time_elapsed = (end-start)* 10**3#calculates elapsed time 
                    
                    #prints time, # of moves, # of disks, and the moves
                    RecurOutputs.write(f'Number of disks:{num_disk}\n')
                    RecurOutputs.write(f'Number of moves:{total_moves}\n')
                    RecurOutputs.write(f'Time elapsed :{time_elapsed}\n')      
                    RecurOutputs.writelines(output)
                    RecurOutputs.write(f'-'*50 + '\n')
                
extractinputfiles('RecurInputs.txt','RecurOutputs.txt')#calls function to execute on input file

    