import unittest


class JobMarketplaceTestPostJob(unittest.TestCase):
    def test_post_job(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        self.assertEqual(jobMarketplace.job_listings, [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}])

    def test_post_job_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.post_job("Mechanical Engineer", "XYZ Company", ['requirement3', 'requirement4'])
        self.assertEqual(jobMarketplace.job_listings, [{'job_title': 'Mechanical Engineer', 'company': 'XYZ Company', 'requirements': ['requirement3', 'requirement4']}])

    def test_post_job_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.post_job("Software Engineer", "ABC Company", ['requirement1', 'requirement2'])
        jobMarketplace.post_job("Mechanical Engineer", "XYZ Company", ['requirement3', 'requirement4'])
        self.assertEqual(jobMarketplace.job_listings, [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']}, {'job_title': 'Mechanical Engineer', 'company': 'XYZ Company', 'requirements': ['requirement3', 'requirement4']}])

import unittest

class AgentTest_post_job(unittest.TestCase):
    def test_post_job_1(self):
        jobMarketplace = JobMarketplace()
        result = jobMarketplace.post_job("Data Analyst", "DEF Company", ['requirement5'])
        self.assertIsNone(result)

    def test_post_job_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.post_job("Nurse", "Health Corp", [])
        self.assertEqual(jobMarketplace.job_listings, [{'job_title': 'Nurse', 'company': 'Health Corp', 'requirements': []}])
        self.assertEqual(set(jobMarketplace.job_listings[0].keys()), {'job_title', 'company', 'requirements'})

class JobMarketplaceTestRemoveJob(unittest.TestCase):
    def test_remove_job(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}]
        jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        self.assertEqual(jobMarketplace.job_listings, [])

    def test_remove_job_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}, {"job_title": "Mechanical Engineer", "company": "XYZ Company", "requirements": ['requirement3', 'requirement4']}]
        jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        self.assertEqual(jobMarketplace.job_listings, [{'job_title': 'Mechanical Engineer', 'company': 'XYZ Company', 'requirements': ['requirement3', 'requirement4']}])

    def test_remove_job_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']}, {"job_title": "Mechanical Engineer", "company": "XYZ Company", "requirements": ['requirement3', 'requirement4']}]
        jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        jobMarketplace.remove_job(jobMarketplace.job_listings[0])
        self.assertEqual(jobMarketplace.job_listings, [])

import unittest

class AgentTest_remove_job(unittest.TestCase):
    def test_remove_job_1(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [
            {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']},
            {"job_title": "Mechanical Engineer", "company": "XYZ Company", "requirements": ['requirement3', 'requirement4']},
            {"job_title": "Data Analyst", "company": "DEF Company", "requirements": ['requirement5']},
        ]
        jobMarketplace.remove_job(jobMarketplace.job_listings[2])
        self.assertEqual(jobMarketplace.job_listings, [
            {'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']},
            {'job_title': 'Mechanical Engineer', 'company': 'XYZ Company', 'requirements': ['requirement3', 'requirement4']},
        ])

    def test_remove_job_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [
            {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['requirement1', 'requirement2']},
            {"job_title": "Mechanical Engineer", "company": "XYZ Company", "requirements": ['requirement3', 'requirement4']},
            {"job_title": "Data Analyst", "company": "DEF Company", "requirements": ['requirement5']},
        ]
        result = jobMarketplace.remove_job(jobMarketplace.job_listings[1])
        self.assertIsNone(result)
        self.assertEqual(jobMarketplace.job_listings, [
            {'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['requirement1', 'requirement2']},
            {'job_title': 'Data Analyst', 'company': 'DEF Company', 'requirements': ['requirement5']},
        ])

class JobMarketplaceTestSubmitResume(unittest.TestCase):
    def test_submit_resume(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        self.assertEqual(jobMarketplace.resumes, [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}])

    def test_submit_resume_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        jobMarketplace.submit_resume("John", ['skill3', 'skill4'], "experience")
        self.assertEqual(jobMarketplace.resumes, [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}, {'name': 'John', 'skills': ['skill3', 'skill4'], 'experience': 'experience'}])

    def test_submit_resume_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        jobMarketplace.submit_resume("John", ['skill3', 'skill4'], "experience")
        jobMarketplace.submit_resume("Tom", ['skill1', 'skill2'], "experience")
        self.assertEqual(jobMarketplace.resumes, [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}, {'name': 'John', 'skills': ['skill3', 'skill4'], 'experience': 'experience'}, {'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}])

import unittest

class AgentTest_submit_resume(unittest.TestCase):
    def test_submit_resume_1(self):
        jobMarketplace = JobMarketplace()
        result = jobMarketplace.submit_resume("Alice", ['skill5'], "2 years")
        self.assertIsNone(result)

    def test_submit_resume_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Nurse", "company": "Health Corp", "requirements": []}]
        jobMarketplace.submit_resume("Bob", [], "none")
        self.assertEqual(len(jobMarketplace.resumes), 1)
        self.assertEqual(set(jobMarketplace.resumes[0].keys()), {'name', 'skills', 'experience'})
        self.assertEqual(jobMarketplace.resumes[0]['name'], 'Bob')
        self.assertEqual(jobMarketplace.resumes[0]['skills'], [])
        self.assertEqual(jobMarketplace.resumes[0]['experience'], 'none')
        self.assertEqual(jobMarketplace.job_listings, [{"job_title": "Nurse", "company": "Health Corp", "requirements": []}])

class JobMarketplaceTestWithdrawResume(unittest.TestCase):
    def test_withdraw_resume(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        self.assertEqual(jobMarketplace.resumes, [])

    def test_withdraw_resume_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}, {"name": "John", "skills": ['skill3', 'skill4'], "experience": "experience"}]
        jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        self.assertEqual(jobMarketplace.resumes, [{'name': 'John', 'skills': ['skill3', 'skill4'], 'experience': 'experience'}])

    def test_withdraw_resume_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}, {"name": "John", "skills": ['skill3', 'skill4'], "experience": "experience"}]
        jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        self.assertEqual(jobMarketplace.resumes, [])

