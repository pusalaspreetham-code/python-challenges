Emergency Resource Dispatch Analyzer

During a disaster drill, emergency response teams report the number of resources requested by different zones. However, these reports may contain:
-Invalid values (such as negative numbers)
-Unrealistic or excessive requests
-Duplicate demands
-Situations indicating critical shortages

 This code analises into four categories and gives the output on personlisation logic

 Personlisation logic used:

 To caluclate PLI=(length of name without spaces) % 3

 If PLI is equal to zero then it will remove all low demand requests
 If PLI is equal to one then it will remove all high demand requests
 IF PLI is equal to two then it keep only moderate demand requests

 How to run file

 Download the file and open it in command prompt and run this command 
 python day5_Emergency_Resource_Dispatch_Analyzer.py
 Then it will show the output of code
