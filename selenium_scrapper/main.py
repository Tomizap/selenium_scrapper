import time


def get_urls(driver=None, default=[], setting={
    "limit": 100,
    "pagination": {
        "count": 1,
        "selector": 'body'
    },
    "scripts": [],
    "clicks": [],
    "items": {
        "selector": 'body',
        "property": "innerText",
        "attribute": None
    }
}):
    if driver is None:
        return default
    print('get urls')
    urls = default
    for _ in range(setting['pagination']['count']):
        if len(urls) > setting['limit']:
            break
        for script in setting['scripts']:
            try:
                driver.execute_script(script)
            except:
                pass
        time.sleep(2)
        for _ in range(3):
            try:
                items = driver.find_elements(setting['items']['selector'])
                for item in items:
                    urls.append(item.get_property('href'))
                break
            except:
                time.sleep(1)
        print('pagination el: ' + str(driver.is_attached(setting['pagination']['selector'])))
        try:
            driver.click(
                setting['pagination']['selector'])
        except:
            break
    print(str(len(urls)) + ' urls found')
    return urls


def get_data(driver=None, model=[], default={}) -> dict:
    print('get data')
    item = default
    if driver is not None:
        for row in model:
            prop = row[0]
            value = row[1]
            try:
                if 'http' in value:
                    item[prop] = value
                elif len(row) > 2:
                    item[prop] = driver.find_element(
                        value).get_property(row[2])
                else:
                    item[prop] = driver.find_element(
                        value).get_property('innerText')
            except:
                pass
    return item


def selenium_scrapper(driver=None, limit=100, url=None):

    if driver is None:
        return []
    print('scrapping')
    if url is not None:
        driver.get(url)
    url = driver.current_url()
    data = []
    # urls = []

    # ================================================================================
    # ================ START MODIFY FROM HERE ===================================
    # ================================================================================

    # ---------- ECOMMERCE -------------

    if '://www.amazon' in url or '://amazon' in url:
        pass

    # ---------- SOCIAL -------------

    elif '://twitter' in url:
        pass

    elif '://pinterest' in url:
        pass

    elif '://facebook' in url:
        pass

    elif '://instagram' in url:
        pass

    elif '://linkedin' in url or '://www.linkedin' in url:

        if '/jobs' in url:

            model = [
                ['company', 'span.jobs-unified-top-card__company-name > a'],
                ['company_link', 'span.jobs-unified-top-card__company-name > a', 'href'],
                ['location', 'span.jobs-unified-top-card__bullet'],
                ['time', 'span.jobs-unified-top-card__posted-date'],
                ['workspace', 'span.jobs-unified-top-card__workplace-type'],
                ['application_count', 'span.jobs-unified-top-card__applicant-count'],
                ['recruiter', '.hirer-card__hirer-information > a'],
                ['recruiter_url', '.hirer-card__hirer-information > a', "href"],
                ['recruiter_title',
                 'div.hirer-card__hirer-information .hirer-card__hirer-job-title'],
            ]

            if '/search' in url:

                setting = {
                    "limit": limit,
                    "pagination": {
                        "count": 1,
                        "selector": 'div.jobs-search-results-list__pagination li.selected + li'
                    },
                    "scripts": [
                        'document.querySelector("div.jobs-search-results-list").scroll(0, 99999)',
                        'document.querySelector("html").scroll(0, 99999)'],
                    "items": {
                        "selector": 'div.artdeco-entity-lockup__title > a.job-card-container__link'
                    }
                }
                urls = get_urls(driver=driver, setting=setting)
                for i in range(len(urls)):
                    driver.get(url=urls[i])
                    data.append(selenium_scrapper(driver=driver))

            elif '/view' in url:

                data = get_data(driver=driver, model=model, default={
                    'ID': driver.current_url().split('/')[5],
                    'job_link': driver.current_url(),
                    "job_application_link": "https://linkedin.com/job-apply/" + str(driver.current_url().split('/')[5])
                })

        elif '/companies' in url:

            model = []

            if '/search' in url:

                setting = {
                    "limit": limit,
                    "pagination": {
                        "count": 40,
                        "selector": 'div.jobs-search-results-list__pagination li.selected + li'
                    },
                    "scripts": [
                        'document.querySelector("div.jobs-search-results-list").scroll(0, 99999)',
                        'document.querySelector("html").scroll(0, 99999)'],
                    "items": {
                        "selector": 'div.artdeco-entity-lockup__title > a.job-card-container__link'
                    }
                }
                for i in range(len(get_urls(driver=driver, setting=setting))):
                    data.append(selenium_scrapper(driver=driver, url=urls[i]))

            elif '/view' in url:

                data = get_data(driver=driver, model=model, default={
                    'ID': driver.current_url().split('/')[5],
                    'url': driver.current_url(),
                })

        elif '/groups' in url:

            model = []

            if '/search' in url:

                setting = {
                    "limit": limit,
                    "pagination": {
                        "count": 40,
                        "selector": 'div.jobs-search-results-list__pagination li.selected + li'
                    },
                    "scripts": [
                        'document.querySelector("div.jobs-search-results-list").scroll(0, 99999)',
                        'document.querySelector("html").scroll(0, 99999)'],
                    "items": {
                        "selector": 'div.artdeco-entity-lockup__title > a.job-card-container__link'
                    }
                }
                for i in range(len(get_urls(driver=driver, setting=setting))):
                    data.append(selenium_scrapper(driver=driver, url=urls[i]))

            elif '/view' in url:

                data = get_data(driver=driver, model=model, default={
                    'ID': driver.current_url().split('/')[5],
                    'url': driver.current_url(),
                })

        elif '/people' in url:

            model = []

            if '/search' in url:

                setting = {
                    "limit": limit,
                    "pagination": {
                        "count": 1,
                        "selector": 'ul.artdeco-pagination__pages > li.selected + li'
                    },
                    "scripts": ['document.querySelector("html").scroll(0, 99999)'],
                    "items": {
                        "selector": 'span.entity-result__title-text > a.app-aware-link'
                    }
                }
                urls = get_urls(driver=driver, setting=setting)
                for i in range(len(urls)):
                    data.append(selenium_scrapper(driver=driver, url=urls[i]))

        elif '/in' in url:

            model = [
                ['name', '.pv-text-details__left-panel h1'],
                ['title', '.pv-text-details__left-panel .text-body-medium'],
                ['relation_count', 'ul.pv-top-card--list .t-bold'],
                ['company', '.pv-text-details__right-panel-item-text']
            ]
            data = get_data(driver=driver, model=model, default={
                'ID': driver.current_url().split('/')[4],
                'contact_link': driver.current_url(),
            })

    # ---------- JOBS -------------

    elif 'pole-emploi.fr' in url:
        pass

    elif 'alternance.emploi.gouv.fr' in url:
        pass

    elif 'indeed.com' in url:
        pass

    # ================================================================================
    # =================================== STOP MODIFY ===================================
    # ================================================================================

    return data
