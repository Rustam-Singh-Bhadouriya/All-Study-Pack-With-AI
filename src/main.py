# To run this code you need to install the following dependencies:
# pip install google-genai
import modules
from modules import *

print("""If You want to choose Articles type 'A' And Whant AI response then type 'G'... """)
# choose = input("Enter which you choose: ")
# print("\n")

# # First There is Gen AI Gemini Model 
# if choose == 'G':   
    # print("There Will you find all descirbe of your all topics!")
    # while True:
    #     promt = input("Enter your promt: ")
    #     if promt.lower() == 'exit':
    #         str = "clear"
    #         for i in range(len(str)):
    #             pg.keyDown(str[i])
    #         pg.keyDown("enter")
    #         break
    #     gen.generate(promt=promt)


# elif choose == 'A':
#     print("You need to type article name we will fetch!")
#     article_name = input("Input Which Article you want: ")
#     article.getarticle(article_name=article_name)


# else:
#     print("choose A/G.....")


match input("Chosse A/G"):
    # Calling WIkipedia for article
    case 'A':
        print("You need to type article name we will fetch!")
        article_name = input("Input Which Article you want: ")
        article.getarticle(article_name=article_name)
    # calling Gen AI Model
    case 'G':
         print("There Will you find all descirbe of your all topics!")
        while True:
            promt = input("Enter your promt: ")
            if promt.lower() == 'exit':
                str = "clear"
                for i in range(len(str)):
                    pg.keyDown(str[i])
                pg.keyDown("enter")
                break
            gen.generate(promt=promt)
    case _ :
            print("Choose A/G)


        
