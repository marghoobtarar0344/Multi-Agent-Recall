import openai
class SeverityRankingAgent:
    def __init__(self, api_key):
        openai.api_key = api_key

    def rank_recalls(self, recalls):
        for recall in recalls:
            recall["manual_severity_score"] = self.manual_calculate_severity(recall)
            recall["severity_score"] = self._calculate_severity(recall)
        return sorted(recalls, key=lambda x: x["severity_score"], reverse=True)
    # Calculate Manual severity Ranking checker
    def manual_calculate_severity(recall):
        """
        Calculate severity ranking for a recall based on risk, scope, and distribution.
        """

        # Define scoring criteria
        health_risk_scores = {
            "Labeling Issue": 1,
            "Undeclared Allergen": 2,
            "Foreign Matter Contamination": 2,
            "Bacterial Contamination": 3,
            "Toxins / Serious Contaminants": 3
        }

        scope_scores = {
            "Local": 1,
            "Regional": 2,
            "Nationwide": 3
        }

        distribution_scores = {
            "Limited": 1,
            "Retail": 2,
            "Retail + Online": 3
        }

        # Assign scores based on recall data
        health_risk = health_risk_scores.get(recall["Reason"], 1)  # Default to 1 if unknown
        scope = scope_scores.get(recall["Scope"], 1)  # Default to 1 if unknown
        distribution = distribution_scores.get(recall["Distribution"], 1)  # Default to 1 if unknown

        # Calculate total severity
        severity_score = health_risk + scope + distribution

        # Assign ranking based on severity score
        if severity_score >= 8:
            ranking = "Critical"
        elif severity_score >= 5:
            ranking = "High"
        elif severity_score >= 3:
            ranking = "Medium"
        else:
            ranking = "Low"

        return ranking


    def _calculate_severity(self, recall):
        # Use OpenAI to calculate a severity score
        prompt = f"""
        Calculate a severity score (1-10) for the following recall:
        - Product: {recall.get('product', 'Unknown')}
        - Reason: {recall.get('reason', 'Unknown')}
        - Scope: {recall.get('scope', 'Nationwide')}
        - Economic Impact: {recall.get('economic_impact', 'Unknown')}

        Consider factors like health risk, economic impact, and geographic scope.
        """

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=10,
            temperature=0
        )
        return float(response.choices[0].text.strip())

# RUN SINGLE FILE AGENT
'''
ranker = SeverityRankingAgent(api_key)
ranked_recalls = ranker.rank_recalls(structured_recalls)
print(ranked_recalls)
'''