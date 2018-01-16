# `whereis`- find geo-location of a mobile IP address
`whereis` - a CLI tool for determining the approximate geo-location of a 4G LTE/3G user visiting your app/site using just the IP address. This is a thin wrapper over the [Fastah GeoIP REST API](https://console.api.getfastah.com/docs/services/fastah-geoip-api-for-mobile-4g/operations/5a0b1caf699a8f0bd05a253b) and uses statistical models to provide city-level results. 

# `howfastis`- find network quality for mobile IP address
`howfastis` - a CLI tool for predicting network performance for a 4G LTE or 3G visitor using just the IP address. This again uses the [Fastah Network Prediction REST API](https://console.api.getfastah.com/docs/services/fastah-geoip-api-for-mobile-4g/operations/5a0b1caf699a8f0bd05a253b) and uses statistical models to provide network QoS ("quality of service") estimates. 

# TODO
- Make a [`twurl`](https://github.com/twitter/twurl)-like command-line interface that supports: 
* Helping a user sign-up for an API key and configuring the tool to use it
* Sensible command-line arguments that showcase key data in the API response
* Pipeing and general UNIXyness of CLI's input and output
* Examples and demos
