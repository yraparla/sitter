source env/bin/activate
wget www.cafc.uscourts.gov/argument/upcoming-oral-arguments -O upcoming-oral-arguments.html
python sitter.py > sittings.json
git commit -am $(date +%Y%m%d)
git push origin master