import requests
from bs4 import BeautifulSoup


class DataCollectionAgent:
    def __init__(self,fda_url,usda_url):
        self.fda_url = fda_url#"https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
        self.usda_url = usda_url#"https://www.fsis.usda.gov/recalls"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def scrape_fda_recalls(self):

        response = requests.get(self.fda_url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Locate the recall table
        table = soup.find("table", {"id": "datatable"})

        # Extract rows
        recalls = []

        for row in table.find_all("tr")[1:]:  # Skip header row
            columns = row.find_all("td")
            if len(columns):  # Ensure valid row
                recall_data = {
                    "Date": columns[0].text.strip(),
                    "Brand Name": columns[1].text.strip(),
                    "Product Description": columns[2].text.strip(),
                    "Product Type": columns[3].text.strip(),
                    "Recall Reason": columns[4].text.strip(),
                    "Company Name": columns[5].text.strip(),
                    "Recall Status": columns[6].text.strip() if len(columns) > 6 else "Unknown",
                }
                recalls.append(recall_data)

        # Show extracted recalls (limit to first 5 for display)
        return recalls

    def scrape_usda_recalls(self):
        response = requests.get(self.usda_url , headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        # Load the USDA HTML file

        usda_recalls = []

        for recall in soup.find_all("div", class_="view__row"):
            recall_data = {}

            # Extract Recall ID (PHA/Recall Number)
            recall_id_tag = recall.find("span", class_="tag tag--active")
            recall_data["Recall ID"] = recall_id_tag.text.strip(
            ) if recall_id_tag else "N/A"

            # Extract Type of Alert (Public Health Alert, Recall, etc.)
            alert_type_tag = recall.find(
                "a", class_="tag tag--public health alert")
            recall_data["Alert Type"] = alert_type_tag.text.strip(
            ) if alert_type_tag else "N/A"

            # Extract Recall Reason
            reason_tag = recall.find("a", class_="tag tag--reason")
            recall_data["Reason"] = reason_tag.text.strip(
            ) if reason_tag else "N/A"

            # Extract Title & Link
            title_tag = recall.find("h3", class_="recall-teaser__title")
            recall_data["Title"] = title_tag.a.text.strip(
            ) if title_tag and title_tag.a else "N/A"
            recall_data["Link"] = title_tag.a["href"] if title_tag and title_tag.a else "N/A"

            # Extract Establishment (Company Name)
            company_tag = recall.find(
                "span", class_="recall-teaser__establishment")
            recall_data["Establishment"] = company_tag.text.strip(
            ) if company_tag else "N/A"

            # Extract Status (Active, Terminated, etc.), handling missing elements
            status_div = recall.find("div", class_="recall-teaser__status")
            status_tag = status_div.find(
                "span", class_="tag tag--active") if status_div else None
            recall_data["Status"] = status_tag.text.strip(
            ) if status_tag else "N/A"

            # Extract Recall Date
            date_tag = recall.find("div", class_="recall-teaser__date")
            recall_data["Date"] = date_tag.text.strip() if date_tag else "N/A"

            # Extract Affected States
            states_tag = recall.find("div", class_="recall-teaser__states")
            recall_data["Affected States"] = states_tag.text.strip(
            ) if states_tag else "N/A"

            # Extract Summary
            summary_tag = recall.find("div", class_="recall-teaser__summary")
            recall_data["Summary"] = summary_tag.text.strip(
            ) if summary_tag else "N/A"

            # Extract Impacted Products
            products_tag = recall.find("div", class_="recall-teaser__products")
            recall_data["Impacted Products"] = products_tag.text.strip(
            ) if products_tag else "N/A"

            # Append to recall list
            usda_recalls.append(recall_data)
            # print('it pushed the data',usda_recalls)

        # Show extracted recalls (limit to first 3 for display)
        return usda_recalls

    def collect_recalls(self):
        fda_recalls = self.scrape_fda_recalls()
        usda_recalls = self.scrape_usda_recalls()
        return fda_recalls.append(usda_recalls)


# run single file agent
'''
data_collector = DataCollectionAgent()
recalls = data_collector.collect_recalls()
print(recalls)
'''
