
from SimplerLLM.tools.rapid_api import RapidAPIClient

def get_seo_page_report(url :str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {
        'url': url,
    }
    api_client = RapidAPIClient()
    api_key = api_client.api_key
    print(api_key)
    print(api_params)
    api_headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "website-seo-analyzer.p.rapidapi.com"
    }
    response = api_client.call_api(api_url, method='GET',headers_extra=api_headers, params=api_params)
    return response