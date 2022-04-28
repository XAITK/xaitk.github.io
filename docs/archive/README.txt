Author: Elim Schenck, elim.schenck@kitware.com
Updated: 4/27/2022

This python script parses the "Capabilities" page of xaitk.org and aids in archiving the resources for each contribution.
The path to the website repo directory is specified in the script source.
The website repo is also bundled and added to the archive.
The script uses selenium to navigate to associated URLs.
Selenium requires a browser driver to be installed, see the following link for more info:
    https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
The script uses a Firefox browser currently.
A new directory "contribs" is created with a sub-directory for each contribution.

For papers, the script navigates to the associated URL and waits for user input to continue.
You should download the paper and place it in the folder created for the contribution.

For software, the script attempts to clone and bundle it as a git repo and place the bundle file in the contrib directory.
If this fails, it navigates to the URL for the user to figure out.
Repos are all cloned into their own sub-directory of "repos".
The "repos" directory can be deleted after the archive is complete.
To restore the original repos from the bundle file, you must have git installed.
You can then simply use git clone on each bundle.
For more information about git bundling, please view the related documentation:
    https://git-scm.com/book/en/v2/Git-Tools-Bundling

For demos, the script navigates to the URL and lets the user figure out what to do.

Currently, data entries are ignored for all contributions.


Contrib Notes:

    igos:
     - demo is a website that doesn't seem to exist

    equas:
     - demo is a website that doesn't seem to exist

    sbsm:
     - software is two files from SMQTK; not archived

    TalesFromTheCovidTrenches:
     - paper is behind IEEE paywall

    utdallas-ufl-xvs:
     - software points to specific branch of git repo, but the archived bundle is of the entire repo
     - demo is a web application; not archived

    fakesal:
     - empty, I think this was a template

    template:
     - empty, also a template I think

    psychological-models-explanatory-reasoning:
     - the resources are not listed in the yaml section of the markdown file; had to download manually

    discovery_platform:
     - demos are both web apps; not archived

    CRA_SC2_RL:
     - demo is a website; not archived

    explain_robot_behaviour_UCLA:
     - paper is behind science.org paywall
     - software is a link to a zip file that doesn't seem to exist, I think this might require a science.org account as well

    bayesian_teaching_rutgers:
     - 5th paper is behind SPIE paywall

    utdallas-ufl-xar-demo:
     - demo is a web app; not archived

    utd-ucla-juice:
     - software points to a group of github repos; archived the main repo
