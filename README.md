# romanNum-ArabicInt
API to translate roman numerals to arabic integers, and vice versa

The base code came from one of the advanced python challenges and reworked in order to function as an API. This was then containerised using Docker.

Once the container is up and running you can do the following API calls:
> '/romanToInt/romNum' 

where romNum is a roman numeral string - for example MCMXCIX. This will return the result 1999

> '/intToRoman/integer'

where integer is an integer string - for example 1999. This will return the result MCMXCIX


