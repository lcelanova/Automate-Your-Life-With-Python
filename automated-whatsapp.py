import pywhatkit

phone_number = input("Insert your phone number here: ")
group_id = input("Insert your group id here: ")

# Send a WhatsApp Message to a Contact at 11:25
pywhatkit.sendwhatmsg(phone_number, "Test", 11, 25)

# Send a WhatsApp Message to a Contact at 11:28 and closing the tab after 2 seconds
pywhatkit.sendwhatmsg(phone_number, "Test", 11, 25, 15, True, 2)

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image(phone_number, "Images/pic.jpg")

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly(group_id, "Hello!")