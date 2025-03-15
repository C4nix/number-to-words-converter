print("✨ Welcome to the **Number to Words Converter**! ✨\n")
####################################### Dictionaries ############################
Thousands_dict = {0: "", 1: "One Thousand", 2: "Two Thousand", 3: "Three Thousand",
                      4: "Four Thousand", 5: "Five Thousand", 6: "Six Thousand",
                      7: "Seven Thousand", 8: "Eight Thousand", 9: "Nine Thousand"}

Hundreds_dict = {0: "", 1: "One Hundred", 2: "Two Hundred", 3: "Three Hundred",
                     4: "Four Hundred", 5: "Five Hundred", 6: "Six Hundred",
                     7: "Seven Hundred", 8: "Eight Hundred", 9: "Nine Hundred"}

Tens_dict = {0: "", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
                 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

Teens_dict = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen",
                     5: "Fifteen", 6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}

Ones_dict_default = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                     6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
########## evaluate Ones,Tens,Hundreds,Thousands digits #################
def evaluate_and_convert():
    number = int(input("🔢 Enter a number (1-9999): ").strip())
    Ones = number % 10
    Tens = int(((number % 100) - Ones) / 10)
    Hundreds = ((number % 1000) - (Tens * 10)) // 100
    Thousands = ((number - (Hundreds * 100) - (Tens * 10) - Ones) // 1000)

    ######################Convert numbers to words #####################
    Ones_dict = Teens_dict if Tens == 1 else Ones_dict_default
    Thousands_word = Thousands_dict.get(Thousands)
    Hundreds_word = Hundreds_dict.get(Hundreds)
    Tens_word = Tens_dict.get(Tens)
    Ones_word = Ones_dict.get(Ones)

    return number, Ones_word, Tens_word, Hundreds_word, Thousands_word

############################ Main Program #############################
while True:
    number, Ones_word, Tens_word, Hundreds_word, Thousands_word = evaluate_and_convert()
    try:
        if number > 9999 or number < 1:
            print("⚠️ This program only supports numbers from **1 to 9999**. Please try again.")
            break
        else:
            final_output = f"\n🎯 {number} → {' '.join(filter(None, [Thousands_word, Hundreds_word, Tens_word, Ones_word]))}"
            print(final_output.strip())

            continue_check = input("\n🔄 Would you like to convert another number? (Y/N): ").lower()
            if continue_check == "n":
                print("\n👋 Thank you for using the **Number to Words Converter**! Have a great day! 😊")
                break
            elif continue_check == "y":
                continue
            else:
                print("⚠️ Invalid input! Please enter **Y** to continue or **N** to exit.")
                continue
    except ValueError:
        print("⚠️ Invalid input! Please enter a **valid number**.")
