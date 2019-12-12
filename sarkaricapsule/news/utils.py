from events.models import Event
from news.models import News
from core.utils import generate_random_string

def create_job_news(event, created):
    
    event.refresh_from_db()

    news_description = f"""
        {event.organization.name} invited application for the post of {event.title} Read the complete
        information about this sarkari result and get a
        direct link to apply online. Last date to apply online is {event.start_date}. Minimum age to apply
        for {event.title} is {event.min_eligible_age} and maximum age is {event.max_eligible_age} Get the
        complete details of all the
        vacancies of {event.organization.name} here. {event.organization.description}
    """

    important_dates = '<br />'.join([(i.title + ': ' + i.date.strftime("%j%M,%Y")) for i in event.importantDates.all()])
    application_fees = '<br />'.join([(i.title + ': Rs ' + str(i.amount))
                                    for i in event.fees.all()])
    eligibility_criterias = '<br />'.join(
        [(i.title + ': ' + i.criteria) for i in event.eligibilities.all()])

    news_body = f"""
        Please read the important dates details carefully
        {important_dates}

        Application fee details for the {event.page_title} is given below
        {application_fees}


        How to pay online fee of {event.page_title}?
        {event.payment_method}

        You can only apply for the {event.page_title} if you are eligible, so read the eligibility criteria carefully
        before you
        apply.

        {eligibility_criterias}

        Vacancy Details of {event.page_title} is given below….

        {event.vacancy_details}

        All the important links for the {event.page_title} is given below

        Click on the respective link to get the deatils...
    """

    try:
        news = News(
            title=("New Job is announced: " if created else "Job is Updated: ") + event.title + "",
            slug=event.slug + generate_random_string()+ "-news",
            description=news_description,
            meta_tags=event.meta_keywords,
            meta_description=news_description,
            event=event,
            body=news_body
        )

        news.save()

    except:
        print("Error occured during job news creation")
    finally:
        print("     =====> Job News Created")



def create_result_news(event, created):
    print("     =====> Result News Created")


def create_admitcard_news(event, created):
    print("     =====> AdmitCard News Created")
