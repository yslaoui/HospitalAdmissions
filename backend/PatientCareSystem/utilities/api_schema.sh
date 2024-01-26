source activateme.sh 
pip install uritemplate
pip install pyyaml
python3 manage.py generateschema --format openapi-json > project_schema.json
# Make it available to the world in the static folder
rsync project_schema.json ./AdmissionTracker/static
