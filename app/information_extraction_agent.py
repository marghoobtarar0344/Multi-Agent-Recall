import openai


class InformationExtractionAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def extract_details(self, recall):
        # Use OpenAI to extract structured information
        prompt = f"""
        Extract the following details from the recall announcement:
        - Product: The affected product name.
        - Reason: The reason for the recall.
        - Scope: The geographic scope of the recall (e.g., nationwide, regional).
        - Distribution: The distribution channels (e.g., retail, wholesale).
        - Company : The compnay name of the product
        Recall Announcement:
        {recall}
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0
        )
        result = response.choices[0].text.strip()
        return self._parse_openai_response(result)

    def _parse_openai_response(self, text):
        # Parse OpenAI's response into a structured format
        details = {}
        for line in text.split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                details[key.strip().lower()] = value.strip()
        return details


# RUN SIGNLE FILE AGENT
'''
api_key = "your_openai_api_key"
extractor = InformationExtractionAgent(api_key)
structured_recalls = [extractor.extract_details(recall) for recall in recalls]
print(structured_recalls)
'''
