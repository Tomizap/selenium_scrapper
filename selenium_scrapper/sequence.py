import time
from pprint import pprint
import re

from selenium.webdriver.common.keys import Keys
from selenium_driver import selenium_driver

from .models import find_model


def get_element_data(driver=None, selector=None, property=None):
    if driver is None or selector is None:
        return ''
    print('-- get_element_data')
    try:
        if property is not None:
            return driver.find_element(selector).get_property(property).strip().split("\n")[0]
        else:
            return driver.find_element(selector).get_property('innerText').strip().split("\n")[0]
    except:
        pass
    print('cannot get element')
    return ''


def get_elements_data(driver=None, selector=None, property=None):
    if driver is None or selector is None:
        return
    print('-- get_elements_data')
    data = []
    # time.sleep(2)
    elements = driver.find_elements(selector)
    for el in elements:
        if property is not None:
            value = el.get_property(property)
            data.append(value)
        else:
            value = el.get_property('innerText')
            data.append(value)
    return data


def play_sequence(driver=None, url=None, item={}, data=[], sequence=None, verbose_item=None):
    if driver is None:
        print('no driver')
        return
    if url is not None:
        driver.get(url)
    original_url = driver.current_url()
    fm = find_model(original_url)
    if sequence is None:
        # if
        sequence = fm['sequence']
    # pprint(sequence)
    time.sleep(3)
    for step in sequence:
        value = sequence[step]
        property = str(step).split(':')[0]
        print('- step: ' + str(step))

        # ---------------- ACTION ---------------------

        if ':click' in step:
            # print(value)
            if type(value) == str:
                driver.click(value)
            elif type(value) == list:
                for e in value:
                    driver.click(e)

        elif ":execute_script" in step:

            if type(value) == str:
                try:
                    driver.execute_script(value)
                except:
                    pass

            elif type(value) == list:
                for script in value:
                    try:
                        driver.execute_script(script)
                    except:
                        pass

        elif ":wait" in step:
            # print(value)
            time.sleep(value)

        elif ":goto" in step:
            if ":original_url" in value:
                print('go back to original_url')
                driver.get(original_url)
            else:
                url = ""
                if type(value) == str:
                    if "http" in value:
                        url = value
                    else:
                        url = get_element_data(
                            driver=driver,
                            selector=value, property="href")
                elif type(value) == dict:
                    url = get_element_data(
                        driver=driver,
                        selector=value['selector'],
                        property=value['property'])
                # print(url)
                if url.strip() != "" and url is not None:
                    # print(url)
                    driver.get(url.strip())
                    time.sleep(3)

        # ---------------- SCRAPPING ---------------------

        elif ':loop' in step:
            listing = []
            for _ in range(value['pagination']):
                pi = play_sequence(
                    driver=driver, sequence=value['listing'], data=[])
                listing.extend(pi.copy())
            print(str(len(listing)) + " urls founded")
            for e in range(len(listing)):
                time.sleep(3)
                if type(listing[e]) == str:
                    items_loop = play_sequence(url=listing[e], driver=driver, data=[], item={
                        "URL": driver.current_url()
                    }, sequence=find_model(listing[e])['sequence'])
                    pprint(items_loop[0])
                    if len(items_loop) == 1:
                        data.append(items_loop[0].copy())
                    elif len(items_loop) > 1:
                        data.extend(items_loop)
                    # item['url'] = e
                print(f"application {e} / {listing}")

        if ":find_email" in step:
            website_search = get_element_data(
                driver=driver, selector=value['selector'], property='href')
            appo = '"'
            td = selenium_driver(inconito=True, url=f"https://www.google.com/search/q={website_search}+{appo}@{appo}+{appo}contact{appo}")
            # td.get(f"https://google.com/{website_search} {appo}@{appo} {appo}contact{appo}")
            # td.write("textarea[name=q]", "python")
            # td.write("textarea[name=q]", Keys.ENTER)
            # td.write("textarea[name=q]",
            #     f"{website_search} {appo}@{appo} {appo}contact{appo}")
            # td.write("textarea[name=q]", Keys.ENTER)
            # td.click('span.recaptcha-checkbox')
            time.sleep(999)
            re_email = re.findall(
                r'[\w.+-]+@[\w-]+\.[\w.-]+', td.find_element('body').get_property('innerText'))
            # print(bool(re_email))
            # if not bool(re_email):
            #     driver.get(
            #         f"https://google.com/search?q={website_search} {appo}@{appo} mail {appo}contact{appo}")
            #     time.sleep(1)
            #     re_email = re.findall(
            #         r'[\w.+-]+@[\w-]+\.[\w.-]+', driver.find_element('body').get_property('innerText'))
            if len(re_email) > 0:
                sfe = re_email[0]
            else:
                sfe = ''
            print(sfe)
            item[value['property']] = sfe

        if ':sequence' in step:
            ps = play_sequence(
                driver=driver, item={}, data=[], sequence=value)
            if len(ps) == 1:
                for prop in ps[0]:
                    item[prop] = ps[0][prop]

        elif ':get' in step:

            if property == "":

                if ":all" in step:
                    if type(value) == str:
                        v = get_elements_data(
                            driver=driver, selector=value['selector'], property="innerText")
                    elif type(value) == dict:
                        v = get_elements_data(
                            driver=driver,
                            selector=value['selector'],
                            property=value['property'])
                    data.extend(v.copy())
                    continue
                else:
                    pass

            else:
                if type(value) == str:
                    item[property] = get_element_data(
                        driver=driver, selector=value, property="innerText")
                elif type(value) == dict:
                    item[property] = get_element_data(
                        driver=driver,
                        selector=value['selector'],
                        property=value['property'])
                continue

        else:
            pass

    if len(list(item)) > 0:
        if verbose_item:
            pprint(item)
        data.append(item.copy())
    return data
