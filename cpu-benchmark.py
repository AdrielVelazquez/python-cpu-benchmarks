import datetime
import platform
import math
from multiprocessing import Pool, cpu_count
from statistics import mean
from functools import reduce

recursive_sqrt = 50000000

def multi_process_test():
    start = datetime.datetime.now()
    for value in range(1, recursive_sqrt):
      math.sqrt(value)
    end = datetime.datetime.now()
    duration = (end - start).total_seconds() * 1000
    return duration

if __name__ == "__main__":
  os_version = platform.system()
  cpu_information = platform.processor()
  platform_information = platform.platform()
  print('CPU: {}'.format(cpu_information))
  print('Arch: {}'.format(platform_information))
  print('OS: {}'.format(os_version))
  jobs = []
  pool = Pool(cpu_count())
  start = datetime.datetime.now()
  for pi_compute in range(500):
      job = pool.apply_async(multi_process_test)
      jobs.append(job)

  final_times_per_process = []
  for job in jobs:
      final_times_per_process.append(job.get())
  end = datetime.datetime.now()
  duration = (end - start).total_seconds() * 1000
  print("Duration {} ms or {} seconds".format(duration, duration / 1000),)
  print("Average of all CPUs {} ms".format(mean(final_times_per_process)))