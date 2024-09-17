# 🗺️ SIC Mapper

The high-level goal of the `SicMapper` is to map a given job advert to Standardised Industrial Classification (SIC) code.

# Installation

1. Create a Python 3.10 conda environment (we strongly recommend conda over e.g. venv due to usage of the faiss package)
2. Install the requirements file `conda install --yes --file requirements.txt`

## 🔨 Core functionality

To map job adverts to SIC codes, you can use the `SicMapper` class in `sic_mapper.py`:

```
from sic_mapper.sic_mapper import SicMapper

job_ad = {'id': 1, 'job_text': 'We are looking for a software engineer to join our team. This company sits in the software engineering industry.'}
sm = SicMapper()

sm.load() # load relevant models, tokenizers and datasets

sic_code = sm.get_sic_codes(job_ad) # get SIC codes for job advert

>> {1: {'company_description': 'This company sits in the software engineering industry..',
  'sic_code': '62012',
  'sic_name': 'Business and domestic software development',
  'sic_method': 'closest distance',
  'sic_confidence': 0.62}}
```

## 🖊️ Methodology

The SIC Mapper can be described in the following diagram:

<p align="center">
  <img src="https://github.com/nestauk/dap_prinz_green_jobs/assets/46863334/6e16b600-aaa9-46f4-9926-0ad4e772e2ef" />
</p>
