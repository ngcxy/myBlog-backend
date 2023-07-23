import boto3
from botocore.exceptions import ClientError
global secrets


class AWSSecretManager(object):

    def __init__(self):
        self._session = boto3.session.Session()
        self.client = self._session.client(
            service_name='secretsmanager',
            region_name="us-east-1"
        )
        self.secrets = self.get()

    def get(self):
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId="blog-app-image-s3"
            )

            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                print(secret)
                return secret
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e


_instance = AWSSecretManager()
response = _instance.get()
print(response)
