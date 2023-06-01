from pprint import pprint
import random


def rand():
    return random.randrange(0, 999) * random.randrange(0, 999)


sequences = {
    "indeed": {
        "COMPANY": {
            "COMPANY_NAME:get": 'header > h2',
            "COMPANY_RATE:get": 'li[data-tn-element="reviews-tab"] > a > div',
            "COMPANY_JOBS_COUNT:get": 'li[data-tn-element="jobs-tab-tab"] > a > div',
            "COMPANY_CREATION_DATE:get": 'li[data-testid="companyInfo-founded"] > div:last-child',
            "COMPANY_EMPLOYEES_COUNT:get": 'li[data-testid="companyInfo-employee"] > div:last-child',
            "COMPANY_REVENUE:get": 'li[data-testid="companyInfo-revenue"] > div:last-child',
            "COMPANY_SECTOR:get": 'li[data-testid="companyInfo-industry"] > div:last-child',
            "COMPANY_LOCATION:get": 'li[data-testid="companyInfo-headquartersLocation"] > div:last-child',
            # COMPANY EMAIL
            "COMPANY_WEBSITE:get": {
                "selector": 'li[data-testid="companyInfo-companyWebsite"] a',
                "property": "href"
            },
            # APPLICATION
            f":goto_{rand()}": 'li[data-tn-element="interviews-tab"] > a',
            "COMPANY_APPLICATION_EXPERIENCE:get": '[data-tn-component="summary-experience-card"] > div > div > div:last-child',
            "COMPANY_APPLICATION_DIFFICULTY:get": '[data-tn-component="summary-difficulty-card"] > div > div > div:last-child',
            "COMPANY_APPLICATION_TIME:get": '[data-tn-component="summary-hiring-duration-card"] > div > div > div:last-child',
        },
        "RECRUITER": {

        }
    },
    "linkedin": {
        'COMPANY': {
            "COMPANY_NAME:get": "h1 > span",
            "COMPANY_SHORT_DESCRIPTION:get": "p.org-top-card-summary__tagline",
            "COMPANY_SECTOR:get": ".org-top-card-summary-info-list > div",
            "COMPANY_LOCATION:get": ".org-top-card-summary-info-list > .inline-block > div",
            "COMPANY_LINKEDIN_SUSCRIBERS_COUNT:get": ".org-top-card-summary-info-list > .inline-block > div:nth-child(2)",
            "COMPANY_EMPLOYEES_COUNT:get": ".org-top-card-summary-info-list > .inline-block > div:nth-child(3)",
            f":click_{rand()}": "ul.org-page-navigation__items > li:nth-child(2)",
            f":wait_{rand()}": 2,
            # "COMPANY_PHONE:get": 'dl > dd + dt + dd',
            "COMPANY_WEBSITE:get": "dl > dd a",
            f":find_email_{rand()}": {
                "selector": "dl > dd a",
                "property": "COMPANY_EMAIL"
            },
        },
        "JOB": {
            "JOB_NAME:get": "h1",
            "JOB_LOCATION:get": "span.jobs-unified-top-card__bullet",
            "JOB_TIME:get": "span.jobs-unified-top-card__posted-date",
            "JOB_WORKSPACE:get": "span.jobs-unified-top-card__workplace-type",
            "JOB_APPLICATION_COUNT:get": "span.jobs-unified-top-card__applicant-count",
            "JOB_SPECIFICATIONS:get": "ul > li.jobs-unified-top-card__job-insight > span",
        },
        "PEOPLE": {
            "PEOPLE_NAME:get": ".pv-text-details__left-panel h1",
            "PEOPLE_TITLE:get": ".pv-text-details__left-panel > .text-body-medium",
            ":click": "span.pv-text-details__separator > #top-card-text-details-contact-info",
            ":wait": 3,
            "PEOPLE_BIRTHDAY": "section.pv-contact-info__contact-type.ci-birthday > div",
            "PEOPLE_TWITTER:get": {
                "selector": "section.pv-contact-info__contact-type.ci-twitter > a",
                "property": "href"
            }
        },
        "RECRUITER": {
            "RECRUITER_NAME:get": ".pv-text-details__left-panel h1",
            "RECRUITER_TITLE:get": ".pv-text-details__left-panel > .text-body-medium",
            ":click": "span.pv-text-details__separator > #top-card-text-details-contact-info",
            ":wait": 3,
            "RECRUITER_BIRTHDAY": "section.pv-contact-info__contact-type.ci-birthday > div",
            "RECRUITER_TWITTER:get": {
                "selector": "section.pv-contact-info__contact-type.ci-twitter > a",
                "property": "href"
            }
        }
    }
}


