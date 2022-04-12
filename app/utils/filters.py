def format_date(date):
    # recieves the datetime object and converts it to a string in the following format
    return date.strftime('%m/%d/%y')

def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word

# TESTING THESE FUNCTIONS ABOVE
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))

# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))

# from datetime import datetime
# print(format_date(datetime.now()))