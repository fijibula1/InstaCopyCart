import openfoodfacts from openfoodfacts

def data
    search_result = openfoodfacts.products.search('item')

    search_result['products'][0]

    item = fetch_nutrition_score()