import openai
class EconomicImpactAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def estimate_impact(self, recall):
        # Use OpenAI to estimate economic impact
        prompt = f"""
        Estimate the economic impact of the following recall:
        - Product: {recall.get('product', 'Unknown')}
        - Reason: {recall.get('reason', 'Unknown')}
        - Scope: {recall.get('scope', 'Nationwide')}
        - Distribution: {recall.get('distribution', 'Unknown')}
        - Company : {recall.get('company', 'Unknown')}

        Provide an estimate in dollars like $M.
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0
        )
        return response.choices[0].text.strip()

#RUN SINGLE FILE AGENT

'''
impact_estimator = EconomicImpactAgent(api_key)
for recall in data:
    recall["economic_impact"] = impact_estimator.estimate_impact(recall)
print(structured_recalls)'''