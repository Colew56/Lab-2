import time #import time module

def towers_iterative(n,S,A,D):#define iterative function 
    
    total_moves = (2**n) - 1#calculate total # of moves needed 
    result = []#initialize empty result string 
    disk_sequence = []#initialize empty string to keep track of disk number 
    
    if n % 2 ==0:#if n is an even number a differant sequence of moves is required 
        sequence = [(S,A), (S,D), (A,D)]#sequence moves n-1 disks to the destination pole first, and the nth disk to the auxilary pole 
    else:#if n is odd
        sequence = [(S,D), (S,A), (D,A)]#sequence moves n-1 disks to the auxilary pole first and the nth disk to the destination pole first 
        
    for i in range(1, n+1):#iterates through 1 until the last disk
        
        disk_sequence.append(i)#appends disk number to empty list 
        
    for i in range(1, total_moves + 1):#iterates through 1 unitl the last move 
        
        from_, to_ = sequence[(i-1) % 3]#uses modulo operator to calculate appropriate move,
                                        #indexs corresponing tuple, assigns from_, to_ to the correct poles  
        
        disk = disk_sequence[(i - 1) % n]#uses modulo operator to calculate appropriate disk in the sequence
        
        result.append(f'{disk} {from_}->{to_}\n')#stores variables into a result string
                                                 #appends to result list      
    return result #returns result
    
   
        
    
def extractinputfiles(filename,outputfile):
   
   #opens and reads input file
    with open(filename, 'r') as file:
        lines = file.readlines() #makes lines equal to the lines in input file  
        with open(outputfile, 'w') as IterOutputs:#opens and writes to IterOutputs.txt
            for line in lines:#iterates through input file
                line = line.strip()#strips white spaces from lines  
                if line:#ignores blank spaces
                    
                    if not line.isdigit():
                        IterOutputs.write(f"Invalid input '{line}'")#error checking, makes sure input is an integer
                        continue
                    
                    num_disk = int(line)#stores input value as integer variable 
                    total_moves = (2**num_disk)-1#calculates total moves to be echoed to output file
                    
                    start = time.perf_counter()#start time of instance 
                    output= towers_iterative(num_disk,'A','B','C')#instance of function 
                    end = time.perf_counter()#end time of instance 
                    time_elapsed = (end-start)* 10**3#calculates elapsed time
                    
                    #prints # of starting disks, # of moves, time elapsed, all moves made
                    IterOutputs.write(f'Number of disks:{num_disk}\n')
                    IterOutputs.write(f'Number of moves:{total_moves}\n')
                    IterOutputs.write(f'Time elapsed :{time_elapsed}\n')
                    IterOutputs.writelines(output)
                    IterOutputs.write(f'-'*50 + '\n')

extractinputfiles('IterInputs.txt','IterOutputs.txt')#calls function to execute on input file    
    