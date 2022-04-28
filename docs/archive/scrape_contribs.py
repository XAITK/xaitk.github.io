import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

website_dir = '../../'

contrib_dir = os.path.join(website_dir, '_capabilities/')
contrib_files = os.listdir(contrib_dir)

base_dir = os.getcwd()

browser = webdriver.Firefox()

download_dir = './contribs/'
repo_dir = './repos/'

os.makedirs(download_dir, exist_ok=True)
os.makedirs(repo_dir, exist_ok=True)

print("Archiving website...")
os.chdir(website_dir)
os.system(f"git bundle create xaitk_website.bundle --all")
os.replace(
    os.path.join('xaitk_website.bundle'),
    os.path.join(base_dir, 'xaitk_website.bundle')
)
os.chdir(base_dir)
print('')

print("Downloading contributions...")
for idx, file in enumerate(contrib_files):
    # change number below to skip first n contribs
    start_idx = 1;
    if idx < start_idx-1:
        continue

    contrib_name = file.split('.')[0]
    os.makedirs(os.path.join(download_dir,contrib_name), exist_ok=True)
    
    contrib_file = os.path.join(contrib_dir, file)
    with open(contrib_file, 'r') as f:
        lines = f.readlines()

    yaml_start = lines.index('---\n')
    yaml_end = lines[yaml_start+1:].index('---\n')

    yaml_str = ''
    for line in lines[yaml_start:yaml_end+1]:
        yaml_str += line

    contrib = yaml.safe_load(yaml_str)
    
    sub = contrib['submission_details']
    
    print('')
    print(f"{idx+1} / {len(contrib_files)}")
    print(contrib_name)
    
    if contrib_name == 'fakesal' or contrib_name == 'template':
        continue
    
    for (resc_type, resc_list) in contrib['submission_details']['resources'].items():
        if resc_list == None:
            continue
        
        for resc in resc_list:
            print("-----------------------------------------------------------")
            if resc_type == 'software':
                print("Found software...")
                print("Trying to bundle...")
                url = resc['url']
                repo = url.split('/')[-1]
                
                if os.path.exists(os.path.join(download_dir, contrib_name, repo+'.bundle')):
                    print("Software already bundled")
                    continue
                    
                os.chdir(repo_dir)
                try:
                    print("Cloning repo...")
                    os.system(f"git clone -q {url}")
                    repo = url.split('/')[-1]
                    os.chdir(repo)
                    print("Bundling repo...")
                    os.system(f"git bundle create {repo}.bundle --all")
                    os.chdir(base_dir)
                    os.replace(
                        os.path.join(repo_dir,repo,repo+'.bundle'),
                        os.path.join(download_dir, contrib_name, repo+'.bundle')
                    )
                except:
                    print("Git bundle failed, navigating to URL...")
                    os.chdir(base_dir)
                    
                    browser.get(url)
                    input("Press enter to continue...")
                    
            if resc_type == 'papers':
                print("Found paper, navigating to URL...")
                url = resc['url']
                try:
                    browser.get(url)
                except:
                    print(f"Navigating to paper url failed: {url}")
                input("Press enter to continue...")
            if resc_type == 'demos':
                print("Found demo, navigation to URL...")
                url = resc['url']
                try:
                    browser.get(url)
                except:
                    print(f"Navigating to demo url failed: {url}")
                input("Press enter to continue...")
            if resc_type == 'data':
                print("Skipping data")
                continue
