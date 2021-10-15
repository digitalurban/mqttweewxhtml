# mqttweewxhtml

Jsontomqtt.py reads the json output to add in max/min/trends and then publishes additional topics to mqtt.

Requires WeewxtoJson - https://github.com/teeks99/weewx-json

Edit /etc/weewx/skins/JSON $ sudo nano weewx.json.tmpl to add new tags

       #if $trend.barometer.has_data
        "baro trend": {"value": $trend.barometer.raw, "units": "$trend.barometer.format(" ").lstrip()"},
        #end if 

        #if $trend.outTemp.has_data
        "temp trend": {"value": $trend.outTemp.raw, "units": "$trend.outTemp.format(" ").lstrip()"},
        #end if 
