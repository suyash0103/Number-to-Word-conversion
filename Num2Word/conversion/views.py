from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# Functioning of /identity endpoint
class Identity(APIView):

    # Request type GET
    def get(self, request):
        responseContent = {
            'server_name': 'Suyash Ghuge'
        }
        return Response(responseContent, status=status.HTTP_200_OK)

    # Request type POST
    def post(self, request):
        responseContent = {"Only GET request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type PUT
    def put(self, request):
        responseContent = {"Only GET request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type PATCH
    def patch(self, request):
        responseContent = {"Only GET request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type DELETE
    def delete(self, request):
        responseContent = {"Only GET request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type OPTIONS
    def options(self, request):
        responseContent = {"Only GET request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Functioning of /convert endpoint
class Convert(APIView):

    # List to maintain words of numbers from 1 to 19
    ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
 
    # List to maintain words of numbers 20-90, all numbers at a gap of 10
    twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    
    # List to maintain large values like million, billion and so on
    thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ", "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "]


    def convertGroupOfThree(self, number):

        units_place = number % 10
        tens_place = ((number % 100) - units_place) / 10
        hundreds_place = ((number % 1000) - (tens_place * 10) - units_place) / 100
    
        # Convert into integer, since the variables can be float due to above operations
        units_place = int(units_place)
        tens_place = int(tens_place)
        hundreds_place = int(hundreds_place)
    
        words = ""

        # We should include the word 'hundred' only when digit at hundreds place is not 0
        if hundreds_place != 0:
            # If tens place is greater than 1, it means the 2 digit number starting from tens place is more than 19, hence use both twenties and ones list
            if tens_place > 1:
                words = self.ones[hundreds_place] + "hundred " + self.twenties[tens_place] + self.ones[units_place]
            # If tens place is less than or equal to 1, it means the 2 digit number starting from tens place is between 0 and 19 inclusive
            else:
                words = self.ones[hundreds_place] + "hundred " + self.ones[number % 100]
        else:
            if tens_place > 1:
                words = self.twenties[tens_place] + self.ones[units_place]
            else:
                words = self.ones[number % 100]

        return words


    def convertNumber(self, number):
        # Divider is a variable to take the last 3 digits of the number and convert them into words
        divider = 3

        numberToWords = ""
        
        # Iterates over the thousands list, incremented each time a group of 3 digits are converted into words. Group of 3 digits is chosen as per American Standard Number System.
        index = 0
        
        while divider == 3:
            # Take the last 3 digits for converting them into words
            lastThreeChar = number[-divider:]

            # Store the remaining digits in remainingChar variable
            remainingChar = number[:-divider]
            
            if int(lastThreeChar) != 0:
                numberToWords = self.convertGroupOfThree(int(lastThreeChar)) + self.thousands[index] + numberToWords
            index += 1
            
            # This is to make sure the index variable does not become more than size of thousands list
            if index == len(self.thousands):
                index = 1

            # There are no remaining characters, hence we can break the loop
            if remainingChar == '':
                divider += 1
            
            # The new number becomes the remaining characters, since the last 3 have already been converted to words in above step
            number = remainingChar
        
        # Remove the last space
        numberToWords = numberToWords[:-1]
        return numberToWords


    def post(self, request):
        # Check for request body being NULL and check if number in request body is a valid number
        try:
            numberInString = str(request.data['value'])
        except:
            responseContent = {"No valid number obtained to convert into words"}
            return Response(responseContent, status=status.HTTP_400_BAD_REQUEST)

        # Check if the value passed is not an Integer
        if type(request.data['value']) != int:
            responseContent = {"Integer should be passed in request body"}
            return Response(responseContent, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if the value in request body is empty or not
        if len(numberInString) == 0:
            responseContent = {"Value field is empty"}
            return Response(responseContent, status=status.HTTP_400_BAD_REQUEST)

        # Check if the value can be converted into integer, only then can it be converted into words
        try:
            numberInInt = int(numberInString)
        except:
            responseContent = {"Invalid Number"}
            return Response(responseContent, status=status.HTTP_400_BAD_REQUEST)
        
        # Negative values are not allowed to be converted into words
        if numberInInt < 0:
            responseContent = {"Value field should be greater than 0"}
            return Response(responseContent, status=status.HTTP_400_BAD_REQUEST)

        # Return the word 'zero' if the value in request body equals 0
        elif numberInInt == 0:
            responseContent = {"value" : numberInInt, "value_in_words" : "zero"}
            return Response(responseContent, status=status.HTTP_200_OK)

        # Call above two helper functions to convert number into words
        else:            
            numberToWords = self.convertNumber(numberInString)

            responseContent = {"value" : numberInInt, "value_in_words" : numberToWords}
            return Response(responseContent, status=status.HTTP_200_OK)

    # Request type GET
    def get(self, request):
        responseContent = {"Only POST request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type PUT
    def put(self, request):
        responseContent = {"Only POST request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type PATCH
    def patch(self, request):
        responseContent = {"Only POST request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type DELETE
    def delete(self, request):
        responseContent = {"Only POST request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Request type OPTIONS
    def options(self, request):
        responseContent = {"Only POST request allowed on this endpoint"}
        return Response(responseContent, status=status.HTTP_405_METHOD_NOT_ALLOWED)