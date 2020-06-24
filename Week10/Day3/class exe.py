import requests


def get_news(category=None, language=None, country=None):
    url = 'http://newsapi.org/v2/top-headlines?'
    api_key = '35f754e21cb449b79e2be6dac7e5fb82'
    response = requests.get(url,
                            params={"apiKey": api_key, "category": category, "language": language, "country": country})
    # url = ('http://newsapi.org/v2/top-headlines?'
    #        'country=us&'
    #        'apiKey=35f754e21cb449b79e2be6dac7e5fb82')

    for headline in response.json()["articles"]:
        print(headline)
        print("\n")

    f = open('news.html', 'w')

    message = f"""<!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title></title>
              <style>
                  Article{{
                    border: 1px solid red;
                    width:500px;
                    margin:5px;
                  }}
                  .head{{
                    color: blue;
                  }}
              </style>
          </head>
          <body>
    """
    for headline in response.json()["articles"]:
        message += (f"""
                <Article>
                  <h1 class = "head">{headline["title"]}</h1>
                  <h3 ><span>Written by: </span><span class = "author" >{headline["author"]}</span></h3>
                  <div class ="news body">
                  {headline["content"]}      </div>
                    <div class = "source">
                      <br />
                      <a href={headline['url']}>{headline["url"]}</a>
                    </div>
                  </Article>""")
    message += """</body>
            </html>
    """
    f.write(message)
    f.close()


get_news("general", "en", "us")
