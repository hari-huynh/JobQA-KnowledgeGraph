from configs import configure_setup
from job_pydantic import JobKnowledgeGraph
from utils.cypher_utils import add_jobs2kg, update_job_status
from utils.check_status import manage_jobs
from process_data import get_job_desc
from datetime import date
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "logs/update_kg.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

if __name__ == "__main__":
    knowledge_graph, client = configure_setup()

    with open("cypher/count_nodes.cypher", "r") as file:
        count_nodes_cypher = file.read()

    with open("cypher/count_relationships.cypher", "r") as file:
        count_relations_cypher = file.read()


    n_processed = 0
    # Get list new jobs & closed jobs
    new_jobs, closed_jobs = manage_jobs()
    logger.info(f"Have {len(new_jobs)} new job postings and {len(closed_jobs)} jobs no longer recruiting.")

    new_jobs_desc = get_job_desc(new_jobs)

    for jd_info in new_jobs_desc:
        try:
            job_title, company_name, job_desc, date_posted = jd_info
            job_desc = job_desc.replace('"', "'")

            system_prompt = f"""
            Help me understand the following by describing it as a detailed knowledge graph.
            Only extract and present only the factual information.
            For entities, always capitalize the first letter of each word.

            Job descriptions: {job_desc}
            """

            resp = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": system_prompt
                    }
                ],
                response_model=JobKnowledgeGraph,
                max_retries = 5
            )

            cypher = add_jobs2kg(resp, job_title, company_name, date_posted)
            knowledge_graph.query(cypher)
            print(f"Added {job_title} @ {company_name} to Knowledge Graph.")
            logger.info(f"Added {job_title} @ {company_name} to Knowledge Graph.")

            n_processed += 1
        except Exception as e:
            print(e)
            logger.info(e)
            continue

    print(f"Added {n_processed} new job postings!")
    logger.info(f"Added {n_processed} new job postings!")


    # Update jobs status of old jobs
    update_status_cypher = update_job_status(closed_jobs)
    knowledge_graph.query(update_status_cypher)
    print(f"Updated status {len(closed_jobs)} closed jobs!")
    logger.info(f"Updated status {len(closed_jobs)} closed jobs!")

    num_node = knowledge_graph.query(count_nodes_cypher)
    num_relation = knowledge_graph.query(count_relations_cypher)

    print(num_node[0], num_relation[0])
    logger.info(num_node[0])
    logger.info(num_relation[0])

