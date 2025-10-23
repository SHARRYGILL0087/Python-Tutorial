
def game(scr) :
    print("Playing the game")
    check_hi_score(scr)
    return scr

def update_file(final_str , my_scr) :
    with open("Hi-score.txt" , "w") as file : 
        file.write(final_str)
    print(f"High Score set {my_scr}")

    
def check_hi_score(my_scr) :
    with open ("Hi-score.txt") as f : 
        scr_str =  f.read()
        if not scr_str : 
            final_str = f"High score is: {my_scr}"
            update_file(final_str , my_scr)
        else : 
            scr_str_list = scr_str.split()

            hi_scr = int(scr_str_list[-1])
            if(my_scr > hi_scr) :
                scr_str_list[-1] = my_scr
                final_str = " ".join(map(str, scr_str_list))        
                update_file(final_str , my_scr)    
            else : 
                print("Try Again")
    

n = int(input("Enter your score - "))
my_scr =  game(n)







