text = '''Apache Airflow is an open-source workflow management platform for data engineering pipelines.
It started at Airbnb in October 2014 as a solution to manage the company's increasingly complex workflows.
Creating Airflow allowed Airbnb to programmatically author and schedule their workflows and monitor them via the built-in Airflow user interface.
From the beginning, the project was made open source, becoming an Apache Incubator project in March 2016 and a Top-Level Apache Software Foundation project in January 2019.

Airflow is written in Python, and workflows are created via Python scripts.
Airflow is designed under the principle of "configuration as code".
While other "configuration as code" workflow platforms exist using markup languages like XML, using Python allows developers to import libraries and classes to help them create their workflows.

Airflow uses directed acyclic graphs (DAGs) to manage workflow orchestration.
Tasks and dependencies are defined in Python and then Airflow manages the scheduling and execution. DAGs can be run either on a defined schedule (e.g. hourly or daily) or based on external event triggers (e.g. a file appearing in Hive).
Previous DAG-based schedulers like Oozie and Azkaban tended to rely on multiple configuration files and file system trees to create a DAG, whereas in Airflow, DAGs can often be written in one Python file.

Three notable providers offer ancillary services around the core open source project.
Astronomer has built a SaaS tool and Kubernetes-deployable Airflow stack that assists with monitoring, alerting, devops, and cluster management.
Cloud Composer is a managed version of Airflow that runs on Google Cloud Platform (GCP) and integrates well with other GCP services.
Starting from November 2020, Amazon Web Services offers Managed Workflows for Apache Airflow.'''

non_alphabetical = [',', '.', '\'', '\"', '?', '!', '/', '\\', '@', '#',
                    '$', '%', '(', ')', '+', '-', '=', '*', '&', '<', '>', ]

class Word:
    def __init__(self, word: str, quantity: int):
        self.word = word
        self.quantity = quantity


with open('article.txt', 'r') as read_file:
    all_lines = read_file.read().split('\n')
    all_words = []
    dicts = []
    unique_words = []

    for line in all_lines:
        if line == '':
            all_lines.remove(line)

    for line in all_lines:

        unique_line_words = []

        for symbol in non_alphabetical:
            line = line.replace(symbol, '')

        all_line_words = line.split()

        for word in all_line_words:
            if not word.lower() in unique_line_words:
                unique_line_words.append(word.lower())

        for unique in unique_line_words:
            quantity = 0
            for word in all_line_words:
                if word.lower() == unique.lower():
                    quantity += 1
            word_obj = Word(unique.lower(), quantity)
            all_words.append(word_obj)


for word_ in all_words:

    if word_.word not in unique_words:
        unique_words.append(word_.word)
        dicts.append({'word': word_.word, 'quantity': word_.quantity})

    else:
        dicts[unique_words.index(word_.word)]['quantity'] += word_.quantity



dicts.sort(key=lambda x: x['quantity'])

# for dictionary in dicts:
#     print(dictionary)

print(dicts[-2])





