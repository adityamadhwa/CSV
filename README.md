# CSV

This python script manipulates a CSV file.

Background: Raw EEG data recorded using Emotiv EPOC can be saved as CSV file, however, the labels incorporated are not parsed by the CSV file reader box in the OpenVibe software. Since I had around 80 samples of data to playback  and analyse, some of the information in these files have to be modified. The script generates a new CSV file with continous time stamps, 14 channel EEGs- Simple enough to be read by the OpenVibe.

Since it served my purposes by helping to automate CSV manipulations for most part, the script is not improved since and may not be directly usable.

