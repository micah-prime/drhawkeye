from drhawkeye.framework import HealthCheck
import os

cfg = './test_config.ini'
dr = HealthCheck(cfg)

print(dr.config)
