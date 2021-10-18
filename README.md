# mqttweewxhtml

Jsontomqtt.py reads the json output to add in max/min/trends and then publishes additional topics to mqtt.

Requires WeewxtoJson - https://github.com/teeks99/weewx-json

Edit /etc/weewx/skins/JSON $ sudo nano weewx.json.tmpl to add new tags (trend data is part of the default output)

       #if $trend.barometer.has_data
        "baro trend": {"value": $trend.barometer.raw, "units": "$trend.barometer.format(" ").lstrip()"},
        #end if 

        #if $trend.outTemp.has_data
        "temp trend": {"value": $trend.outTemp.raw, "units": "$trend.outTemp.format(" ").lstrip()"},
        #end if 

html includes standard and eink versions - these are general templates and need to be edited to your own mqtt feeds. If you just want the mqtt feeds then ignore the html pages.

![eink](https://github.com/digitalurban/mqttweewxhtml/blob/main/Screenshot%202021-10-15%20at%2011.19.49.png)

![standard](https://github.com/digitalurban/mqttweewxhtml/blob/main/Screenshot%202021-10-15%20at%2011.18.53.png)
