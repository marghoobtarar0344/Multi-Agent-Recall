import openai
class ReportGenerationAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_report(self, ranked_recalls):
        # Use OpenAI to generate a report
        prompt = f"""
        Generate a concise weekly food recall briefing for a VP of Supply Chain.
        Include the following:
        - Top recalls ranked by severity.
        - Summary of total recalls and economic impact.
        - Recommendations for action.

        Recalls:
        {ranked_recalls}
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].text.strip()

# RUN SIGNLE FILE AGENT
'''
report_generator = ReportGenerationAgent(api_key)
report = report_generator.generate_report(ranked_recalls)
print(report)
'''