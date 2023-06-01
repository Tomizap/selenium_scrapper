import time
from pprint import pprint
# import array

# import numpy

from .models import find_model
from .sequence import play_sequence


# def get_data_model(driver=None, model={}, item={}):
#     if driver is None:
#         return {}
#     for prop in model:
#         value = model[prop]
#         if type(value) == str:
#             item[prop] = value
#         elif type(value) == dict:
#             try:
#                 item[prop] = driver.find_element(
#                     value['selector']).get_property(value['property'])
#             except:
#                 try:
#                     item[prop] = driver.find_element(
#                         value['selector']).get_property('innerText')
#                 except:
#                     pass
#     item['link'] = driver.current_url()
#     return item

def get_data(driver=None, url=None):
    if driver is None:
        return {}
    if url is not None:
        driver.get(url)
    print('get_data')
    return play_sequence(driver=driver)

# def play_sequence(driver=None, item={}, sequence=[]):
#     if driver is None:
#         return
#     print('play_sequence')
#     data = {}

#     for step in sequence:
#         value = sequence[step]

#         try:

#             if 'loop' in step:

#                 # data = []
#                 for _ in value['count']:
#                     item = get_data_model(model=value['model'])
#                     data.append(item.copy())

#             elif 'click' in step:

#                 if type(value) == str:
#                     driver.click(value)

#             elif "get" in step:

#                 if ':all' in step:
#                     data = []

#                     if type(value) == str:

#                         items = driver.find_elements(value)
#                         for item in items:
#                             v = item.get_property('innerText')
#                             data.append(v.copy())
#                         # return data

#                     if type(value) == dict:

#                         items = driver.find_elements(value['selector'])
#                         for item in items:
#                             try:
#                                 data = driver.find_element(
#                                     value['selector']).get_property(value['property'])
#                             except:
#                                 try:
#                                     data = driver.find_element(
#                                         value['selector']).get_property('innerText')
#                                 except:
#                                     pass
#                             data.append(v.copy())
#                         # return data

#                 else:

#                     if type(value) == str:
#                         return driver.find_element(value).get_property('innerText')

#                     elif type(value) == dict:
#                         try:
#                             data = driver.find_element(
#                                 value['selector']).get_property(value['property'])
#                         except:
#                             try:
#                                 data = driver.find_element(
#                                     value['selector']).get_property('innerText')
#                             except:
#                                 pass

#                     elif type(value) == list:
#                         model = value
#                         for prop in model:
#                             v = model[prop]
#                             if type(v) == str:
#                                 data[prop] = v
#                             elif type(v) == dict:
#                                 try:
#                                     data[prop] = driver.find_element(
#                                         v['selector']).get_property(v['property'])
#                                 except:
#                                     try:
#                                         data[prop] = driver.find_element(
#                                             v['selector']).get_property('innerText')
#                                     except:
#                                         pass
#                         data['link'] = driver.current_url()

#                     else:
#                         print("type: " + str(type(value)))

#             elif "execute_script" in step:

#                 if type(value) == str:
#                     try:
#                         driver.execute_script(value)
#                     except:
#                         pass

#             elif "wait" in step:

#                 if type(value) == str:
#                     time.sleep(int(value))

#                 elif type(value) == int:
#                     time.sleep(value)

#         except:
#             print('step error')

#     return data


# def get_urls(driver=None, default=[], sequence=[]):
#     if driver is None:
#         return default
#     print('get urls')
#     urls = default
#     urls = play_sequence(driver, sequence)
#     # for _ in range(setting['pagination']['count']):
#     #     time.sleep(2)
#     #     for script in setting['scripts']:
#     #         try:
#     #             driver.execute_script(script)
#     #         except:
#     #             pass
#     #     for selector in setting['items']['selector']:
#     #         try:
#     #             items = driver.find_elements(selector)
#     #             # print(selector)
#     #             # print(len(items))
#     #             for item in items:
#     #                 urls.append(item.get_property('href'))
#     #         except:
#     #             pass
#     #     for selector in setting['pagination']['selector']:
#     #         try:
#     #             driver.click(setting['pagination']['selector'])
#     #         except:
#     #             pass
#     # print(str(len(urls)) + ' urls found')
#     return urls


# def get_data(driver=None, default={}) -> dict:
#     print('get data')
#     data = default
#     if driver is not None:
#         url = driver.current_url()
#         fm = find_model(url=url)
#         model = fm['model']
#         w = fm['website']
#         t = fm['type']
#         l = fm['listing']
#         setting = fm['setting']
#         if l == True:
#             # pprint(fm)
#             urls = play_sequence(
#                 driver=driver, sequence=fm['ListingSequence'])
#             print(urls)
#             data = []
#             for u in urls:
#                 driver.get(u)
#                 item = get_data(driver=driver)['data']
#                 data.append(item.copy())
#         else:
#             # print(setting['item']['preclick'])
#             time.sleep(1)
#             for pc in setting['item']['preclick']:
#                 try:
#                     driver.click(pc)
#                 except:
#                     pass
#             time.sleep(1)
#             for prop in model:
#                 value = model[prop]
#                 if type(value) == str:
#                     data[prop] = value
#                 elif type(value) == dict:
#                     try:
#                         data[prop] = driver.find_element(
#                             value['selector']).get_property(value['property'])
#                     except:
#                         try:
#                             data[prop] = driver.find_element(
#                                 value['selector']).get_property('innerText')
#                         except:
#                             pass
#             data['link'] = driver.current_url()
#         return {
#             "website": w,
#             "type": t,
#             "listing": l,
#             "data": data
#         }
#     print('no driver')


# def selenium_scrapper(driver=None, url=None):

#     if driver is None:
#         return []
#     print('scrapping')
#     if url is not None:
#         driver.get(url)
#     gd = get_data(driver=driver)
#     return {
#         "listing": gd['listing'],
#         "data": gd['data']
#     }


# def selenium_scrapper(driver=None, url=None):

#     if driver is None:
#         return []
#     print('scrapping')
#     if url is not None:
#         driver.get(url)
#     gd = get_data(driver=driver)
#     return {
#         "listing": gd['listing'],
#         "data": gd['data']
#     }
