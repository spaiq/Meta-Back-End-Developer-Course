/auth/users/                #Use this path to register
/restaurant/api-token-auth/ #Use this path to get your auth token
/restaurant/bookings/tables #Use this path to test
/restaurant/menu            #Use this path to test


Virtualenv installation:

To work with the project installing a venv is required. If you don't have it make sure to install it with the following command:

pip install virtualenv

You can do that by using the following command inside the project directory:

python -m venv venv

After that make sure to activate the venv using:
Windows:
venv\Scripts\activate

Mac:
source venv/bin/activate

Finally install all the necessary packages from requirements.txt using:
pip install <package_name>