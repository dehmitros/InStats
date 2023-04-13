import os
import json

lime = '\033[32m'
ORANGE = '\033[33m'




# Check if path.txt exists
if not os.path.exists('path.txt'):
    print('Error: please open main.py first')
else:
    # Read the path from path.txt
    with open('path.txt', 'r') as f:
        path = f.read().strip()

    # Use the path variable here in your code
    print(f'The path is {path}')

# Replace the following with your instagram name
searched_sender_name = 'REPLACE ME!!!'

message_counts = {}

for folder_name in os.listdir(path):
    folder_path = os.path.join(path, folder_name)
    if not os.path.isdir(folder_path):
        continue

    message_files = []
    for message_file_name in os.listdir(folder_path):
        if message_file_name in ['message_1.json', 'message_2.json']:
            message_files.append(os.path.join(folder_path, message_file_name))

    if not message_files:
        continue

    sender_name_counts = {}
    for message_file in message_files:
        with open(message_file) as f:
            data = json.load(f)
        messages = data['messages']
        for message in messages:
            sender_name = message.get('sender_name')
            if sender_name and sender_name != searched_sender_name:
                sender_name_counts[sender_name] = sender_name_counts.get(sender_name, 0) + 1

    message_count = sum(sender_name_counts.values())
    folder_name_without_random_string = folder_name[:-16] # Removes the last 16 random characters from the folder name
    message_counts[folder_name_without_random_string] = message_count

sorted_message_counts = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)
print(lime + "Done! Saving the file now")
with open('TotalReceivedMessages.txt', 'w') as f:
    for folder_name, message_count in sorted_message_counts:
        f.write(f'{folder_name}: {message_count}\n')
