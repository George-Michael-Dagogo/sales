from newsapi import NewsApiClient
import pandas as pandas

newsapi = NewsApiClient(api_key='ff4373852c2343a98303951439854f8c')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
                                          category='business',
                                          language='en',
                                        )

print(top_headlines)