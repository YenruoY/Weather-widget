# Weather widget (to use with i3status)

It's a simple script to show current temperature, humidity and wind speed. This scipt uses OpenWeatherMap API to get data. The user have to provide their own API key and their location in the form of latitude and longitude. 


# Dependencies

The script don't have any dependencies, however it uses Font-awesome for the icons. 

# Use

The script was created to used with i3-status. To add it to your i3status bar, open your i3 config file and edit the line as below :

    bar {
    status_command i3status | ~/path/to/weather_widget.py
    (...)
    }
 
Add executable permission to the file :

    chmod +x ~/path/to/weather_widget.py 
