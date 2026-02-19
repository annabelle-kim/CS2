import csv
def open_shakespeare(filename, csv_filename):
    excluded_words = ["and", "or", "the", "i", "but", "so", "because","then","for","they","them","of","to","you","a","my","it","is","in","that"] #these are my excluded words for the dictionary
    word_dictionary={}
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split()
                for i in row:
                    i = i.lower()
                    if i in word_dictionary:
                         word_dictionary[i] +=1
                    elif i in excluded_words:
                         continue
                    else:
                        word_dictionary[i]=1

                 
            words = []
            for key,values in word_dictionary.items():                                                                                      #both of these two for loops get rid of the words that only have a value of 1
                if values <= 5:
                    words.append(key)

            for word in words:
                word_dictionary.pop(word)

            word_dictionary= dict(sorted(word_dictionary.items(),key = lambda item: item[1], reverse=True))                                 # this sprted function sorts the words by numerical value
        
        #remove unnecessary values (anything with a value less than 3 or top 10/20 )
        #sort dictionary by value

        print(word_dictionary)

        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Value'])
            for key, value in word_dictionary.items():
                writer.writerow([key, value])

    except FileNotFoundError:
            print(f"Error: 'Hamlet.txt' not found")


if __name__ == "__main__":
    print("""
Hamlet
          """)
    open_shakespeare('Hamlet.txt', 'Hamlet.csv')
    print("""
          
Romeo and Juliet
          """)
    open_shakespeare('Romeo and Juliet.txt', 'Romeo and Juliet.csv')
