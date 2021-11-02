# mpassive

### Running Server locally

```bash
# Change to the server directory
cd ./server

# Create a venv
python3 -m venv .

# Enable the virtual environment
source bin/activate

# Install libraries
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run django project
python manage.py runserver
```
