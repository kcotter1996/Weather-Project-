#****************************************************************
#**  Program:    Weather Project                               **
#**  Programmer: Kiersten Cotter                               **
#**  Date:       03/02/2022                                    **
#****************************************************************
import urllib.request
import time
import json

#program variables

pWordFile   = "D:\\school\\PY CODE\\weather project\\passwordFile.txt"  # File holding password to weather API
status_code = 0                                                         # Result condition of the URL call
apiid       = ''                                                        # Var for website api password 
urlAddr     = ''                                                        # URL address of website      


def get_pWord( ):                                                       # Function: extract website password from file
    f = open( pWordFile )                                               # Open the file
    if f.closed:                                                        # If file did not open
        print( "Password file not accessible." )                        #   Display error
        quit( )                                                         #   End program
    else:                                                               # Otherwise,
        apiid = f.read( )                                               #   Read contents of passwordFile
        f.close( )                                                      #   Close passwordFile
    return( apiid )                                                     # Return password to calling process


def printScrnHdr( ):                                                    # Print the screen header
    print( "\n-------------------------------------" )                  # Message header for clarity. 
    print( "Get weather conditions for an area:    " )                  # Explain program usage. 
    print( "    Enter 1 to search by city,state.   " )
    print( "    Enter 2 to search by zip code.     " )
    print( "    Enter 3 to end program.            " )
                                                            

def fetch_data( zip=None, city=None, apiid=None ):                      # the method fetches the weather data and returns the result
    baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    if zip is not None:
        baseUrl += "?zip=" + str( zip )                                 # Append search key for Zip
    else:
        baseUrl += "?q="+str( city )                                    # Append search key for City
                                                            
    baseUrl += ",us&appid="+str( apiid )                                # finally append the api id
    
    urlAddr  = urllib.request.urlopen( baseUrl )                        # Call the API location
    text     = urlAddr.read( )                                          # Copy data from the API
    weather  = json.loads( text )                                       # Create a data dictionary

    return weather                                                      # Return the weather results


def convertTemp( tempIn ):
    tempOut = (( tempIn-273 ) * 1.8 ) + 32                              # Convert °K to °F

    return tempOut
   

def showResult( resp ):
    if( resp ):                                                         # this means request was successful
        minTemp = convertTemp( resp['main']['temp_min'] )
        maxTemp = convertTemp( resp['main']['temp_max'] )

        my_formatter = "{0:.0f}"                                        # Format temps to whole numbers
        minFTemp     = my_formatter.format( minTemp )
        maxFTemp     = my_formatter.format( maxTemp )

        print(f"""{resp['name']} Weather Forecast:
        There will be {resp['weather'][0]['description']} with wind speed of {resp['wind']['speed']}.
        Visibility will be {resp['visibility']}.
        Min. temp will be {minFTemp} and max temp will be {maxFTemp}
        """)
    else:
        print("Request Failed.  Error Code: ", status_code )

        
print("* * **********************  Welcome  ********************** * *")

                                                             
def main( ):                                                            # main method
    apiid = get_pWord( )                                                # Get website password from function

    loop = True                                                         # Loop control variable
    while loop:
        inp =int( input( "\nYour options :\n1. By Zip Code    (Ex: 99999)\n2. By City,State  (Ex: Chicago,IL)\n3. Exit\n   Your Choice    : " ))
        
        if inp == 1:
            try:
                queryData = int( input( "   Enter zip code : " ))       # Request user input
                resp      = fetch_data( queryData, None, apiid )        # Request data from website
                showResult( resp )                                      # Display returned data highlights

            except Exception as ex:                                     # If try fails
                print( "Error : ", ex )                                 # Display errmsg

        elif inp == 2:
            try:
                queryData = input( "   Enter city name: " )             # Request user input
                resp      = fetch_data( None, queryData, apiid )        # Request data from website
                showResult( resp )                                      # Display returned data highlights

            except Exception as ex:                                     # If try fails
                    print("Error : ", ex )                              # Display errmsg

        else:                                                           # User selected 3-Exit from menu
                print( "\nExiting program." )                           # Inform user of program exit
                loop = False                                            # This collapses the loop 

    
if __name__ == "__main__":                                              # Call the main method
    main( )



'''  *****************  END OF PROGRAM CODE  ********************  '''    
