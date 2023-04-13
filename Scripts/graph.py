import matplotlib.pyplot as plt
lime = '\033[32m'
ORANGE = '\033[33m'
YELLOW = '\033[93m'
# Define a function to plot the graph based on the selected option
def plot_graph(option):
    # Set the filename and title based on the selected option
    if option == 1:
        filename = 'TotalMessages.txt'
        title = 'Total Messages'
    elif option == 2:
        filename = 'TotalReceivedMessages.txt'
        title = 'Total Received Messages'
    elif option == 3:
        filename = 'TotalSentMessages.txt'
        title = 'Total Sent Messages'
    else:
        print('Invalid option')
        return
    
    # Read the data from the text file
    with open(filename, 'r') as f:
        data = f.read().splitlines()

    folder_names = []
    message_counts = []
    for line in data:
        folder_name, count = line.split(': ')
        folder_names.append(folder_name)
        message_counts.append(int(count))

    # Set the figure size
    plt.figure(figsize=(len(folder_names) * 1, 6))

    # Create a bar graph
    plt.bar(folder_names, message_counts)
    plt.xticks(rotation=60)
    plt.xlabel('User')
    plt.ylabel('Message Count')
    plt.title(title)

    # Save the graph as a PNG image file
    plt.savefig(f'{title}.png', dpi=300, bbox_inches='tight')
    print(lime + "Done! Saving the graph now.")


# Create an option menu
print(lime + 'Select an option:')
print(ORANGE + '1. Total Messages Graph')
print(YELLOW + '2. Total Messages Received Graph')
print(ORANGE + '3. Total Messages Sent Graph')

option = int(input())

plot_graph(option)
