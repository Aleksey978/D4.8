from django import template

register = template.Library()

word_list = ['редиска', 'дурак', 'козел']


@register.filter()
def censor(value):
    censored_value = value
    for word in word_list:
        censored_value = censored_value.replace(word[1:], '*' * (len(word) - 1)) if len(word) > 1 else censored_value
    return censored_value
