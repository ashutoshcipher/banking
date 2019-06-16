1. Given a bank branch IFSC code, get branch details
URL: https://radiant-earth-44521.herokuapp.com/banks/ifsc/<str:ifsc>/
TYPE: GET
Sample Request URL: https://radiant-earth-44521.herokuapp.com/banks/ifsc/UTIB0000004/

2. Given a bank name and city, gets details of all branches of the bank in the city
URL: https://radiant-earth-44521.herokuapp.com/bankdetails/nameandcity/
TYPE: POST
Sample Request Body: {"name" : "ZILA SAHAKRI BANK LIMITED GHAZIABAD", "city" : "LONI"}

