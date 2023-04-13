# InStats (Instagram Data Analyzer)

This Python script analyzes the Instagram data package and provides The number of messages received from a user + the number of messages sent from a user in both plain text and graph forms

    

# Installation

To use this script, you will need to have Python 3 installed on your machine. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can clone this repository by clicking the big green 'Code' button on the top right corner, then "Download ZIP"
Unzip the folder, open command prompt and navigate to the folder.
After that install the required Python packages using:

```pip install -r requirements.txt```

# Usage

To use the script, you need to download your Instagram data package from your Instagram account. Here's how:

    Go to your Instagram profile
    Click on the three horizontal lines in the top right corner
    Click on Settings
    Click on Privacy & Security
    Under "Data Download", click on "Request Download"

➡️**MAKE SURE YOU REQUEST IN JSON FORMAT, NOT HTML**   
➡️**IT WILL NOT WORK IF YOU CHOOSE HTML**

It may take some time for Instagram to prepare your data package. Once it's ready, you'll receive an email with a link to download it.

Extract the downloaded ZIP file and go to the "messages" directory, then "inbox". Keep the "inbox" location handy as the script will ask you for it later.

While you're in the "inbox" folder, click on any conversation and open the "message_1.json" file inside it (using notepad++ or something). You should see your instagram name. If it's in unicode characters, for example: ```\u00ce\u00bd\u00cf\u0084```
then you need to copy that. If there are two usernames, both in unicode, then you'll have to figure out on your own which one is yours. (You can use a unicode translator)

➡️**Take your name and replace it wherever the scripts say "REPLACE ME!!!"**<br />
More specifically, in line 22 of scripts "TotalSentMessagesCounter.py" and "TotalReceivedMessagesCounter.py"

Finally, you can run "main.py" through the terminal. All outputs will be saved in the same directory as "main.py".
That's it! Enjoy!

## Known Limitations
Right now, the script doesn't prompt the user for their name, and they have to manually add it in the script. At some point, this will be fixed.

The graph script cannot graph most, if not all, of the requests. You have to manually go into the text file, keep 25~ people and delete the rest.

## LICENSE
Distributed under the ODC Open Database License (ODbL). See [LICENSE](https://github.com/dehmitros/InStats/blob/master/LICENSE.md) for more information.

