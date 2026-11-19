import unittest


import unittest

class AgentTest_post_job(unittest.TestCase):

    def test_post_job_1(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        self.assertEqual(
            marketplace.job_listings,
            [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}]
        )

    def test_post_job_2(self):
        marketplace = JobMarketplace()
        result = marketplace.post_job("Software Engineer", "ABC Company", ['requirement1'])
        self.assertIsNone(result)

    def test_post_job_3(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['requirement1'])
        marketplace.post_job("Data Analyst", "XYZ Corp", ['skill1', 'skill2'])
        self.assertEqual(len(marketplace.job_listings), 2)
        self.assertEqual(marketplace.job_listings[0]['job_title'], 'Software Engineer')
        self.assertEqual(marketplace.job_listings[1]['job_title'], 'Data Analyst')
        self.assertEqual(marketplace.job_listings[1]['company'], 'XYZ Corp')
        self.assertEqual(marketplace.job_listings[1]['requirements'], ['skill1', 'skill2'])

    def test_post_job_4(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['requirement1'])
        self.assertEqual(len(marketplace.job_listings), 1)
        self.assertEqual(
            set(marketplace.job_listings[0].keys()),
            {'job_title', 'company', 'requirements'}
        )

    def test_post_job_5(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Designer", "Design Co", [])
        self.assertEqual(marketplace.job_listings[0]['requirements'], [])
        self.assertEqual(marketplace.resumes, [])

import unittest

class AgentTest_remove_job(unittest.TestCase):

    def test_remove_job_1(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}]
        marketplace.remove_job(marketplace.job_listings[0])
        self.assertEqual(marketplace.job_listings, [])

    def test_remove_job_2(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1']}]
        result = marketplace.remove_job(marketplace.job_listings[0])
        self.assertIsNone(result)

    def test_remove_job_3(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [
            {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1']},
            {"job_title": "Data Analyst", "company": "XYZ Corp", "requirements": ['skill2']},
            {"job_title": "Designer", "company": "Design Co", "requirements": []},
        ]
        marketplace.remove_job(marketplace.job_listings[1])
        self.assertEqual(
            marketplace.job_listings,
            [
                {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1']},
                {"job_title": "Designer", "company": "Design Co", "requirements": []},
            ]
        )

    def test_remove_job_4(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        marketplace.remove_job({"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']})
        self.assertEqual(marketplace.job_listings, [])

    def test_remove_job_5(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['requirement1'])
        marketplace.post_job("Data Analyst", "XYZ Corp", ['skill1', 'skill2'])
        marketplace.remove_job(marketplace.job_listings[0])
        self.assertEqual(len(marketplace.job_listings), 1)
        self.assertEqual(marketplace.job_listings[0]['job_title'], 'Data Analyst')
        self.assertEqual(marketplace.job_listings[0]['company'], 'XYZ Corp')
        self.assertEqual(marketplace.job_listings[0]['requirements'], ['skill1', 'skill2'])

import unittest

class AgentTest_submit_resume(unittest.TestCase):

    def test_submit_resume_1(self):
        marketplace = JobMarketplace()
        marketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        self.assertEqual(
            marketplace.resumes,
            [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]
        )

    def test_submit_resume_2(self):
        marketplace = JobMarketplace()
        result = marketplace.submit_resume("Tom", ['skill1'], "experience")
        self.assertIsNone(result)

    def test_submit_resume_3(self):
        marketplace = JobMarketplace()
        marketplace.submit_resume("Tom", ['skill1'], "2 years")
        marketplace.submit_resume("Anna", ['skill2', 'skill3'], "5 years")
        self.assertEqual(len(marketplace.resumes), 2)
        self.assertEqual(marketplace.resumes[0]['name'], 'Tom')
        self.assertEqual(marketplace.resumes[1]['name'], 'Anna')
        self.assertEqual(marketplace.resumes[1]['skills'], ['skill2', 'skill3'])
        self.assertEqual(marketplace.resumes[1]['experience'], '5 years')

    def test_submit_resume_4(self):
        marketplace = JobMarketplace()
        marketplace.submit_resume("Tom", ['skill1'], "experience")
        self.assertEqual(len(marketplace.resumes), 1)
        self.assertEqual(
            set(marketplace.resumes[0].keys()),
            {'name', 'skills', 'experience'}
        )

    def test_submit_resume_5(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['requirement1'])
        marketplace.submit_resume("Tom", [], "")
        self.assertEqual(marketplace.resumes[0]['skills'], [])
        self.assertEqual(marketplace.resumes[0]['experience'], "")
        self.assertEqual(
            marketplace.job_listings,
            [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1']}]
        )

import unittest

class AgentTest_withdraw_resume(unittest.TestCase):

    def test_withdraw_resume_1(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        marketplace.withdraw_resume(marketplace.resumes[0])
        self.assertEqual(marketplace.resumes, [])

    def test_withdraw_resume_2(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1'], "experience": "2 years"}]
        result = marketplace.withdraw_resume(marketplace.resumes[0])
        self.assertIsNone(result)

    def test_withdraw_resume_3(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [
            {"name": "Tom", "skills": ['skill1'], "experience": "2 years"},
            {"name": "Anna", "skills": ['skill2', 'skill3'], "experience": "5 years"},
            {"name": "Bob", "skills": ['skill4'], "experience": "1 year"},
        ]
        marketplace.withdraw_resume(marketplace.resumes[1])
        self.assertEqual(
            marketplace.resumes,
            [
                {"name": "Tom", "skills": ['skill1'], "experience": "2 years"},
                {"name": "Bob", "skills": ['skill4'], "experience": "1 year"},
            ]
        )

    def test_withdraw_resume_4(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [
            {"name": "Tom", "skills": ['skill1'], "experience": "2 years"},
            {"name": "Anna", "skills": ['skill2', 'skill3'], "experience": "5 years"},
        ]
        marketplace.withdraw_resume({"name": "Anna", "skills": ['skill2', 'skill3'], "experience": "5 years"})
        self.assertEqual(len(marketplace.resumes), 1)
        self.assertEqual(marketplace.resumes[0]['name'], 'Tom')
        self.assertEqual(marketplace.resumes[0]['skills'], ['skill1'])
        self.assertEqual(marketplace.resumes[0]['experience'], '2 years')

    def test_withdraw_resume_5(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1']}]
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        marketplace.withdraw_resume(marketplace.resumes[0])
        self.assertEqual(marketplace.resumes, [])
        self.assertEqual(
            marketplace.job_listings,
            [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1']}]
        )

import unittest

class AgentTest_search_jobs(unittest.TestCase):

    def test_search_jobs_1(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(
            marketplace.search_jobs("skill1"),
            [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']}]
        )

    def test_search_jobs_2(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(marketplace.search_jobs("skill9"), [])

    def test_search_jobs_3(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [
            {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1']},
            {"job_title": "Data Analyst", "company": "XYZ Corp", "requirements": ['skill2', 'skill3']},
            {"job_title": "Designer", "company": "Design Co", "requirements": ['skill4']},
        ]
        self.assertEqual(
            marketplace.search_jobs("skill2"),
            [{"job_title": "Data Analyst", "company": "XYZ Corp", "requirements": ['skill2', 'skill3']}]
        )

    def test_search_jobs_4(self):
        marketplace = JobMarketplace()
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        result = marketplace.search_jobs("skill1")
        self.assertIsInstance(result, list)
        self.assertEqual(
            marketplace.job_listings,
            [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        )

    def test_search_jobs_5(self):
        marketplace = JobMarketplace()
        marketplace.post_job("Software Engineer", "ABC Company", ['python', 'sql'])
        marketplace.post_job("Data Analyst", "XYZ Corp", ['sql', 'excel'])
        marketplace.post_job("Designer", "Design Co", ['figma'])
        result = marketplace.search_jobs("sql")
        self.assertEqual(len(result), 2)
        self.assertCountEqual(
            [job['job_title'] for job in result],
            ['Software Engineer', 'Data Analyst']
        )

import copy

import unittest

class AgentTest_get_job_applicants(unittest.TestCase):

    def test_get_job_applicants_1(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(
            marketplace.get_job_applicants(marketplace.job_listings[0]),
            [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}]
        )

    def test_get_job_applicants_2(self):
        marketplace = JobMarketplace()
        marketplace.resumes = []
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(marketplace.get_job_applicants(marketplace.job_listings[0]), [])

    def test_get_job_applicants_3(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [
            {"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "2 years"},
            {"name": "Anna", "skills": ['skill9', 'skill10'], "experience": "5 years"},
        ]
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        result = marketplace.get_job_applicants(marketplace.job_listings[0])
        self.assertEqual(
            result,
            [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': '2 years'}]
        )

    def test_get_job_applicants_4(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        marketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        resumes_before = copy.deepcopy(marketplace.resumes)
        listings_before = copy.deepcopy(marketplace.job_listings)
        marketplace.get_job_applicants(marketplace.job_listings[0])
        self.assertEqual(marketplace.resumes, resumes_before)
        self.assertEqual(marketplace.job_listings, listings_before)

    def test_get_job_applicants_5(self):
        marketplace = JobMarketplace()
        marketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        marketplace.job_listings = [{"job_title": "Data Scientist", "company": "XYZ Corp", "requirements": ['skillX']}]
        result = marketplace.get_job_applicants(marketplace.job_listings[0])
        self.assertIsInstance(result, list)
        self.assertEqual(result, [])