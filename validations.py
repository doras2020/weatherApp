import json
import unittest

#Validate and parse the response
class TestsValidations(unittest.TestCase):

    def validate(self, response, description="", status=200):
        if response.status_code != status:
            print(f'FAILED validation for request status, {response.status_code} is not {status}')
        self.assertEqual(status, response.status_code, description)
        return response

    def validate_and_parse(self, response, description="", status=200):
        validated_response = self.validate(response, description, status)
        content = json.loads(validated_response.text)
        # If we want to print the response text, we can, with the next 2 lines:
        # prettified_content = json.dumps(content, indent=4, sort_keys=True)
        # print(f"Content: {prettified_content}")
        return content