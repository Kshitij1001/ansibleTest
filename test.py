import ansible_runner

## r = ansible_runner.run(private_data_dir="/home/uteja70/testCode/playBooks", playbook="test1.yml")

r = ansible_runner.run(private_data_dir="/home/uteja70/testCode",
                       playbook="playBooks/test1.yml", inventory="inventory/file")

print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event["event"])
    print("Final status:")
    print(r.stats)
