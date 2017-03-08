"""
Gunicorn Configuration File.
"""
import multiprocessing

bind = '0.0.0.0:8080'
workers = multiprocessing.cpu_count() * 2 + 1
