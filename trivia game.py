#nathan Broadbent
#1/2019
#trivia game
import sys
def open_file(file_name,mode):
    try:
        the_file=open(file_name,mode)
    except  IOError as e :
        print("That file couldn't be opened because")
        print(e)
        input("\n\nPress enter to quit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    try:
        line=the_file.readline()
    except IOError as e:
        print("we couldn't open the file",e)
    else:
        line=line.replace('/','\n')
        return line

def next_block(the_file):
    category=next_line(the_file)
    question=next_line(the_file)
    answers=[]
    for i in range(4):
        answer=next_line(the_file)
        answers.append(answer)
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    print('\t\tWelcome to Trivia Challenge')
    print('\t\t',title,"\n")

def main():
    the_file=open_file("test_questions.txt",'r')
    title=the_file.readline()
    welcome(title)
    score=0
    category, question, answers, correct, explanation=next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1,answers[i])
        user=input("which answer is it answer with the numbers in front numbers")
        if user==correct:
            print("congratulations you got it correct")
            score+=1
        else:
            print("you failed that question")
        print(explanation)
        category, question, answers, correct, explanation=next_block(the_file)
    the_file.close()
    print("the game is now over you got ",score,'correct')
    input("press enter to quit")
    
main()   
