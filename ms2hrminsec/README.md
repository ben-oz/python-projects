# Coding Challenge: Convert Milliseconds into Hours, Minutes, and Seconds

Purpose of the this coding challenge is to write program that converts the given milliseconds into hours, minutes, and seconds.

   ## Problem Statement

   - Write program that converts the given milliseconds into hours, minutes, and seconds. The program should convert only from milliseconds to hours/minutes/seconds, not vice versa and during the conversion following notes should be taken into consideration.

      - If the calculated time of hours is 0, it should not be shown in the output.

      - If the calculated time of minutes is 0, it should not be shown in the output.

      - If the calculated time of seconds is 0, it should not be shown in the output.

      - If the milliseconds is greater than 1000, remainder milliseconds should not be shown in the output.

      - If milliseconds given is less than 1000, only milliseconds should be shown in the output.

      - Output should always be string in the format shown in the examples.

      - Program should ask user for the input, after giving information text show as below.

     ```text
     ###  This program converts milliseconds into hours, minutes, and seconds ###
     (To exit the program, please type "exit")
     Please enter the milliseconds (should be greater than zero) :  
     ```

     - User input can be either integer or string, thus the input should be checked for the followings,

     - The input should be a decimal number greater then zero.
			   
     - If the input is less then 1, user should be warned and asked for input again.

     - If the input is string and can not be converted to decimal number, user should be warned and asked for input again.

     - Program should run until the user types `exit` in case insensitive manner.
