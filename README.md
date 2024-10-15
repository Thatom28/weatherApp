## weather app using weather API
### create account and log on to weather app
` 
https://www.weatherapi.com/my/                                                                                                                                     
`
### env file
`
WEATHER_API_KEY=Api_key                                           
PORT=<port number>
`

## hosted teh website on render.com
### add the port  number and host adress on the main methods
`if __name__ == "__main__":
    port = int(os.environ.get("PORT", <port number>))
    app.run(host="0.0.0.0", port=port)   //allow all the ports
`
