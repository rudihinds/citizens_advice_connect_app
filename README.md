# Service Opening Hours App
This is an application to determine whether a given service is open or closed for the current date.

## Prerequisites

Ensure you have the following installed and configured with appropriate access:
- AWS CLI
- Python 3.6 or later
- AWS CDK

## Storage Definitions

We are using AWS DynamoDB as our primary data store. The table schema is as follows:

- Table name: `ServicesTable`
- Primary key: `ServiceName` (String): The name of the service.
- Attributes:
  - `HolidayDates` (List of Strings): A list of holiday dates when the service is closed.

Note: each date could potentially be used as a primary key for a holiday item in a prospective Holidays table. This would enable us to provide more information about the holiday, such as holiday name etc which we could use to improve user experience in the future. It would also allow us to have a single source of truth for each holiday which could prevent errors when storing dates in the service holidays list.

## Environment Variables

Set the following environment variables:

- `SERVICES_TABLE`: The name of your DynamoDB table.
- `CONNECT_INSTANCE_ARN`: The ARN of your Connect instance.

## Setup Instructions
- Clone the repository
- Install dependencies
    - pip install -r requirements.txt
- Deploy the application with AWS CDK
    - cdk deploy
- seed the database
    - python seed_data.py

## CDK instructions
The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
# citizens_advice_connect_app
this is a Python CDK application to determine open status of a service for public holidays alongside AWS Connect
