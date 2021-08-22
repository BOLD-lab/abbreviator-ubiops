import abbreviator

"""
    Deployment Class for UbiOps
    https://ubiops.com/docs/deployments/deployment-package/deployment-structure/
"""

class Deployment:

    def __init__(self, base_directory, context):
        print("Initialising My Deployment")

    def request(self, data):
        print("Processing request for My Deployment")

        lang = data.get('language', 'en')

        if not lang in abbreviator.core.pyphen_dict.keys():
            lang = 'en'

        """
            How to check?
        """

        return {
            "original": data['long'],
            "short" : abbreviator.sentence_shortener(data['long'], language=lang)
        }