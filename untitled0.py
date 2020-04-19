#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:50:50 2020

@author: mcruzmbp2019
"""

import glassdoor_scraper as gs
import pandas as pd
path = "/Users/mcruzmbp2019/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data analyst', 5, False, path, 10)

df.to_csv('glassdoor_jobs.csv', index = False)