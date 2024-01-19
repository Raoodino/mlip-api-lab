from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from config import AZURE_ENDPOINT, AZURE_KEY

# endpoint = "https://jrrao.cognitiveservices.azure.com/"
# key = "0e80f21417a64dc7ae2864ecef666020"

credentials = CognitiveServicesCredentials(AZURE_KEY)

client = ComputerVisionClient(endpoint=AZURE_ENDPOINT, credentials=credentials)


def read_image(uri):
    numberOfCharsInOperationId = 36
    maxRetries = 10

    # SDK call
    rawHttpResponse = client.read(uri, language="en", raw=True)

    # Get ID from returned headers
    operationLocation = rawHttpResponse.headers["Operation-Location"]
    idLocation = len(operationLocation) - numberOfCharsInOperationId
    operationId = operationLocation[idLocation:]

    # SDK call
    result = client.get_read_result(operationId)

    # Try API
    retry = 0

    while retry < maxRetries:
        if result.status.lower() not in ["notstarted", "running"]:
            break
        time.sleep(1)
        result = client.get_read_result(operationId)

        retry += 1

    if retry == maxRetries:
        return "max retries reached"

    if result.status == OperationStatusCodes.succeeded:
        res_text = " ".join(
            [line.text for line in result.analyze_result.read_results[0].lines]
        )
        return res_text
    else:
        return "error"


def analyze_image(uri, analysis_type):
    # client = ComputerVisionClient(endpoint=endpoint, credentials=credentials)
    if analysis_type == "object_detection":
        # Call object detection API
        detected_objects = client.analyze_image(
            uri, visual_features=[VisualFeatureTypes.objects]
        )
        # Process the response
        objects = [
            {
                "object": obj.object_property,
                "confidence": obj.confidence,
                "rectangle": obj.rectangle.__dict__,
            }
            for obj in detected_objects.objects
        ]
        return {"detected_objects": objects}

    elif analysis_type == "facial_recognition":
        # Facial recognition logic here (if supported by the API)
        pass

    # ... other types of analysis

    else:
        raise ValueError("Unsupported analysis type")