all_models = [
    # LINKEDIN
    {
        "website": "linkedin.com",
        "type": "jobs",
        "RegexUrl": ["/jobs/search"],
        "sequence": {
            ":loop": {
                "pagination": 40,
                "listing": {
                    ":execute_script": 'document.querySelector("div.jobs-search-results-list").scroll(0, 999999)',
                    ":get:all": {"property": "href", "selector": 'div.artdeco-entity-lockup__title > a.job-card-container__link'},
                    ":click": 'div.jobs-search-results-list__pagination li.selected + li',
                },
            }
        }
    },
    {
        "website": "linkedin.com",
        "type": "job",
        "RegexUrl": ["/jobs/view"],
        "sequence": {
            "JOB_NAME:get": "h1",
            "JOB_LOCATION:get": "span.jobs-unified-top-card__bullet",
            "JOB_TIME:get": "span.jobs-unified-top-card__posted-date",
            "JOB_WORKSPACE:get": "span.jobs-unified-top-card__workplace-type",
            "JOB_APPLICATION_COUNT:get": "span.jobs-unified-top-card__applicant-count",
            "JOB_SPECIFICATIONS:get": "ul > li.jobs-unified-top-card__job-insight > span",
            # COMPANY
            "COMPANY_LINKEDIN:get": {
                "selector": "section.jobs-company a",
                "property": "href"
            },
            f":click_{rand()}": "section.jobs-company a",
            f":sequence_{rand()}": sequences['linkedin']['COMPANY'],
            f":goto_{rand()}": ":original_url",
            # RECRUITER
            "RECRUITER_LINK:get": {
                "selector": ".hirer-card__hirer-information > a.app-aware-link",
                "property": "href"
            },
            # f":click_{rand()}": ".hirer-card__hirer-information > a.app-aware-link",
            # f":sequence_{rand()}": sequences['linkedin']['RECRUITER']
        }
    },
    {
        "website": "linkedin.com",
        "type": "companies",
        "RegexUrl": ["/search/results/companies"],
        "sequence": {
            ":loop": {
                "pagination": 1,
                "listing": {
                    ":execute_script": 'document.querySelector("html").scroll(0, 9999999)',
                    ":get:all": {"property": "href", "selector": 'span.entity-result__title-text > a.app-aware-link'},
                    ":click": 'ul.artdeco-pagination__pages > li.selected + li',
                },
            }
        }
    },
    {
        "website": "linkedin.com",
        "type": "company",
        "RegexUrl": ["/company/", "/school/"],
        "sequence": sequences['linkedin']['COMPANY']
    },
    {
        "website": "linkedin.com",
        "type": "people",
        "RegexUrl": ["/in/"],
        "sequence": sequences['linkedin']['PEOPLE']
    },
    # INDEED
    {
        "website": "indeed.com",
        "type": "jobs",
        "RegexUrl": ["/jobs"],
        "sequence": {
            ":loop": {
                "pagination": 1,
                "listing": {
                    ":execute_script": 'document.querySelector("html").scroll(0, 9999999)',
                    ":get:all": {"property": "href", "selector": 'td.resultContent h2 > a'},
                    ":click": "#mosaic-modal-mosaic-provider-desktopserp-jobalert-popup > div > div > div.icl-Modal > div > button",
                    ":click": 'nav[role="navigation"] > div:last-child > a',
                },
            }
        }
    },
    {
        "website": "indeed.com",
        "type": "job",
        "RegexUrl": ["/viewjob", '/job/'],
        "sequence": {
            "JOB_TITLE:get": "h1 > span",
            "JOB_LOCATION:get": ".css-6z8o9s > div",
            "JOB_SPECIFICATION:get": "span.jobsearch-JobMetadataHeader-item",
            "JOB_REQUIREMENTS:get": "#qualificationsSection li > p",
            "JOB_TIME:get": "#mosaic-belowFullJobDescription + .css-q7fux ul li > *:last-child",
            "JOB_ADVANTAGE:get": "#benefits > div",
            "JOB_WORKTIME:get": "#jobDetailsSection > div:last-child > div:last-child",
            # COMPANY
            "COMPANY_LOCATION:get": ".css-6z8o9s > div",
            "COMPANY_PAGE:get": {
                "selector": ".jobsearch-CompanyInfoContainer a",
                "property": "href"
            },
            ":goto": ".jobsearch-CompanyInfoContainer a",
            ":sequence": sequences['indeed']['COMPANY'],
            # f":goto_{rand()}": ":original_url",
            # ":execute_script": "history.back();",
            # ":wait": 2,
        }
    },
    {
        "website": "indeed.com",
        "type": "company",
        "RegexUrl": ["/cmp/"],
        "sequence": {
            "COMPANY_NAME:get": 'header > h2',
            "COMPANY_RATE:get": 'li[data-tn-element="reviews-tab"] > a > div',
            "COMPANY_JOBS_COUNT:get": 'li[data-tn-element="jobs-tab-tab"] > a > div',
            "COMPANY_CREATION_DATE:get": 'li[data-testid="companyInfo-founded"] > div:last-child',
            "COMPANY_EMPLOYEES_COUNT:get": 'li[data-testid="companyInfo-employee"] > div:last-child',
            "COMPANY_REVENUE:get": 'li[data-testid="companyInfo-revenue"] > div:last-child',
            "COMPANY_SECTOR:get": 'li[data-testid="companyInfo-industry"] > div:last-child',
            "COMPANY_LOCATION:get": 'li[data-testid="companyInfo-headquartersLocation"] > div:last-child',
            # COMPANY EMAIL
            "COMPANY_WEBSITE:get": {
                "selector": 'li[data-testid="companyInfo-companyWebsite"] a',
                "property": "href"
            },
            # APPLICATION
            ":goto": 'li[data-tn-element="interviews-tab"] > a',
            "COMPANY_APPLICATION_EXPERIENCE:get": '[data-tn-component="summary-experience-card"] > div > div > div:last-child',
            "COMPANY_APPLICATION_DIFFICULTY:get": '[data-tn-component="summary-difficulty-card"] > div > div > div:last-child',
            "COMPANY_APPLICATION_TIME:get": '[data-tn-component="summary-hiring-duration-card"] > div > div > div:last-child',
            # ":execute_script": "history.back();",
            # ":wait": 2,
        }
    },
    # POLE EMPLOI
    {
        "website": "pole-emploi.com",
        "type": "jobs",
        "RegexUrl": ["/offres/recherche"],
        "sequence": {
            ":loop": {
                "pagination": 1,
                "listing": {
                    ":execute_script": 'document.querySelector("html").scroll(0, 9999999)',
                    ":click": "#zoneAfficherPlus a",
                    ":execute_script": 'document.querySelector("html").scroll(0, 9999999)',
                    ":click": "#zoneAfficherPlus a",
                    ":execute_script": 'document.querySelector("html").scroll(0, 9999999)',
                    ":click": "#zoneAfficherPlus a",
                    ":get:all": {"property": "href", "selector": 'li.result > a.media'}
                },
            }
        }
    },
    {
        "website": "pole-emploi.com",
        "type": "job",
        "RegexUrl": ["/offres/recherche/detail/"],
        "sequence": {
            "JOB_NAME:get": "#labelPopinDetailsOffre > span:last-child",
            "JOB_LOCATION:get": 'p[itemprop="jobLocation"] span[itemprop="name"]',
            "JOB_TIME:get": 'span[itemprop="datePosted"]',
            "JOB_SPECIFICATION:get": 'div.description-aside dd',
            "JOB_WORTIME:get": 'div.description-aside dd[itemprop="workHours"]',
            "JOB_REVENUE:get": 'div.description-aside [itemprop="baseSalary"] + ul li',
            # "JOB_EXPERIENCE:get": "",
            # "JOB_REQUIREMENTS:get": "",
            # "JOB_SKILLS:get": "",
            # "JOB_INFOS": "",
            "COMPANY_NAME:get": '[itemprop="hiringOrganization"] + h2 + .media .media-body h3',
            "COMPANY_PHONE:get": '[itemprop="hiringOrganization"] + h2 + .media [itemprop="telephone"]',
            "COMPANY_WEBSITE:get": '[itemprop="hiringOrganization"] + h2 + .media .media-body dl a',
            ":click": '[itemprop="hiringOrganization"] + h2 + .media .media-body p > a',
            ":sequence": None,
        }
    },
    {
        "website": "pole-emploi.com",
        "type": "company",
        "RegexUrl": ["/page-entreprise"],
        "sequence": {
            "COMPANY_NAME:get": "h1",
            "COMPANY_TITLE:get": "h1 + p",
            "COMPANY_EMPLOYEES_COUNT": ".bloc-illustration > div span > p:last-child",
            "COMPANY_SECTOR": ".bloc-illustration > div:last-child span > p:last-child",
            "COMPANY_EMAIL": ".vcard-entreprise .vcard-descriptif > p:last-child",
            "COMPANY_WEBSITE": ".vcard-entreprise .vcard-descriptif > p:last-child a",
            # "COMPANY_FACEBOOK": "",
            # "COMPANY_TWITTER": "",
            # "COMPANY_LINKEDIN": "",
        }
    }
]


def find_model(url=None, models=all_models):
    if url is None:
        return
    print('find_model')
    for model in models:
        if model['website'] in url:
            for regex in model['RegexUrl']:
                if regex in url:
                    # pprint(model)
                    return model
                else:
                    pass
        else:
            pass
    print(url)
    print('Aucun modèle')
