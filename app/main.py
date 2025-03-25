
from data_collection_agent import DataCollectionAgent
from information_extraction_agent import InformationExtractionAgent
from economic_impact_estimation_agent import EconomicImpactAgent
from severity_rank_agent import SeverityRankingAgent
from report_generation_agent import ReportGenerationAgent
from config import (
    API_KEY
)
# Step 1: Collect data
fda_url = "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
usda_url = "https://www.fsis.usda.gov/recalls"
data_collector = DataCollectionAgent(fda_url,usda_url)
recalls = data_collector.collect_recalls()

# Step 2: Extract information
extractor = InformationExtractionAgent(API_KEY)
structured_recalls = [extractor.extract_details(recall) for recall in recalls]

# Step 3: Estimate economic impact
impact_estimator = EconomicImpactAgent(API_KEY)
i = 0
for recall in structured_recalls:
    recall["economic_impact"] = impact_estimator.estimate_impact(recall)

# Step 4: Rank recalls by severity
ranker = SeverityRankingAgent(API_KEY)
ranked_recalls = ranker.rank_recalls(structured_recalls)

# Step 5: Generate report
report_generator = ReportGenerationAgent(API_KEY)
report = report_generator.generate_report(ranked_recalls)
print(report)