from sic_mapper import SicMapper
import warnings

warnings.filterwarnings("ignore")

job_ad = {'id': 1, 'job_text': 'We are looking for a software engineer to join our team. This company sits in the software engineering industry.'}
sm = SicMapper()
sm.load()
sic_code = sm.get_sic_codes(job_ad)
print(sic_code)