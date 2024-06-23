import os
def add_job_nodes(response, job_name, date_posted):
    job = response.job

    if "Before" in date_posted:
        date_posted = date_posted.split()[1]

    # Create job nodes
    cypher = f'''
    CREATE (job:Job {{name: "{job_name}"}})
    SET job.status = "Opening"
    SET job.date_posted = date("{date_posted}")
    '''

    # Work Levels
    if job.work_level:
        cypher += f'''
        SET job.workLevel = "{job.work_level}"
        '''

    # Job description
    if job.description:
        cypher += f'SET job.description = "{job.description}"'

    # Work mode
    if job.work_mode:
        cypher += f'''
        SET job.workMode = "{job.work_mode}"
        '''

    # Benefits & Compensations
    if job.benefit_compensation:
        cypher += f'''
        SET job.benefitCompensation = "{job.benefit_compensation}"
        '''

    # Locations
    if job.work_at:
        cypher += f'''
    MERGE (loc: Location {{name: "{job.work_at.name}", locationType: "{job.work_at.location_type}"}})
    MERGE (job)-[:WORK_AT]->(loc)
    '''

    # Required educations
    if job.education_requirements:
        for i, edu in enumerate(job.education_requirements):
            cypher += f'''
        CREATE (edu_{i}:Education {{name: "{edu.name}"}})
        MERGE (job)-[:REQUIRES]->(edu_{i})
            '''

            if edu.fields:
                cypher += f'SET edu_{i}.fields = "{edu.fields}"'

            if edu.status:
                cypher += f'SET edu_{i}.status = "{edu.status}"'

    # Required skills
    if job.skill_requirements:
        for i, skill in enumerate(job.skill_requirements):
            cypher += f'''
        MERGE (skill_{i}:Skill {{name: "{skill.name}"}})
        MERGE (job)-[:REQUIRES]->(skill_{i})
            '''

            if skill.hypernym:
                cypher += f'''
        MERGE (hypernym_{i}:Skill {{name: "{skill.hypernym}"}})
        MERGE (skill_{i})-[:HYPERNYM]->(hypernym_{i})  
        '''

    # Required work experiences
    if job.work_exper_requirements:
        for i, exper in enumerate(job.work_exper_requirements):
            cypher += f'''
        MERGE (exper_{i}:Work_Exper {{name: "{exper.name}"}})
        MERGE (job)-[:REQUIRES]->(exper_{i})
        '''

            if exper.duration:
                cypher += f'SET exper_{i}.duration = "{exper.duration}"'

    return cypher

def add_company_nodes(response, company_name):
    company = response.job.from_company

    cypher = f'''
    MERGE (company:Company {{name: "{company_name}"}})
    MERGE (job)-[:FROM]->(company)
    MERGE (company)-[:RECRUITS]->(job)
        '''

    if company:
        if company.locations:
            for i, loc in enumerate(company.locations):
                cypher += f'''
            MERGE (loc_{i}:Location {{name: "{loc.name}"}})
            MERGE (company)-[:LOCATED_IN]->(loc_{i})
                '''

                if loc.location_type:
                    cypher += f'SET loc_{i}.locationType = "{loc.location_type}"'

        if company.industry:
            for i, industry in enumerate(company.industry):
                cypher += f'''
            MERGE (industry_{i}:Industry {{name: "{industry}"}})
            MERGE (company)-[:OPERATED_IN]->(industry_{i})
                '''

    return cypher

def add_jobs2kg(response, job_title, company_name, date_posted):
    job_cypher = add_job_nodes(response, job_title, date_posted)
    company_cypher = add_company_nodes(response, company_name)
    return job_cypher + company_cypher

def update_job_status(job_list):
    update_cypher = ""
    for job in job_list:
        job_title, company = job["title"], job["company"]
        update_cypher += f"""
        MATCH (j:Job {{name: "{job_title}"}})-[:FROM]->(c:Company {{name: "{company}"}})
        SET j.status = "Closed"
        """

    return update_cypher

if __name__ == "__main__":
    pass
    # _, closed_jobs = manage_jobs()
    # print(update_job_status(closed_jobs))


