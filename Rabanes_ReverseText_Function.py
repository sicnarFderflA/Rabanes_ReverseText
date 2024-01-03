def reverse():
    while True:
        text = input("Enter a string: ")
        
        if text.replace(' ', '').isalpha(): #checks if the variable text is a string. replaces space as empty string.
            rtext = '' #eversed Text.
            for char in text:
                rtext = char + rtext
            print("Output:", rtext)
            break
        else:
            print("Error Reported! Enter text only.")

reverse()
