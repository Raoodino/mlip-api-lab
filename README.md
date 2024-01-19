# Lab 1: Calling third-party Machine Learning APIs

Experience connecting to Azure Vision API and rewrite the hard-coding credentials,
put the hard-coding credentials in local file 'config.py' and add to .gitignore.

## Getting started

Clone the starter code from this Git repository

The code implements a flask web application that receives API requests to analyze an image and return information about the image, including the text contained within. To identify the text, the OCR feature of the Azure Vision API [[documentation](https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f20d#:~:text=test.jpg%22%7D-,Response%20200,-The%20OCR%20results), [response format](https://westcentralus.dev.cognitive.microsoft.com/docs/services/computer-vision-v3-2/operations/56f91f2e778daf14a499f20d#:~:text=test.jpg%22%7D-,Response%20200,-The%20OCR%20results)] can be used by adjusting the API endpoint and credentials in the code. We use the Azure’s provided libraries to abstract from low-level protocol details.

Install the dependencies in the `requirements.txt` file with pip or similar. Replace Endpoint and Key with your own in [analyze.py](https://github.com/eshetty/mlip-api-lab/blob/main/analyze.py). To set up the flask server, just run `python3 app.py`. The system should try to analyze an example image and report the results when you go to http://localhost:3000/

## Connecting to the Azure Vision API

1. Sign up for the a student account for Microsoft Azure: https://azure.microsoft.com/en-us/free/students/ – no credit card required

2. Create an instance of the Computer Vision service and get an API endpoint of your instance of the service.

3. Get a subscription key to authorize your script to call the Computer Vision API.

4. Update the code with the endpoint and key and test it.

## Secure your Credentials

The starter code hardcodes credentials in the code. This is a bad practice.
Rewrite the code to load credentials from a file or an environment variable and commit the code without the credentials to GitHub.

## Calling your own API

The starter code comes with a flask server that serves the website at http://localhost:3000/ but also exposes an own API at http://localhost:3000/api/v1/analysis/ accepting a GET request with a JSON object with a single field “uri” and a 'analyze_type' pointing to an image to analyze.

Identify how to call your own API with a tool like [curl](https://curl.se/docs/manpage.html) or [Postman](https://www.postman.com).

Optionally extend the API or document it with [Swagger](https://swagger.io).

## Additional resources

- [Redhat article on API](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces)
- [Azure Computer Vision](https://learn.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python)
- [API Design Best Practices](https://blog.stoplight.io/crud-api-design?_ga=2.223919515.1813989671.1674077556-1488117179.1674077556)
- [API Endpoint Best Practices](https://www.telerik.com/blogs/7-tips-building-good-web-api)
- The file seai-azure-cv-ocr-api.json has the structure to test calls to the Azure Vision API with Postman.
