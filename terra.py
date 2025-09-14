import subprocess

def terraform_run(command):
    # process = 
    subprocess.run(command, shell=True, check=True)#, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # print(process.stdout.decode())

directory = r"C:/Users/asksa/OneDrive/Desktop/Python/Terra-auomate/Project/terraform"
# command = f"terraform -chdir={directory} init"
# command = f"terraform -chdir={directory} plan"
# command = f"terraform -chdir={directory} apply -auto-approve"
command = f"terraform -chdir={directory} destroy -auto-approve"
# print(command)
terraform_run(command)