import unittest

class AgentTest_withdraw_resume(unittest.TestCase):
    def test_withdraw_resume_1(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        result = jobMarketplace.withdraw_resume(jobMarketplace.resumes[0])
        self.assertIsNone(result)
        self.assertEqual(jobMarketplace.resumes, [])

    def test_withdraw_resume_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [
            {"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"},
            {"name": "John", "skills": ['skill3', 'skill4'], "experience": "experience"},
            {"name": "Alice", "skills": ['skill5'], "experience": "2 years"},
        ]
        jobMarketplace.withdraw_resume(jobMarketplace.resumes[2])
        self.assertEqual(jobMarketplace.resumes, [
            {'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'},
            {'name': 'John', 'skills': ['skill3', 'skill4'], 'experience': 'experience'},
        ])

class JobMarketplaceTestSearchJobs(unittest.TestCase):
    def test_search_jobs(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.search_jobs("skill1"), [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']}])

    def test_search_jobs_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}, {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill3', 'skill4']}]
        self.assertEqual(jobMarketplace.search_jobs("skill1"), [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']}])

    def test_search_jobs_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}, {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill3', 'skill4']}]
        self.assertEqual(jobMarketplace.search_jobs("skill3"), [{'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill3', 'skill4']}])

import unittest

class AgentTest_search_jobs(unittest.TestCase):
    def test_search_jobs_1(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.search_jobs("skill9"), [])

    def test_search_jobs_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.job_listings = [
            {"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']},
            {"job_title": "Data Analyst", "company": "DEF Company", "requirements": ['skill5']},
            {"job_title": "Mechanical Engineer", "company": "XYZ Company", "requirements": ['skill1', 'skill4']},
        ]
        self.assertEqual(jobMarketplace.search_jobs("skill1"), [
            {'job_title': 'Software Engineer', 'company': 'ABC Company', 'requirements': ['skill1', 'skill2']},
            {'job_title': 'Mechanical Engineer', 'company': 'XYZ Company', 'requirements': ['skill1', 'skill4']},
        ])

class JobMarketplaceTestGetJobApplicants(unittest.TestCase):
    def test_get_job_applicants(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}]
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0]), [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}])

    def test_get_job_applicants_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}, {"name": "John", "skills": ['skill3', 'skill4'], "experience": "experience"}]
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0]), [{'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'}])

    def test_get_job_applicants_3(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"}, {"name": "John", "skills": ['skill3', 'skill4'], "experience": "experience"}]
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill3', 'skill4']}]
        self.assertEqual(jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0]), [{'name': 'John', 'skills': ['skill3', 'skill4'], 'experience': 'experience'}])

import unittest

class AgentTest_get_job_applicants(unittest.TestCase):
    def test_get_job_applicants_1(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [{"name": "Mike", "skills": ['skill9'], "experience": "1 year"}]
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0]), [])

    def test_get_job_applicants_2(self):
        jobMarketplace = JobMarketplace()
        jobMarketplace.resumes = [
            {"name": "Tom", "skills": ['skill1', 'skill2'], "experience": "experience"},
            {"name": "Mike", "skills": ['skill9'], "experience": "1 year"},
            {"name": "Alice", "skills": ['skill1', 'skill2'], "experience": "2 years"},
        ]
        jobMarketplace.job_listings = [{"job_title": "Software Engineer", "company": "ABC Company", "requirements": ['skill1', 'skill2']}]
        self.assertEqual(jobMarketplace.get_job_applicants(jobMarketplace.job_listings[0]), [
            {'name': 'Tom', 'skills': ['skill1', 'skill2'], 'experience': 'experience'},
            {'name': 'Alice', 'skills': ['skill1', 'skill2'], 'experience': '2 years'},
        ])