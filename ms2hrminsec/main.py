TEXT_START = """
...  This program converts milliseconds into hours, minutes, and seconds ...
(To exit the program, please type "exit")
"""
TEXT_ASK_INPUT = "Please enter the milliseconds (should be greater than zero) :  "
TEXT_ERROR = "Not a valid input! Please enter a integer of 1 or greater\n"
TEXT_EXIT = "\nExiting the program\n...Good Bye...\n" 


###############################################################

print(TEXT_START)

while True:

    user_input = input(TEXT_ASK_INPUT)
    if user_input.lower() == "exit":
        print(TEXT_EXIT)
        break

    else:
        try:
            user_input = int(user_input)
        
        except ValueError:
            print(TEXT_ERROR)

        else:
            if user_input < 1:
                print(TEXT_ERROR)

            elif 1 <= user_input < 1000:
                print(f"just {user_input} millisecond/s")
            
            else:
                seconds = user_input // 1000   # ignoring remaining milliseconds
                
                # result = ""
                # remaining_seconds = seconds % 60
                # if remaining_seconds > 0: 
                #     result = f"{remaining_seconds} second/s"

                # minutes = seconds // 60
                # remaining_minutes = minutes % 60
                # if remaining_minutes > 0: 
                #     result = f"{remaining_minutes} minute/s " + result
                
                # hours = minutes // 60
                # if hours > 0: 
                #     result = f"{hours} hour/s " + result
                ### ANOTHER ALGORITM ###
                
                h = (seconds // 3600, "hour/s")
                tm = seconds % 3600
                m = (tm // 60, "minute/s")
                s = (tm % 60, "second/s")

                result = ""
                for item in (h, m, s):
                    #result.append(item[])
                    result += f"{item[0]} {item[1]} " if item[0] > 0 else ""

                print(result)
