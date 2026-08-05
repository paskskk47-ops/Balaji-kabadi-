@echo off
echo ==========================================
echo Running Local SEO, Rates, and CTA Updates...
echo ==========================================
python update_ctas.py
python update_host.py
python add_robots_meta.py
python remove_html_ext.py
python rename_brand.py
python add_agency.py
python add_official_links.py
python add_gmb_link.py

echo ==========================================
echo Deploying Balaji Kabadi Website to GitHub
echo ==========================================

:: Initialize git repository if not already done
if not exist .git (
    echo Initializing Git repository...
    git init
    git checkout -b main
)

:: Configure remote URL
echo Setting remote origin to https://github.com/paskskk47-ops/Balaji-kabadi-.git ...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/paskskk47-ops/Balaji-kabadi-.git

:: Stage files
echo Staging all files...
git add -A

:: Commit files
echo Committing changes...
git commit -m "Deploy Balaji Kabadi website with updated CTA and Rates tables"

:: Push to GitHub
echo Pushing to main branch...
git push -u origin main

echo ==========================================
echo Deployment steps completed.
echo Please enable GitHub Pages in repository settings:
echo Settings -> Pages -> Build and deployment -> Branch: main (root) -> Save
echo ==========================================
pause
