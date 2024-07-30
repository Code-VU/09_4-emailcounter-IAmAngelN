def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    fh = open(name)
    lines = fh.readlines()

    sender = dict() #creating a dictionary to palce email addresses in

    for line in lines:
        if line.startswith("From "):
            words = line.split()
            from_name = words[1]
            if from_name not in sender: #adding email addresses to dictionary
                sender[from_name] = 1 # if none exist, add 1
            else:
                sender[from_name] += 1 #if it does exist in dict already +1

    max_count = None #setting the max count to None to be able to repalce later
    max_sender = None #setting the max sender to None to be able to repalce later

    for email, count in sender.items(): #looping through keys and values in sender dict.
        if max_count is None or count > max_count: #determing the most occuring based on it looping through each value
            max_count = count #places the higher count of emails here
            max_sender = email #places the higher count of emails email address here

    print(max_sender,max_count) #print the n
## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
