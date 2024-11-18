# lessons.py

lessons = {
    'laborlaw1': {
        'title': 'Chapter 1 - Labor Law',
        'content': [
            """
            Isang kahig, isang tuka...a meek characterization commonly tagged to most Filipino laborers, to portray
            the daily plight of an ordinary worker whose hands act as nothing more than a conduit of the money he earns,
            from his paycheck towards the overwhelming expenses that he and his family has to incur in order to withstand
            the survival-driven society that we are in. Therefore, he would most likely concern himself solely on receiving
            the monetary equivalent of the services that he has and will be rendering for another person. However, more than
            just wages and bonuses, his/her labor rights comprehend a wider array of benefits and remunerations than what is
            being extended to him/her - much less he/she is being made aware of.
            """,
            """
            So the first question we have to address before we go wobbly with technical terms and legal jargons as regards
            employment rights and duties is: what is labor law? It is a law that governs the rights and duties of employers
            and employees, with respect to the following:
            1. terms and conditions of employment
            2. labor disputes arising from collective bargaining respecting such terms and conditions
            """,
            """
            From the above-mentioned definition, two major divisions of Labor Law were formulated - the first one is Labor
            Standard laws, while the second is Labor Relations laws. The former deals primarily with the minimum standards of
            labor, such as wages, hours of work and other terms and conditions; the latter deals with how the employer-employee
            relations serves as the foundation for resorting to legal and peaceful means of resolving any dispute or disagreement
            arising from the terms and conditions of employment.
            """
        ]
    },
    'laborlaw2': {
        'title': 'Chapter 1 - Labor Law',
        'content': [
            """
            Labor standards laws provide the LEAST terms and conditions of employment that employers MUST comply 
            with and to which employees are entitled as a matter of LEGAL RIGHT. Labor relations law, on the other
            hand, defines the status, rights and duties, and the institutional mechanisms that govern the 
            individual and collective interactions, of employers, employees and their representatives.
            """,

            """
            But although the distinction between labor standards and labor relations is useful for academic purposes, 
            they in reality overlap. The question what am I entitled to under the law is addressed in Labor standards 
            laws; and the query how can I upgrade these minimum standards is shed light under Labor relations laws. 
            These two major divisions of labor law shall be discussed in this book in a juxtaposed manner.
            """,

            """
            Labor Standard laws, in themselves, do not guarantee lasting industrial peace, as they only provide for 
            the minimum standards of employment. Labor relations laws, by enabling workers to obtain improvements of 
            the benefits guaranteed by labor standard laws and by providing for a mechanism by which disputes between 
            the employer and his employees are expeditiously settled, can assure a stable and lasting industrial peace.
            """,

            """
             The Labor Code of the Philippines (PD 442), hereinafter referred to as the Labor Code, is the most basic 
             labor law in our country, which took effect on November 1, 1974. It is a set of substantive and procedural 
             laws that prescribe the principal rights and responsibilities of employers, employees, and other industrial 
             participants, as well as the roll of the Government, in employment and related activities, so as to institute 
             social justice. Under Article 3 of the Labor Code, it declares that the State shall:
              a. Afford protection to labor
              b. Promote full employment
              c. Ensure equal work opportunities regardless of sex, age or creed
              d. Regulate the relations between workers and employees, and
              e. Assure the right of workers to:
               • Just and humane working conditions of work
               • Self-Organization
               • Security of tenure, and
               • Collective bargaining
             Each item shall be elucidated thoroughly as this book progresses.
            """,

            """
            However, labor laws are not the only ones which govern the whole spectrum of employment rights and 
            duties. Judicial decisions, specifically that of the Supreme Court, applying and interpreting labor 
            laws are also taken into consideration. In addition, rules and regulations issued by administrative 
            agencies (such as the Department of Labor and Employment) within their legal competence implementing 
            labor laws are likewise mulled over. The latter two sources of labor rights and duties shall also be 
            discussed and incorporated in this book.
            """,
        ]
    },

'laborlaw3': {
        'title': 'Chapter 1 - Labor Law',
        'content': [
            """
            NNNNNNNNNLabor standards laws provide the LEAST terms and conditions of employment that employers MUST comply 
            with and to which employees are entitled as a matter of LEGAL RIGHT. Labor relations law, on the other
            hand, defines the status, rights and duties, and the institutional mechanisms that govern the 
            individual and collective interactions, of employers, employees and their representatives.
            """,

            """
            But although the distinction between labor standards and labor relations is useful for academic purposes, 
            they in reality overlap. The question what am I entitled to under the law is addressed in Labor standards 
            laws; and the query how can I upgrade these minimum standards is shed light under Labor relations laws. 
            These two major divisions of labor law shall be discussed in this book in a juxtaposed manner.
            """,

            """
            Labor Standard laws, in themselves, do not guarantee lasting industrial peace, as they only provide for 
            the minimum standards of employment. Labor relations laws, by enabling workers to obtain improvements of 
            the benefits guaranteed by labor standard laws and by providing for a mechanism by which disputes between 
            the employer and his employees are expeditiously settled, can assure a stable and lasting industrial peace.
            """,

            """
             The Labor Code of the Philippines (PD 442), hereinafter referred to as the Labor Code, is the most basic 
             labor law in our country, which took effect on November 1, 1974. It is a set of substantive and procedural 
             laws that prescribe the principal rights and responsibilities of employers, employees, and other industrial 
             participants, as well as the roll of the Government, in employment and related activities, so as to institute 
             social justice. Under Article 3 of the Labor Code, it declares that the State shall:
              a. Afford protection to labor
              b. Promote full employment
              c. Ensure equal work opportunities regardless of sex, age or creed
              d. Regulate the relations between workers and employees, and
              e. Assure the right of workers to:
               • Just and humane working conditions of work
               • Self-Organization
               • Security of tenure, and
               • Collective bargaining
             Each item shall be elucidated thoroughly as this book progresses.
            """,

            """
            However, labor laws are not the only ones which govern the whole spectrum of employment rights and 
            duties. Judicial decisions, specifically that of the Supreme Court, applying and interpreting labor 
            laws are also taken into consideration. In addition, rules and regulations issued by administrative 
            agencies (such as the Department of Labor and Employment) within their legal competence implementing 
            labor laws are likewise mulled over. The latter two sources of labor rights and duties shall also be 
            discussed and incorporated in this book.
            """,
        ]
    },
    # Add more lessons as needed...
}

# Function to get a lesson by chapter name
def get_lesson(chapter_name):
    return lessons.get(chapter_name)
