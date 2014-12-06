import os
import argparse

def main():
  parser = argparse.ArgumentParser(description='TODO')
  parser.add_argument('-ho', '--host_dir', required=True)
  parser.add_argument('-s', '--submit_script', required=True)
  parser.add_argument('-ex', '--executable', required=True)
  args = parser.parse_args()

  ndata = [10**4, 10**5, 10**6, 10**7]
  nrepeat = [10**4, 10**3, 10**2, 10]

  machines = [2,4,8,16,31]

  for i, data in enumerate(ndata):
    for machine in machines:
      host_file = os.path.join(args.host_dir, 'hosts%d' % machine)
      cmd = 'python %s %d %s %s %d %d' % (args.submit_script, machine, host_file, args.executable, data, nrepeat[i])
      print 'data=%d, repeat=%d, machine=%d' % (data, nrepeat[i], machine)
      os.system(cmd)

if __name__ == "__main__":
  main()